#!/usr/bin/env python3
"""
Convertidor CSV a QTI que imita exactamente la estructura del Kansas State Converter
Genera QTI con la misma estructura que produce el conversor oficial

Uso:
    python csv_to_kansas_qti.py banco-preguntas-bloque1_kansas.csv

Genera:
    - Archivo ZIP QTI idéntico al de Kansas State
    - Solo XML (sin manifest como hace Kansas State)
    - Estructura exacta para Canvas
"""

import csv
import xml.etree.ElementTree as ET
from xml.dom import minidom
import zipfile
import os
import sys
import hashlib

class KansasQTIGenerator:
    def __init__(self):
        # Namespace exacto del Kansas State Converter
        self.qti_namespace = 'http://www.imsglobal.org/xsd/ims_qtiasiv1p2'
        self.xsi_namespace = 'http://www.w3.org/2001/XMLSchema-instance'
        self.schema_location = 'http://www.imsglobal.org/xsd/ims_qtiasiv1p2 http://www.imsglobal.org/xsd/ims_qtiasiv1p2p1.xsd'
    
    def generate_item_id(self, question_num):
        """Genera ID de item con hash como hace Kansas State"""
        # Crear hash único pero reproducible
        hash_input = f"question_{question_num}_item"
        hash_obj = hashlib.md5(hash_input.encode())
        return f"i{hash_obj.hexdigest()}"
    
    def generate_assessment_id(self, filename):
        """Genera ID de assessment con hash"""
        hash_input = f"assessment_{filename}"
        hash_obj = hashlib.md5(hash_input.encode())
        return f"i{hash_obj.hexdigest()}"
    
    def read_csv_questions(self, csv_file):
        """Lee preguntas del CSV en formato Kansas State"""
        questions = []
        
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            
            for row_num, row in enumerate(reader, 1):
                if len(row) < 9:
                    continue
                
                # Formato: MC,,1.0,pregunta,respuesta_num,A,B,C,D
                question = {
                    'number': row_num,
                    'type': row[0],           # MC
                    'points': row[2],         # 1.0
                    'text': row[3],           # Pregunta
                    'correct_num': int(row[4]), # 1-4
                    'choices': [
                        row[5],  # Choice A  
                        row[6],  # Choice B
                        row[7],  # Choice C
                        row[8] if len(row) > 8 else ""  # Choice D
                    ]
                }
                questions.append(question)
        
        return questions
    
    def create_qti_item(self, question):
        """Crea item QTI con estructura exacta de Kansas State"""
        item_id = self.generate_item_id(question['number'])
        
        # Item principal
        item = ET.Element('item', {
            'ident': item_id,
            'title': f"Question {question['number']}"
        })
        
        # Metadatos del item (estructura Kansas State)
        itemmetadata = ET.SubElement(item, 'itemmetadata')
        qtimetadata = ET.SubElement(itemmetadata, 'qtimetadata')
        
        # Tipo de pregunta
        field1 = ET.SubElement(qtimetadata, 'qtimetadatafield')
        ET.SubElement(field1, 'fieldlabel').text = 'question_type'
        ET.SubElement(field1, 'fieldentry').text = 'multiple_choice_question'
        
        # Puntos
        field2 = ET.SubElement(qtimetadata, 'qtimetadatafield')
        ET.SubElement(field2, 'fieldlabel').text = 'points_possible'
        ET.SubElement(field2, 'fieldentry').text = question['points']
        
        # ID de referencia (como hace Kansas State)
        field3 = ET.SubElement(qtimetadata, 'qtimetadatafield')
        ET.SubElement(field3, 'fieldlabel').text = 'assessment_question_identifierref'
        ref_id = self.generate_item_id(f"ref_{question['number']}")
        ET.SubElement(field3, 'fieldentry').text = ref_id
        
        # Presentación
        presentation = ET.SubElement(item, 'presentation')
        
        # Material de la pregunta (text/html como Kansas State)
        material = ET.SubElement(presentation, 'material')
        mattext = ET.SubElement(material, 'mattext', {'texttype': 'text/html'})
        mattext.text = question['text']
        
        # Respuestas (estructura Kansas State)
        response_lid = ET.SubElement(presentation, 'response_lid', {
            'ident': 'response1',
            'rcardinality': 'Single'
        })
        
        render_choice = ET.SubElement(response_lid, 'render_choice')
        
        # Crear opciones con IDs numéricos como Kansas State
        for i, choice_text in enumerate(question['choices']):
            if choice_text.strip():  # Solo si hay texto
                choice_id = f"{question['number']}{i:03d}"  # Formato: 1000, 1001, 1002, 1003
                
                response_label = ET.SubElement(render_choice, 'response_label', {
                    'ident': choice_id
                })
                choice_material = ET.SubElement(response_label, 'material')
                choice_mattext = ET.SubElement(choice_material, 'mattext', {
                    'texttype': 'text/plain'  # Kansas State usa text/plain
                })
                choice_mattext.text = choice_text.strip()
        
        # Procesamiento de respuestas (estructura Kansas State)
        resprocessing = ET.SubElement(item, 'resprocessing')
        
        # Outcomes
        outcomes = ET.SubElement(resprocessing, 'outcomes')
        decvar = ET.SubElement(outcomes, 'decvar', {
            'maxvalue': '100',
            'minvalue': '0', 
            'varname': 'SCORE',
            'vartype': 'Decimal'
        })
        
        # Respuesta correcta
        correct_choice_id = f"{question['number']}{(question['correct_num']-1):03d}"
        
        respcondition = ET.SubElement(resprocessing, 'respcondition', {
            'continue': 'No'
        })
        conditionvar = ET.SubElement(respcondition, 'conditionvar')
        varequal = ET.SubElement(conditionvar, 'varequal', {
            'respident': 'response1'
        })
        varequal.text = correct_choice_id
        
        setvar = ET.SubElement(respcondition, 'setvar', {
            'action': 'Set',
            'varname': 'SCORE'
        })
        setvar.text = '100'
        
        return item
    
    def create_assessment(self, questions, base_filename):
        """Crea assessment con estructura exacta de Kansas State"""
        assessment_id = self.generate_assessment_id(base_filename)
        
        # Root element con encoding ISO-8859-1 como Kansas State
        questestinterop = ET.Element('questestinterop', {
            'xmlns': self.qti_namespace,
            'xmlns:xsi': self.xsi_namespace,
            'xsi:schemaLocation': self.schema_location
        })
        
        # Assessment
        assessment = ET.SubElement(questestinterop, 'assessment', {
            'ident': assessment_id,
            'title': base_filename
        })
        
        # Metadatos mínimos como Kansas State
        qtimetadata = ET.SubElement(assessment, 'qtimetadata')
        field = ET.SubElement(qtimetadata, 'qtimetadatafield')
        ET.SubElement(field, 'fieldlabel').text = 'cc_maxattempts'
        ET.SubElement(field, 'fieldentry').text = '1'
        
        # Sección principal
        section = ET.SubElement(assessment, 'section', {
            'ident': 'root_section'
        })
        
        # Agregar todos los items
        for question in questions:
            item = self.create_qti_item(question)
            section.append(item)
        
        return questestinterop
    
    def format_xml_kansas_style(self, elem):
        """Formatea XML exactamente como Kansas State (con ISO-8859-1)"""
        rough_string = ET.tostring(elem, encoding='unicode')
        reparsed = minidom.parseString(rough_string)
        
        # Obtener XML sin la declaración de minidom
        xml_str = reparsed.toprettyxml(indent="  ")[23:]  # Remover declaración
        
        # Agregar declaración Kansas State
        kansas_declaration = '<?xml version="1.0" encoding="ISO-8859-1"?>\n'
        
        return kansas_declaration + xml_str
    
    def convert_csv_to_kansas_qti(self, csv_file, output_zip=None):
        """Convierte CSV a QTI con estructura exacta de Kansas State"""
        if not os.path.exists(csv_file):
            raise FileNotFoundError(f"Archivo no encontrado: {csv_file}")
        
        # Leer preguntas
        questions = self.read_csv_questions(csv_file)
        
        if not questions:
            raise ValueError("No se encontraron preguntas en el CSV")
        
        # Generar nombres (como Kansas State)
        base_name = os.path.splitext(os.path.basename(csv_file))[0]
        xml_filename = f"{base_name}_{abs(hash(base_name)) % 1000000000}.xml"
        
        if output_zip is None:
            output_zip = f"{base_name}_kansas_qti.zip"
        
        # Crear assessment
        assessment_xml = self.create_assessment(questions, base_name)
        
        # Formatear como Kansas State
        xml_content = self.format_xml_kansas_style(assessment_xml)
        
        # Crear ZIP con solo el XML (como Kansas State - sin manifest)
        with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zf:
            zf.writestr(xml_filename, xml_content.encode('iso-8859-1'))
        
        return output_zip, len(questions), xml_filename

def main():
    if len(sys.argv) != 2:
        print("Uso: python csv_to_kansas_qti.py <archivo_csv>")
        print("Ejemplo: python csv_to_kansas_qti.py banco-preguntas-bloque1_kansas.csv")
        sys.exit(1)
    
    csv_file = sys.argv[1]
    
    try:
        generator = KansasQTIGenerator()
        output_file, question_count, xml_name = generator.convert_csv_to_kansas_qti(csv_file)
        
        print(f"QTI generado (estilo Kansas State): {output_file}")
        print(f"Archivo XML interno: {xml_name}")
        print(f"Preguntas procesadas: {question_count}")
        print(f"Encoding: ISO-8859-1 (como Kansas State)")
        print(f"Estructura: Solo XML (sin manifest)")
        print(f"\nPara importar en Canvas:")
        print(f"1. Ve a tu curso en Canvas")
        print(f"2. Configuración -> Importar contenido del curso")
        print(f"3. Selecciona 'Paquete QTI'")
        print(f"4. Sube el archivo: {output_file}")
        print(f"5. Las preguntas aparecerán en tu banco")
        
    except Exception as e:
        print(f"ERROR: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()