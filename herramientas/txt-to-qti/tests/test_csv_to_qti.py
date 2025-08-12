#!/usr/bin/env python3
"""
Tests para el convertidor CSV a QTI
Valida el funcionamiento correcto de csv_to_kansas_qti.py
"""

import unittest
import os
import sys
import tempfile
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

# Agregar el directorio padre al path para importar el módulo
parent_dir = Path(__file__).parent.parent
sys.path.insert(0, str(parent_dir))

from csv_to_kansas_qti import KansasQTIGenerator

class TestKansasQTIGenerator(unittest.TestCase):
    
    def setUp(self):
        """Configuración inicial para cada test"""
        self.generator = KansasQTIGenerator()
        self.test_dir = Path(__file__).parent
        
    def create_test_csv(self, content):
        """Helper para crear archivos CSV temporales"""
        tmp_file = tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False, encoding='utf-8')
        tmp_file.write(content)
        tmp_file.close()
        return tmp_file.name
        
    def test_id_generation(self):
        """Test de generación de IDs únicos y reproducibles"""
        # Los IDs deben ser reproducibles
        id1 = self.generator.generate_item_id(1)
        id2 = self.generator.generate_item_id(1)
        self.assertEqual(id1, id2, "Los IDs deben ser reproducibles")
        
        # Los IDs deben ser únicos para diferentes preguntas
        id3 = self.generator.generate_item_id(2)
        self.assertNotEqual(id1, id3, "Los IDs deben ser únicos")
        
        # Los IDs deben empezar con 'i'
        self.assertTrue(id1.startswith('i'), "Los IDs deben empezar con 'i'")
        
    def test_csv_reading(self):
        """Test de lectura de archivos CSV"""
        csv_content = '''MC,,1.0,Pregunta de prueba?,2,Opcion A,Opcion B,Opcion C,Opcion D
MC,,1.0,Segunda pregunta?,1,Si,No,,'''
        
        csv_file = self.create_test_csv(csv_content)
        
        try:
            questions = self.generator.read_csv_questions(csv_file)
            
            # Verificar que lee correctamente
            self.assertEqual(len(questions), 2, "Debe leer 2 preguntas")
            
            # Verificar primera pregunta
            q1 = questions[0]
            self.assertEqual(q1['number'], 1)
            self.assertEqual(q1['type'], 'MC')
            self.assertEqual(q1['points'], '1.0')
            self.assertEqual(q1['text'], 'Pregunta de prueba?')
            self.assertEqual(q1['correct_num'], 2)
            self.assertEqual(q1['choices'], ['Opcion A', 'Opcion B', 'Opcion C', 'Opcion D'])
            
            # Verificar segunda pregunta
            q2 = questions[1]
            self.assertEqual(q2['correct_num'], 1)
            self.assertEqual(q2['choices'], ['Si', 'No', '', ''])  # Opciones vacías
            
        finally:
            os.unlink(csv_file)
            
    def test_qti_item_creation(self):
        """Test de creación de items QTI"""
        question = {
            'number': 1,
            'type': 'MC',
            'points': '1.0',
            'text': 'Pregunta de test?',
            'correct_num': 2,
            'choices': ['Opcion A', 'Opcion B', 'Opcion C', 'Opcion D']
        }
        
        item = self.generator.create_qti_item(question)
        
        # Verificar estructura básica
        self.assertEqual(item.tag, 'item')
        self.assertTrue(item.get('ident').startswith('i'))
        self.assertEqual(item.get('title'), 'Question 1')
        
        # Verificar metadatos
        metadata = item.find('itemmetadata/qtimetadata')
        self.assertIsNotNone(metadata)
        
        # Verificar que tiene tipo de pregunta
        question_type_field = None
        for field in metadata.findall('qtimetadatafield'):
            label = field.find('fieldlabel')
            if label is not None and label.text == 'question_type':
                question_type_field = field.find('fieldentry')
                break
        
        self.assertIsNotNone(question_type_field)
        self.assertEqual(question_type_field.text, 'multiple_choice_question')
        
        # Verificar presentación
        presentation = item.find('presentation')
        self.assertIsNotNone(presentation)
        
        # Verificar texto de la pregunta
        mattext = presentation.find('material/mattext')
        self.assertIsNotNone(mattext)
        self.assertEqual(mattext.text, 'Pregunta de test?')
        
        # Verificar opciones
        render_choice = presentation.find('response_lid/render_choice')
        self.assertIsNotNone(render_choice)
        
        response_labels = render_choice.findall('response_label')
        self.assertEqual(len(response_labels), 4, "Debe tener 4 opciones")
        
        # Verificar procesamiento de respuestas
        resprocessing = item.find('resprocessing')
        self.assertIsNotNone(resprocessing)
        
    def test_assessment_creation(self):
        """Test de creación de assessment completo"""
        questions = [
            {
                'number': 1,
                'type': 'MC',
                'points': '1.0',
                'text': 'Primera pregunta?',
                'correct_num': 1,
                'choices': ['A', 'B', 'C', 'D']
            },
            {
                'number': 2,
                'type': 'MC',
                'points': '1.0',
                'text': 'Segunda pregunta?',
                'correct_num': 2,
                'choices': ['X', 'Y', 'Z', '']
            }
        ]
        
        assessment = self.generator.create_assessment(questions, "test_assessment")
        
        # Verificar estructura del assessment
        self.assertEqual(assessment.tag, 'questestinterop')
        
        # Verificar namespaces
        self.assertEqual(assessment.get('xmlns'), self.generator.qti_namespace)
        
        # Verificar assessment interno
        assessment_elem = assessment.find('assessment')
        self.assertIsNotNone(assessment_elem)
        self.assertEqual(assessment_elem.get('title'), 'test_assessment')
        
        # Verificar sección
        section = assessment_elem.find('section')
        self.assertIsNotNone(section)
        
        # Verificar items
        items = section.findall('item')
        self.assertEqual(len(items), 2, "Debe tener 2 items")
        
    def test_xml_formatting(self):
        """Test del formateo XML estilo Kansas State"""
        questions = [{
            'number': 1,
            'type': 'MC',
            'points': '1.0',
            'text': 'Test?',
            'correct_num': 1,
            'choices': ['A', 'B', '', '']
        }]
        
        assessment = self.generator.create_assessment(questions, "test")
        xml_content = self.generator.format_xml_kansas_style(assessment)
        
        # Verificar declaración XML
        self.assertTrue(xml_content.startswith('<?xml version="1.0" encoding="ISO-8859-1"?>'))
        
        # Verificar que es XML válido
        try:
            ET.fromstring(xml_content.encode('iso-8859-1'))
        except ET.ParseError:
            self.fail("El XML generado no es válido")
            
    def test_full_conversion(self):
        """Test de conversión completa CSV a QTI"""
        csv_content = '''MC,,1.0,Test question?,1,Yes,No,,
MC,,1.0,Another test?,2,A,B,C,D'''
        
        csv_file = self.create_test_csv(csv_content)
        
        try:
            output_zip, question_count, xml_name = self.generator.convert_csv_to_kansas_qti(csv_file)
            
            # Verificar que se creó el archivo ZIP
            self.assertTrue(os.path.exists(output_zip))
            self.assertEqual(question_count, 2)
            
            # Verificar contenido del ZIP
            with zipfile.ZipFile(output_zip, 'r') as zf:
                files = zf.namelist()
                self.assertEqual(len(files), 1, "El ZIP debe contener solo 1 archivo XML")
                self.assertTrue(files[0].endswith('.xml'))
                
                # Verificar que el XML es válido
                xml_content = zf.read(files[0])
                try:
                    ET.fromstring(xml_content)
                except ET.ParseError:
                    self.fail("El XML dentro del ZIP no es válido")
            
            # Limpiar archivos temporales
            os.unlink(output_zip)
            
        finally:
            os.unlink(csv_file)
            
    def test_file_not_found(self):
        """Test con archivo CSV inexistente"""
        with self.assertRaises(FileNotFoundError):
            self.generator.convert_csv_to_kansas_qti("archivo_inexistente.csv")
            
    def test_empty_csv(self):
        """Test con CSV vacío"""
        csv_file = self.create_test_csv("")
        
        try:
            with self.assertRaises(ValueError):
                self.generator.convert_csv_to_kansas_qti(csv_file)
        finally:
            os.unlink(csv_file)
            
    def test_malformed_csv(self):
        """Test con CSV mal formateado"""
        csv_content = '''MC,1.0,Pregunta incompleta
Linea sin formato correcto'''
        
        csv_file = self.create_test_csv(csv_content)
        
        try:
            questions = self.generator.read_csv_questions(csv_file)
            # Debe ignorar filas mal formateadas
            self.assertEqual(len(questions), 0)
        finally:
            os.unlink(csv_file)

class TestQTICompliance(unittest.TestCase):
    """Tests para verificar cumplimiento del estándar QTI"""
    
    def setUp(self):
        self.generator = KansasQTIGenerator()
        
    def test_qti_namespaces(self):
        """Test de namespaces QTI correctos"""
        self.assertEqual(
            self.generator.qti_namespace,
            'http://www.imsglobal.org/xsd/ims_qtiasiv1p2'
        )
        self.assertEqual(
            self.generator.xsi_namespace,
            'http://www.w3.org/2001/XMLSchema-instance'
        )
        
    def test_choice_id_format(self):
        """Test del formato de IDs de opciones"""
        question = {
            'number': 5,
            'type': 'MC',
            'points': '1.0',
            'text': 'Test?',
            'correct_num': 1,
            'choices': ['A', 'B', 'C', 'D']
        }
        
        item = self.generator.create_qti_item(question)
        render_choice = item.find('presentation/response_lid/render_choice')
        response_labels = render_choice.findall('response_label')
        
        # Verificar formato de IDs: [numero][indice]
        expected_ids = ['5000', '5001', '5002', '5003']
        actual_ids = [label.get('ident') for label in response_labels]
        
        self.assertEqual(actual_ids, expected_ids)
        
    def test_response_processing(self):
        """Test del procesamiento de respuestas"""
        question = {
            'number': 1,
            'type': 'MC',
            'points': '1.0',
            'text': 'Test?',
            'correct_num': 3,  # Respuesta C
            'choices': ['A', 'B', 'C', 'D']
        }
        
        item = self.generator.create_qti_item(question)
        
        # Verificar respuesta correcta
        varequal = item.find('resprocessing/respcondition/conditionvar/varequal')
        self.assertIsNotNone(varequal)
        self.assertEqual(varequal.text, '1002')  # C = índice 2 -> 1002
        
        # Verificar variable de puntuación
        setvar = item.find('resprocessing/respcondition/setvar')
        self.assertIsNotNone(setvar)
        self.assertEqual(setvar.get('varname'), 'SCORE')
        self.assertEqual(setvar.text, '100')

if __name__ == '__main__':
    unittest.main(verbosity=2)