"""
QTI generator for txt-to-qti library

Generates QTI-compliant XML packages compatible with Canvas LMS.
"""

import xml.etree.ElementTree as ET
from xml.dom import minidom
import zipfile
import hashlib
from typing import List, Dict, Any, Tuple
from pathlib import Path

from .exceptions import ConversionError
from .utils import map_answer_to_number, ensure_directory


class QTIGenerator:
    """
    Generates QTI packages from structured question data.
    
    Creates Canvas LMS-compatible QTI packages using the Kansas State format
    for maximum compatibility.
    """
    
    def __init__(self):
        # Kansas State Converter-compatible namespaces
        self.qti_namespace = 'http://www.imsglobal.org/xsd/ims_qtiasiv1p2'
        self.xsi_namespace = 'http://www.w3.org/2001/XMLSchema-instance'
        self.schema_location = (
            'http://www.imsglobal.org/xsd/ims_qtiasiv1p2 '
            'http://www.imsglobal.org/xsd/ims_qtiasiv1p2p1.xsd'
        )
        
    def generate_qti_package(self, questions: List[Dict[str, Any]], 
                           output_file: str = None,
                           base_name: str = "questions") -> Tuple[str, int, str]:
        """
        Generate a complete QTI package from questions.
        
        Args:
            questions: List of question dictionaries
            output_file: Output ZIP file path (optional)
            base_name: Base name for internal files
            
        Returns:
            Tuple of (zip_file_path, question_count, xml_filename)
            
        Raises:
            ConversionError: If QTI generation fails
        """
        if not questions:
            raise ConversionError("No questions provided for QTI generation")
            
        # Generate filenames
        if output_file is None:
            output_file = f"{base_name}_canvas_qti.zip"
            
        xml_filename = self._generate_xml_filename(base_name)
        
        try:
            # Create QTI XML
            xml_content = self._create_qti_xml(questions, base_name)
            
            # Ensure output directory exists
            ensure_directory(output_file)
            
            # Create ZIP package (Kansas State style - no manifest)
            with zipfile.ZipFile(output_file, 'w', zipfile.ZIP_DEFLATED) as zf:
                zf.writestr(xml_filename, xml_content.encode('iso-8859-1'))
                
            return output_file, len(questions), xml_filename
            
        except Exception as e:
            raise ConversionError(f"Failed to generate QTI package: {e}", "QTI Generation")
            
    def _generate_xml_filename(self, base_name: str) -> str:
        """Generate XML filename with hash like Kansas State converter."""
        hash_value = abs(hash(base_name)) % 1000000000
        return f"{base_name}_{hash_value}.xml"
        
    def _create_qti_xml(self, questions: List[Dict[str, Any]], base_name: str) -> str:
        """
        Create QTI XML content from questions.
        
        Args:
            questions: List of question dictionaries
            base_name: Base name for assessment
            
        Returns:
            Formatted XML string with Kansas State-style formatting
        """
        # Create root assessment
        assessment_xml = self._create_assessment_element(questions, base_name)
        
        # Format XML with Kansas State styling
        return self._format_xml_kansas_style(assessment_xml)
        
    def _create_assessment_element(self, questions: List[Dict[str, Any]], 
                                 base_name: str) -> ET.Element:
        """Create the main assessment XML element."""
        assessment_id = self._generate_assessment_id(base_name)
        
        # Root element
        questestinterop = ET.Element('questestinterop', {
            'xmlns': self.qti_namespace,
            'xmlns:xsi': self.xsi_namespace,
            'xsi:schemaLocation': self.schema_location
        })
        
        # Assessment element
        assessment = ET.SubElement(questestinterop, 'assessment', {
            'ident': assessment_id,
            'title': base_name
        })
        
        # Add minimal metadata like Kansas State
        qtimetadata = ET.SubElement(assessment, 'qtimetadata')
        field = ET.SubElement(qtimetadata, 'qtimetadatafield')
        ET.SubElement(field, 'fieldlabel').text = 'cc_maxattempts'
        ET.SubElement(field, 'fieldentry').text = '1'
        
        # Main section
        section = ET.SubElement(assessment, 'section', {
            'ident': 'root_section'
        })
        
        # Add all questions as items
        for question in questions:
            item = self._create_qti_item(question)
            section.append(item)
            
        return questestinterop
        
    def _create_qti_item(self, question: Dict[str, Any]) -> ET.Element:
        """Create QTI item element for a single question."""
        item_id = self._generate_item_id(question['number'])
        
        # Main item element
        item = ET.Element('item', {
            'ident': item_id,
            'title': f"Question {question['number']}"
        })
        
        # Item metadata
        self._add_item_metadata(item, question)
        
        # Question presentation
        self._add_item_presentation(item, question)
        
        # Response processing
        self._add_response_processing(item, question)
        
        return item
        
    def _add_item_metadata(self, item: ET.Element, question: Dict[str, Any]):
        """Add metadata to item element."""
        itemmetadata = ET.SubElement(item, 'itemmetadata')
        qtimetadata = ET.SubElement(itemmetadata, 'qtimetadata')
        
        # Question type
        field1 = ET.SubElement(qtimetadata, 'qtimetadatafield')
        ET.SubElement(field1, 'fieldlabel').text = 'question_type'
        ET.SubElement(field1, 'fieldentry').text = 'multiple_choice_question'
        
        # Points
        field2 = ET.SubElement(qtimetadata, 'qtimetadatafield')
        ET.SubElement(field2, 'fieldlabel').text = 'points_possible'
        ET.SubElement(field2, 'fieldentry').text = '1.0'
        
        # Reference ID (Kansas State style)
        field3 = ET.SubElement(qtimetadata, 'qtimetadatafield')
        ET.SubElement(field3, 'fieldlabel').text = 'assessment_question_identifierref'
        ref_id = self._generate_item_id(f"ref_{question['number']}")
        ET.SubElement(field3, 'fieldentry').text = ref_id
        
    def _add_item_presentation(self, item: ET.Element, question: Dict[str, Any]):
        """Add presentation section to item."""
        presentation = ET.SubElement(item, 'presentation')
        
        # Question text
        material = ET.SubElement(presentation, 'material')
        mattext = ET.SubElement(material, 'mattext', {'texttype': 'text/html'})
        mattext.text = question['text']
        
        # Answer choices
        response_lid = ET.SubElement(presentation, 'response_lid', {
            'ident': 'response1',
            'rcardinality': 'Single'
        })
        
        render_choice = ET.SubElement(response_lid, 'render_choice')
        
        # Create option elements
        for i, choice_text in enumerate(question['options']):
            if choice_text.strip():  # Only non-empty choices
                choice_id = f"{question['number']}{i:03d}"  # Format: 1000, 1001, etc.
                
                response_label = ET.SubElement(render_choice, 'response_label', {
                    'ident': choice_id
                })
                choice_material = ET.SubElement(response_label, 'material')
                choice_mattext = ET.SubElement(choice_material, 'mattext', {
                    'texttype': 'text/plain'
                })
                choice_mattext.text = choice_text.strip()
                
    def _add_response_processing(self, item: ET.Element, question: Dict[str, Any]):
        """Add response processing section to item."""
        resprocessing = ET.SubElement(item, 'resprocessing')
        
        # Outcomes
        outcomes = ET.SubElement(resprocessing, 'outcomes')
        ET.SubElement(outcomes, 'decvar', {
            'maxvalue': '100',
            'minvalue': '0',
            'varname': 'SCORE',
            'vartype': 'Decimal'
        })
        
        # Correct answer condition
        correct_index = ord(question['correct_answer']) - ord('A')
        correct_choice_id = f"{question['number']}{correct_index:03d}"
        
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
        
    def _generate_item_id(self, seed: str) -> str:
        """Generate unique item ID using MD5 hash."""
        hash_obj = hashlib.md5(str(seed).encode())
        return f"i{hash_obj.hexdigest()}"
        
    def _generate_assessment_id(self, base_name: str) -> str:
        """Generate unique assessment ID using MD5 hash."""
        hash_obj = hashlib.md5(f"assessment_{base_name}".encode())
        return f"i{hash_obj.hexdigest()}"
        
    def _format_xml_kansas_style(self, elem: ET.Element) -> str:
        """
        Format XML exactly like Kansas State converter.
        
        Uses ISO-8859-1 encoding and specific indentation.
        """
        # Convert to string first
        rough_string = ET.tostring(elem, encoding='unicode')
        reparsed = minidom.parseString(rough_string)
        
        # Get pretty XML without minidom declaration
        xml_str = reparsed.toprettyxml(indent="  ")[23:]  # Remove XML declaration
        
        # Add Kansas State-style declaration
        kansas_declaration = '<?xml version="1.0" encoding="ISO-8859-1"?>\n'
        
        return kansas_declaration + xml_str