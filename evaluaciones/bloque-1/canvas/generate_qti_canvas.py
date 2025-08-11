#!/usr/bin/env python3
"""
Generador de archivos QTI compatibles con Canvas LMS
Convierte banco de preguntas JSON a formato QTI empaquetado en ZIP

Uso:
    python generate_qti_canvas.py banco-preguntas-bloque1.json

Genera:
    - Archivo ZIP con estructura QTI estándar
    - Compatible con importación directa en Canvas
"""

import json
import xml.etree.ElementTree as ET
from xml.dom import minidom
import zipfile
import os
import sys
from datetime import datetime
import uuid

class CanvasQTIGenerator:
    def __init__(self):
        self.namespace = {
            'xmlns': 'http://www.imsglobal.org/xsd/ims_qtiasiv1p2',
            'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance',
            'xsi:schemaLocation': 'http://www.imsglobal.org/xsd/ims_qtiasiv1p2 http://www.imsglobal.org/xsd/ims_qtiasiv1p2p1.xsd'
        }
        
    def generate_question_id(self, question_id):
        """Genera ID único para pregunta compatible con Canvas"""
        return f"QUE_{question_id}_{uuid.uuid4().hex[:8]}"
    
    def create_multiple_choice_question(self, question_data):
        """Crea pregunta de opción múltiple en formato QTI"""
        q_id = self.generate_question_id(question_data['id'])
        
        # Elemento principal de la pregunta
        item = ET.Element('item', {
            'ident': q_id,
            'title': f"Pregunta {question_data['id']}"
        })
        
        # Metadata
        itemmetadata = ET.SubElement(item, 'itemmetadata')
        qtimetadata = ET.SubElement(itemmetadata, 'qtimetadata')
        
        # Tipo de pregunta Canvas
        qtimetadatafield = ET.SubElement(qtimetadata, 'qtimetadatafield')
        ET.SubElement(qtimetadatafield, 'fieldlabel').text = 'question_type'
        ET.SubElement(qtimetadatafield, 'fieldentry').text = 'multiple_choice_question'
        
        # Categoría
        qtimetadatafield2 = ET.SubElement(qtimetadata, 'qtimetadatafield')
        ET.SubElement(qtimetadatafield2, 'fieldlabel').text = 'category'
        ET.SubElement(qtimetadatafield2, 'fieldentry').text = question_data.get('topic', 'General')
        
        # Presentación
        presentation = ET.SubElement(item, 'presentation')
        material = ET.SubElement(presentation, 'material')
        mattext = ET.SubElement(material, 'mattext', {'texttype': 'text/html'})
        mattext.text = f"<p>{question_data['question']}</p>"
        
        # Respuestas
        response_lid = ET.SubElement(presentation, 'response_lid', {
            'ident': f'response_{q_id}',
            'rcardinality': 'Single'
        })
        
        render_choice = ET.SubElement(response_lid, 'render_choice')
        
        for option in question_data['options']:
            response_label = ET.SubElement(render_choice, 'response_label', {
                'ident': option['id']
            })
            material_opt = ET.SubElement(response_label, 'material')
            mattext_opt = ET.SubElement(material_opt, 'mattext', {'texttype': 'text/html'})
            mattext_opt.text = f"<p>{option['text']}</p>"
        
        # Procesamiento de respuestas
        resprocessing = ET.SubElement(item, 'resprocessing')
        outcomes = ET.SubElement(resprocessing, 'outcomes')
        decvar = ET.SubElement(outcomes, 'decvar', {
            'maxvalue': '100',
            'minvalue': '0',
            'varname': 'SCORE',
            'vartype': 'Decimal'
        })
        
        # Respuesta correcta
        respcondition = ET.SubElement(resprocessing, 'respcondition', {'continue': 'No'})
        conditionvar = ET.SubElement(respcondition, 'conditionvar')
        varequal = ET.SubElement(conditionvar, 'varequal', {'respident': f'response_{q_id}'})
        varequal.text = question_data['correct_answer']
        
        setvar = ET.SubElement(respcondition, 'setvar', {
            'action': 'Set',
            'varname': 'SCORE'
        })
        setvar.text = '100'
        
        # Respuesta incorrecta (por defecto)
        respcondition_wrong = ET.SubElement(resprocessing, 'respcondition', {'continue': 'Yes'})
        conditionvar_wrong = ET.SubElement(respcondition_wrong, 'conditionvar')
        ET.SubElement(conditionvar_wrong, 'other')
        setvar_wrong = ET.SubElement(respcondition_wrong, 'setvar', {
            'action': 'Set',
            'varname': 'SCORE'
        })
        setvar_wrong.text = '0'
        
        return item
    
    def create_numeric_question(self, question_data):
        """Crea pregunta numérica en formato QTI"""
        q_id = self.generate_question_id(question_data['id'])
        
        item = ET.Element('item', {
            'ident': q_id,
            'title': f"Pregunta {question_data['id']}"
        })
        
        # Metadata
        itemmetadata = ET.SubElement(item, 'itemmetadata')
        qtimetadata = ET.SubElement(itemmetadata, 'qtimetadata')
        
        qtimetadatafield = ET.SubElement(qtimetadata, 'qtimetadatafield')
        ET.SubElement(qtimetadatafield, 'fieldlabel').text = 'question_type'
        ET.SubElement(qtimetadatafield, 'fieldentry').text = 'numerical_question'
        
        # Presentación
        presentation = ET.SubElement(item, 'presentation')
        material = ET.SubElement(presentation, 'material')
        mattext = ET.SubElement(material, 'mattext', {'texttype': 'text/html'})
        mattext.text = f"<p>{question_data['question']}</p>"
        
        # Respuesta numérica
        response_num = ET.SubElement(presentation, 'response_num', {
            'ident': f'response_{q_id}',
            'rcardinality': 'Single'
        })
        
        render_fib = ET.SubElement(response_num, 'render_fib')
        response_label = ET.SubElement(render_fib, 'response_label', {
            'ident': f'answer_{q_id}'
        })
        
        # Procesamiento
        resprocessing = ET.SubElement(item, 'resprocessing')
        outcomes = ET.SubElement(resprocessing, 'outcomes')
        decvar = ET.SubElement(outcomes, 'decvar', {
            'maxvalue': '100',
            'minvalue': '0',
            'varname': 'SCORE',
            'vartype': 'Decimal'
        })
        
        # Respuesta correcta con tolerancia
        respcondition = ET.SubElement(resprocessing, 'respcondition', {'continue': 'No'})
        conditionvar = ET.SubElement(respcondition, 'conditionvar')
        
        correct_value = question_data['correct_answer']
        tolerance = question_data.get('tolerance', 0)
        
        if tolerance > 0:
            # Rango de tolerancia
            vargte = ET.SubElement(conditionvar, 'vargte', {'respident': f'response_{q_id}'})
            vargte.text = str(correct_value - tolerance)
            
            varlte = ET.SubElement(conditionvar, 'varlte', {'respident': f'response_{q_id}'})
            varlte.text = str(correct_value + tolerance)
        else:
            # Valor exacto
            varequal = ET.SubElement(conditionvar, 'varequal', {'respident': f'response_{q_id}'})
            varequal.text = str(correct_value)
        
        setvar = ET.SubElement(respcondition, 'setvar', {
            'action': 'Set',
            'varname': 'SCORE'
        })
        setvar.text = '100'
        
        return item
    
    def create_assessment(self, questions_data):
        """Crea assessment principal QTI con todas las preguntas"""
        assessment_id = f"assessment_{uuid.uuid4().hex[:8]}"
        
        questestinterop = ET.Element('questestinterop', self.namespace)
        
        assessment = ET.SubElement(questestinterop, 'assessment', {
            'ident': assessment_id,
            'title': questions_data['metadata']['title']
        })
        
        # Metadata del assessment
        assessmentmetadata = ET.SubElement(assessment, 'assessmentmetadata')
        qtimetadata = ET.SubElement(assessmentmetadata, 'qtimetadata')
        
        # Configuración Canvas
        fields = [
            ('cc_maxattempts', '3'),
            ('cc_timelimit', '60'),
            ('cc_showfeedback', 'true'),
            ('cc_showresults', 'true'),
            ('points_possible', str(questions_data['metadata']['suggested_exam_questions']))
        ]
        
        for label, entry in fields:
            field = ET.SubElement(qtimetadata, 'qtimetadatafield')
            ET.SubElement(field, 'fieldlabel').text = label
            ET.SubElement(field, 'fieldentry').text = entry
        
        # Sección de preguntas
        section = ET.SubElement(assessment, 'section', {
            'ident': f'section_{uuid.uuid4().hex[:8]}',
            'title': 'Preguntas'
        })
        
        # Agregar preguntas
        for question in questions_data['questions']:
            if question['type'] == 'multiple_choice':
                item = self.create_multiple_choice_question(question)
            elif question['type'] == 'numeric':
                item = self.create_numeric_question(question)
            else:
                continue
                
            section.append(item)
        
        return questestinterop
    
    def create_manifest(self, assessment_filename):
        """Crea manifest IMS para el paquete QTI"""
        manifest = ET.Element('manifest', {
            'identifier': f'manifest_{uuid.uuid4().hex[:8]}',
            'version': '1.1',
            'xmlns': 'http://www.imsglobal.org/xsd/imscp_v1p1',
            'xmlns:lom': 'http://ltsc.ieee.org/xsd/LOM',
            'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance',
            'xsi:schemaLocation': 'http://www.imsglobal.org/xsd/imscp_v1p1 http://www.imsglobal.org/xsd/imscp_v1p1.xsd'
        })
        
        metadata = ET.SubElement(manifest, 'metadata')
        schema = ET.SubElement(metadata, 'schema')
        schema.text = 'IMS Content'
        schemaversion = ET.SubElement(metadata, 'schemaversion')
        schemaversion.text = '1.1'
        
        organizations = ET.SubElement(manifest, 'organizations')
        
        resources = ET.SubElement(manifest, 'resources')
        resource = ET.SubElement(resources, 'resource', {
            'identifier': f'resource_{uuid.uuid4().hex[:8]}',
            'type': 'imsqti_xmlv1p2',
            'href': assessment_filename
        })
        
        file_elem = ET.SubElement(resource, 'file', {'href': assessment_filename})
        
        return manifest
    
    def prettify_xml(self, elem):
        """Formatea XML de manera legible"""
        rough_string = ET.tostring(elem, 'unicode')
        reparsed = minidom.parseString(rough_string)
        return reparsed.toprettyxml(indent="  ")[23:]  # Remover línea XML declaration duplicada
    
    def generate_qti_package(self, json_file, output_zip=None):
        """Genera paquete QTI completo desde archivo JSON"""
        if not os.path.exists(json_file):
            raise FileNotFoundError(f"Archivo no encontrado: {json_file}")
        
        # Cargar datos
        with open(json_file, 'r', encoding='utf-8') as f:
            questions_data = json.load(f)
        
        # Generar nombres de archivo
        base_name = os.path.splitext(os.path.basename(json_file))[0]
        assessment_filename = f"{base_name}_assessment.xml"
        
        if output_zip is None:
            output_zip = f"{base_name}_QTI_CANVAS.zip"
        
        # Crear assessment QTI
        assessment_xml = self.create_assessment(questions_data)
        
        # Crear manifest
        manifest_xml = self.create_manifest(assessment_filename)
        
        # Crear ZIP
        with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zf:
            # Escribir manifest
            manifest_content = self.prettify_xml(manifest_xml)
            zf.writestr('imsmanifest.xml', manifest_content)
            
            # Escribir assessment
            assessment_content = self.prettify_xml(assessment_xml)
            zf.writestr(assessment_filename, assessment_content)
        
        return output_zip, len(questions_data['questions'])


def main():
    if len(sys.argv) != 2:
        print("Uso: python generate_qti_canvas.py <archivo_json>")
        print("Ejemplo: python generate_qti_canvas.py banco-preguntas-bloque1.json")
        sys.exit(1)
    
    json_file = sys.argv[1]
    
    try:
        generator = CanvasQTIGenerator()
        output_file, question_count = generator.generate_qti_package(json_file)
        
        print(f"✓ Paquete QTI generado: {output_file}")
        print(f"✓ Preguntas procesadas: {question_count}")
        print(f"✓ Listo para importar en Canvas LMS")
        print(f"\nInstrucciones:")
        print(f"1. Ve a tu curso en Canvas")
        print(f"2. Configuración → Importar contenido del curso")
        print(f"3. Selecciona 'Paquete QTI' como tipo de contenido")
        print(f"4. Sube el archivo: {output_file}")
        print(f"5. Las preguntas aparecerán en tu banco de preguntas")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
