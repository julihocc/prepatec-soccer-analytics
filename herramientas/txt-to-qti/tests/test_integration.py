#!/usr/bin/env python3
"""
Tests de integración para el pipeline completo TXT → CSV → QTI
Valida que todo el flujo funcione correctamente de extremo a extremo
"""

import unittest
import os
import sys
import tempfile
import zipfile
import xml.etree.ElementTree as ET
import csv
from pathlib import Path

# Agregar el directorio padre al path para importar los módulos
parent_dir = Path(__file__).parent.parent
sys.path.insert(0, str(parent_dir))

from txt_to_csv_direct import TxtToCSVConverter
from csv_to_kansas_qti import KansasQTIGenerator

class TestFullPipeline(unittest.TestCase):
    """Tests del pipeline completo: TXT → CSV → QTI → Validación"""
    
    def setUp(self):
        """Configuración inicial"""
        self.test_dir = Path(__file__).parent
        self.temp_files = []  # Para limpiar archivos temporales
        
    def tearDown(self):
        """Limpieza de archivos temporales"""
        for file_path in self.temp_files:
            if os.path.exists(file_path):
                os.unlink(file_path)
                
    def create_temp_file(self, content, suffix='.txt'):
        """Helper para crear archivos temporales"""
        tmp_file = tempfile.NamedTemporaryFile(mode='w', suffix=suffix, delete=False, encoding='utf-8')
        tmp_file.write(content)
        tmp_file.close()
        self.temp_files.append(tmp_file.name)
        return tmp_file.name
        
    def test_complete_pipeline_valid_questions(self):
        """Test del pipeline completo con preguntas válidas"""
        
        # 1. Crear archivo TXT de prueba
        txt_content = """Q1: Pregunta de test numero uno?
A) Primera opcion
B) Segunda opcion
C) Tercera opcion
D) Cuarta opcion
RESPUESTA: B

Q2: Segunda pregunta de prueba?
A) Opcion A
B) Opcion B
RESPUESTA: A

Q3: Tercera pregunta con caracteres especiales: ¿cuál?
A) Opción con acentos
B) Opción normal
C) Opción con símbolos +/-
D) Otra opción
RESPUESTA: C"""
        
        txt_file = self.create_temp_file(txt_content, '.txt')
        
        # 2. Convertir TXT → CSV
        converter = TxtToCSVConverter()
        csv_file, question_count = converter.convert_to_csv(txt_file)
        self.temp_files.append(csv_file)
        
        # Verificar conversión TXT → CSV
        self.assertEqual(question_count, 3)
        self.assertTrue(os.path.exists(csv_file))
        
        # Verificar contenido del CSV
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            csv_rows = list(reader)
            
        self.assertEqual(len(csv_rows), 3)
        
        # Verificar formato CSV
        row1 = csv_rows[0]
        self.assertEqual(row1[0], 'MC')        # Tipo
        self.assertEqual(row1[2], '1.0')       # Puntos
        self.assertEqual(row1[4], '2')         # Respuesta B=2
        self.assertIn('numero uno', row1[3])   # Texto pregunta
        
        # 3. Convertir CSV → QTI
        generator = KansasQTIGenerator()
        qti_file, qti_question_count, xml_name = generator.convert_csv_to_kansas_qti(csv_file)
        self.temp_files.append(qti_file)
        
        # Verificar conversión CSV → QTI
        self.assertEqual(qti_question_count, 3)
        self.assertTrue(os.path.exists(qti_file))
        self.assertTrue(xml_name.endswith('.xml'))
        
        # 4. Validar contenido del QTI
        with zipfile.ZipFile(qti_file, 'r') as zf:
            files = zf.namelist()
            self.assertEqual(len(files), 1)
            self.assertTrue(files[0].endswith('.xml'))
            
            # Leer y validar XML
            xml_content = zf.read(files[0])
            root = ET.fromstring(xml_content)
            
            # Verificar estructura QTI
            self.assertEqual(root.tag, 'questestinterop')
            
            # Verificar namespace
            self.assertEqual(root.get('xmlns'), 'http://www.imsglobal.org/xsd/ims_qtiasiv1p2')
            
            # Verificar assessment
            assessment = root.find('assessment')
            self.assertIsNotNone(assessment)
            
            # Verificar items
            items = assessment.findall('.//item')
            self.assertEqual(len(items), 3)
            
            # Verificar primera pregunta
            first_item = items[0]
            mattext = first_item.find('.//material/mattext')
            self.assertIsNotNone(mattext)
            self.assertIn('numero uno', mattext.text)
            
            # Verificar respuesta correcta de primera pregunta
            varequal = first_item.find('.//resprocessing/respcondition/conditionvar/varequal')
            self.assertIsNotNone(varequal)
            self.assertEqual(varequal.text, '1001')  # B = índice 1 → 1001
            
    def test_pipeline_with_edge_cases(self):
        """Test del pipeline con casos especiales"""
        
        txt_content = """Q1: Pregunta con comillas "dobles" y 'simples'?
A) Respuesta con, comas
B) Respuesta "con comillas"
C) Respuesta normal
RESPUESTA: A

Q2: Pregunta muy larga que podría causar problemas de formato en CSV si no se maneja adecuadamente?
A) Respuesta muy larga que también podría ser problemática
B) OK
RESPUESTA: B"""
        
        txt_file = self.create_temp_file(txt_content, '.txt')
        
        # Pipeline completo
        converter = TxtToCSVConverter()
        csv_file, _ = converter.convert_to_csv(txt_file)
        self.temp_files.append(csv_file)
        
        generator = KansasQTIGenerator()
        qti_file, question_count, _ = generator.convert_csv_to_kansas_qti(csv_file)
        self.temp_files.append(qti_file)
        
        # Verificar que maneja casos especiales
        self.assertEqual(question_count, 2)
        
        # Verificar que el QTI es válido
        with zipfile.ZipFile(qti_file, 'r') as zf:
            xml_content = zf.read(zf.namelist()[0])
            root = ET.fromstring(xml_content)  # No debe lanzar excepción
            
            # Verificar que las comillas se manejan correctamente
            items = root.findall('.//item')
            first_mattext = items[0].find('.//material/mattext').text
            self.assertIn('comillas', first_mattext)
            
    def test_pipeline_error_handling(self):
        """Test de manejo de errores en el pipeline"""
        
        # Archivo con preguntas inválidas
        txt_content = """Q1: Pregunta sin respuesta?
A) Opcion A
B) Opcion B

Q3: Pregunta con salto en numeracion?
A) Opcion A
RESPUESTA: A"""
        
        txt_file = self.create_temp_file(txt_content, '.txt')
        
        # La conversión debe manejar errores gracefully
        converter = TxtToCSVConverter()
        csv_file, question_count = converter.convert_to_csv(txt_file)
        self.temp_files.append(csv_file)
        
        # Solo debe procesar 1 pregunta válida
        self.assertEqual(question_count, 1)
        
        # Verificar validaciones
        issues = converter.validate_questions(converter.questions)
        self.assertTrue(len(issues) > 0)  # Debe detectar problemas
        
    def test_real_question_bank(self):
        """Test con el banco de preguntas real del proyecto"""
        
        real_file = self.test_dir.parent / "banco-preguntas-bloque1.txt"
        if not real_file.exists():
            self.skipTest("Archivo real de preguntas no encontrado")
            
        # Pipeline completo con archivo real
        converter = TxtToCSVConverter()
        csv_file, question_count = converter.convert_to_csv(str(real_file))
        self.temp_files.append(csv_file)
        
        # Verificar que procesa todas las preguntas
        self.assertEqual(question_count, 25)  # Banco actual tiene 25 preguntas
        
        # Generar QTI
        generator = KansasQTIGenerator()
        qti_file, qti_count, _ = generator.convert_csv_to_kansas_qti(csv_file)
        self.temp_files.append(qti_file)
        
        self.assertEqual(qti_count, 25)
        
        # Validar QTI final
        with zipfile.ZipFile(qti_file, 'r') as zf:
            xml_content = zf.read(zf.namelist()[0])
            root = ET.fromstring(xml_content)
            
            items = root.findall('.//item')
            self.assertEqual(len(items), 25)
            
    def test_character_encoding_consistency(self):
        """Test de consistencia de encoding a través del pipeline"""
        
        txt_content = """Q1: Pregunta con acentos: ¿Cuál es la respuesta correcta?
A) Opción con ñ y acentos: á, é, í, ó, ú
B) Respuesta normal
C) Símbolos matemáticos: ≤, ≥, ≠
D) Caracteres especiales: @, #, $, %
RESPUESTA: A"""
        
        txt_file = self.create_temp_file(txt_content, '.txt')
        
        # Pipeline completo
        converter = TxtToCSVConverter()
        csv_file, _ = converter.convert_to_csv(txt_file)
        self.temp_files.append(csv_file)
        
        # Verificar que el CSV mantiene los caracteres
        with open(csv_file, 'r', encoding='utf-8') as f:
            csv_content = f.read()
            self.assertIn('¿Cuál', csv_content)
            self.assertIn('ñ y acentos', csv_content)
            
        # Generar QTI
        generator = KansasQTIGenerator()
        qti_file, _, _ = generator.convert_csv_to_kansas_qti(csv_file)
        self.temp_files.append(qti_file)
        
        # Verificar encoding en QTI (ISO-8859-1)
        with zipfile.ZipFile(qti_file, 'r') as zf:
            xml_bytes = zf.read(zf.namelist()[0])
            xml_str = xml_bytes.decode('iso-8859-1')
            
            # Verificar declaración de encoding
            self.assertIn('encoding="ISO-8859-1"', xml_str)
            
            # Verificar que XML es parseable
            root = ET.fromstring(xml_bytes)
            mattext = root.find('.//material/mattext')
            
            # Los caracteres deben estar presentes (posiblemente convertidos)
            self.assertIsNotNone(mattext.text)

class TestPerformance(unittest.TestCase):
    """Tests básicos de rendimiento"""
    
    def setUp(self):
        self.temp_files = []
        
    def tearDown(self):
        for file_path in self.temp_files:
            if os.path.exists(file_path):
                os.unlink(file_path)
                
    def test_large_question_bank(self):
        """Test con banco de preguntas grande (100 preguntas)"""
        
        # Generar 100 preguntas de prueba
        questions = []
        for i in range(1, 101):
            questions.append(f"""Q{i}: Pregunta número {i} de prueba?
A) Opción A para pregunta {i}
B) Opción B para pregunta {i}
C) Opción C para pregunta {i}
D) Opción D para pregunta {i}
RESPUESTA: {['A', 'B', 'C', 'D'][i % 4]}

""")
        
        txt_content = ''.join(questions)
        
        # Crear archivo temporal
        tmp_file = tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False, encoding='utf-8')
        tmp_file.write(txt_content)
        tmp_file.close()
        self.temp_files.append(tmp_file.name)
        
        # Pipeline completo
        import time
        
        start_time = time.time()
        
        converter = TxtToCSVConverter()
        csv_file, question_count = converter.convert_to_csv(tmp_file.name)
        self.temp_files.append(csv_file)
        
        generator = KansasQTIGenerator()
        qti_file, qti_count, _ = generator.convert_csv_to_kansas_qti(csv_file)
        self.temp_files.append(qti_file)
        
        end_time = time.time()
        processing_time = end_time - start_time
        
        # Verificar que procesa correctamente
        self.assertEqual(question_count, 100)
        self.assertEqual(qti_count, 100)
        
        # Verificar que es razonablemente rápido (menos de 10 segundos)
        self.assertLess(processing_time, 10.0, f"Procesamiento tomó {processing_time:.2f}s, demasiado lento")
        
        print(f"\n✅ Procesadas 100 preguntas en {processing_time:.2f} segundos")

if __name__ == '__main__':
    unittest.main(verbosity=2)