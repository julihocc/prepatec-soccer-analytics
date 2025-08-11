#!/usr/bin/env python3
import json
import os
import xml.etree.ElementTree as ET
from xml.dom import minidom

def escape_html(text):
    """Escape HTML characters in text."""
    return (text
            .replace('&', '&amp;')
            .replace('<', '&lt;')
            .replace('>', '&gt;')
            .replace('"', '&quot;')
            .replace("'", '&#39;'))

def create_multiple_choice_qti(question_data):
    """Create QTI XML for multiple choice question."""
    
    # Root element
    root = ET.Element('assessmentItem')
    root.set('xmlns', 'http://www.imsglobal.org/xsd/imsqti_v2p1')
    root.set('xmlns:xsi', 'http://www.w3.org/2001/XMLSchema-instance')
    root.set('xsi:schemaLocation', 'http://www.imsglobal.org/xsd/imsqti_v2p1 http://www.imsglobal.org/xsd/qti/qtiv2p1/imsqti_v2p1.xsd')
    root.set('identifier', f"question_{question_data['id']}")
    root.set('title', f"Pregunta {question_data['id']}")
    root.set('adaptive', 'false')
    root.set('timeDependent', 'false')
    
    # Response declaration
    response_declaration = ET.SubElement(root, 'responseDeclaration')
    response_declaration.set('identifier', 'RESPONSE')
    response_declaration.set('cardinality', 'single')
    response_declaration.set('baseType', 'identifier')
    
    correct_response = ET.SubElement(response_declaration, 'correctResponse')
    value = ET.SubElement(correct_response, 'value')
    value.text = question_data['correct_answer']
    
    # Outcome declaration
    outcome_declaration = ET.SubElement(root, 'outcomeDeclaration')
    outcome_declaration.set('identifier', 'SCORE')
    outcome_declaration.set('cardinality', 'single')
    outcome_declaration.set('baseType', 'float')
    
    default_value = ET.SubElement(outcome_declaration, 'defaultValue')
    value = ET.SubElement(default_value, 'value')
    value.text = '0'
    
    # Item body
    item_body = ET.SubElement(root, 'itemBody')
    
    # Question text
    div = ET.SubElement(item_body, 'div')
    p = ET.SubElement(div, 'p')
    p.text = question_data['question'].replace('```python', '\n').replace('```', '').replace('\n', '\n')
    
    # Choice interaction
    choice_interaction = ET.SubElement(item_body, 'choiceInteraction')
    choice_interaction.set('responseIdentifier', 'RESPONSE')
    choice_interaction.set('shuffle', 'false')
    choice_interaction.set('maxChoices', '1')
    
    prompt = ET.SubElement(choice_interaction, 'prompt')
    prompt.text = 'Selecciona la respuesta correcta:'
    
    # Options
    for option in question_data['options']:
        simple_choice = ET.SubElement(choice_interaction, 'simpleChoice')
        simple_choice.set('identifier', option['id'])
        simple_choice.text = option['text']
    
    # Response processing
    response_processing = ET.SubElement(root, 'responseProcessing')
    response_processing.set('template', 'http://www.imsglobal.org/question/qti_v2p1/rptemplates/match_correct')
    
    return root

def create_numeric_qti(question_data):
    """Create QTI XML for numeric question."""
    
    # Root element
    root = ET.Element('assessmentItem')
    root.set('xmlns', 'http://www.imsglobal.org/xsd/imsqti_v2p1')
    root.set('xmlns:xsi', 'http://www.w3.org/2001/XMLSchema-instance')
    root.set('xsi:schemaLocation', 'http://www.imsglobal.org/xsd/imsqti_v2p1 http://www.imsglobal.org/xsd/qti/qtiv2p1/imsqti_v2p1.xsd')
    root.set('identifier', f"question_{question_data['id']}")
    root.set('title', f"Pregunta {question_data['id']}")
    root.set('adaptive', 'false')
    root.set('timeDependent', 'false')
    
    # Response declaration
    response_declaration = ET.SubElement(root, 'responseDeclaration')
    response_declaration.set('identifier', 'RESPONSE')
    response_declaration.set('cardinality', 'single')
    response_declaration.set('baseType', 'float')
    
    correct_response = ET.SubElement(response_declaration, 'correctResponse')
    value = ET.SubElement(correct_response, 'value')
    value.text = str(question_data['correct_answer'])
    
    # Outcome declaration
    outcome_declaration = ET.SubElement(root, 'outcomeDeclaration')
    outcome_declaration.set('identifier', 'SCORE')
    outcome_declaration.set('cardinality', 'single')
    outcome_declaration.set('baseType', 'float')
    
    default_value = ET.SubElement(outcome_declaration, 'defaultValue')
    value = ET.SubElement(default_value, 'value')
    value.text = '0'
    
    # Item body
    item_body = ET.SubElement(root, 'itemBody')
    
    # Question text
    div = ET.SubElement(item_body, 'div')
    p = ET.SubElement(div, 'p')
    p.text = question_data['question'].replace('```python', '\n').replace('```', '').replace('\n', '\n')
    
    # Text entry interaction
    text_entry_interaction = ET.SubElement(item_body, 'textEntryInteraction')
    text_entry_interaction.set('responseIdentifier', 'RESPONSE')
    text_entry_interaction.set('expectedLength', '10')
    
    # Response processing
    response_processing = ET.SubElement(root, 'responseProcessing')
    
    # Response condition
    response_condition = ET.SubElement(response_processing, 'responseCondition')
    response_if = ET.SubElement(response_condition, 'responseIf')
    
    # Equal condition with tolerance
    tolerance = question_data.get('tolerance', 0.1)
    if tolerance > 0:
        # Use tolerance for floating point comparison
        and_condition = ET.SubElement(response_if, 'and')
        
        gte = ET.SubElement(and_condition, 'gte')
        variable1 = ET.SubElement(gte, 'variable')
        variable1.set('identifier', 'RESPONSE')
        value1 = ET.SubElement(gte, 'baseValue')
        value1.set('baseType', 'float')
        value1.text = str(float(question_data['correct_answer']) - tolerance)
        
        lte = ET.SubElement(and_condition, 'lte')
        variable2 = ET.SubElement(lte, 'variable')
        variable2.set('identifier', 'RESPONSE')
        value2 = ET.SubElement(lte, 'baseValue')
        value2.set('baseType', 'float')
        value2.text = str(float(question_data['correct_answer']) + tolerance)
    else:
        # Exact match
        equal = ET.SubElement(response_if, 'equal')
        variable = ET.SubElement(equal, 'variable')
        variable.set('identifier', 'RESPONSE')
        value = ET.SubElement(equal, 'baseValue')
        value.set('baseType', 'float')
        value.text = str(question_data['correct_answer'])
    
    # Set score to 1 if correct
    set_outcome_value = ET.SubElement(response_if, 'setOutcomeValue')
    set_outcome_value.set('identifier', 'SCORE')
    base_value = ET.SubElement(set_outcome_value, 'baseValue')
    base_value.set('baseType', 'float')
    base_value.text = '1'
    
    return root

def prettify_xml(elem):
    """Return a pretty-printed XML string for the Element."""
    rough_string = ET.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

def generate_qti_files(json_file_path, output_dir):
    """Generate QTI XML files from JSON question bank."""
    
    # Load JSON data
    with open(json_file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Generate XML file for each question
    for question in data['questions']:
        if question['type'] == 'multiple_choice':
            qti_element = create_multiple_choice_qti(question)
        elif question['type'] == 'numeric':
            qti_element = create_numeric_qti(question)
        else:
            print(f"Unsupported question type: {question['type']}")
            continue
        
        # Write to XML file
        xml_filename = f"question_{question['id']}.xml"
        xml_path = os.path.join(output_dir, xml_filename)
        
        with open(xml_path, 'w', encoding='utf-8') as f:
            f.write(prettify_xml(qti_element))
        
        print(f"Generated: {xml_filename}")

if __name__ == "__main__":
    json_file = "/home/julihocc/topico/main.worktrees/publicar-curso-en-canvas/evaluaciones/bloque-1/canvas/banco-preguntas-bloque1.json"
    output_directory = "/home/julihocc/topico/main.worktrees/publicar-curso-en-canvas/evaluaciones/bloque-1/canvas/qti_package"
    
    generate_qti_files(json_file, output_directory)
    print("QTI files generation completed!")