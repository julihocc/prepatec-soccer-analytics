#!/usr/bin/env python3
"""
Core functionality tests for txttoqti library
"""

import unittest
import tempfile
import os
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

# Import the modules to test
from txttoqti import TxtToQtiConverter, QuestionParser, QTIGenerator, convert_txt_to_qti
from txttoqti.exceptions import ParseError, ConversionError


class TestQuestionParser(unittest.TestCase):
    """Test the question parser functionality."""
    
    def setUp(self):
        self.parser = QuestionParser()
        self.sample_text = """Q1: What is the capital of France?
A) London
B) Paris  
C) Berlin
D) Madrid
RESPUESTA: B

Q2: Which team won the 2018 World Cup?
A) Brazil
B) Germany
C) France
D) Argentina
RESPUESTA: C"""

    def test_parse_text_basic(self):
        """Test basic text parsing."""
        questions = self.parser.parse_text(self.sample_text)
        
        self.assertEqual(len(questions), 2)
        self.assertEqual(questions[0]['number'], 1)
        self.assertEqual(questions[0]['text'], "What is the capital of France?")
        self.assertEqual(len(questions[0]['options']), 4)
        self.assertEqual(questions[0]['correct_answer'], 'B')
        
    def test_parse_text_with_missing_answer(self):
        """Test parsing text with missing answer."""
        bad_text = """Q1: What is the capital?
A) London
B) Paris"""
        
        with self.assertRaises(ParseError):
            self.parser.parse_text(bad_text)
            
    def test_get_parsing_stats(self):
        """Test parsing statistics."""
        questions = self.parser.parse_text(self.sample_text)
        stats = self.parser.get_parsing_stats()
        
        self.assertEqual(stats['total_questions'], 2)
        self.assertEqual(stats['average_options'], 4.0)
        self.assertIn('B', stats['answer_distribution'])
        self.assertIn('C', stats['answer_distribution'])


class TestQTIGenerator(unittest.TestCase):
    """Test QTI generation functionality."""
    
    def setUp(self):
        self.generator = QTIGenerator()
        self.sample_questions = [
            {
                'number': 1,
                'text': 'What is the capital of France?',
                'options': ['London', 'Paris', 'Berlin', 'Madrid'],
                'correct_answer': 'B'
            },
            {
                'number': 2, 
                'text': 'Which team won the 2018 World Cup?',
                'options': ['Brazil', 'Germany', 'France', 'Argentina'],
                'correct_answer': 'C'
            }
        ]
        
    def test_generate_qti_package(self):
        """Test QTI package generation."""
        with tempfile.NamedTemporaryFile(suffix='.zip', delete=False) as tmp:
            qti_file, question_count, xml_filename = self.generator.generate_qti_package(
                self.sample_questions, tmp.name, 'test_questions'
            )
            
            # Verify results
            self.assertEqual(question_count, 2)
            self.assertTrue(xml_filename.endswith('.xml'))
            self.assertTrue(os.path.exists(qti_file))
            
            # Verify ZIP contents
            with zipfile.ZipFile(qti_file, 'r') as zf:
                files = zf.namelist()
                self.assertEqual(len(files), 1)
                self.assertTrue(files[0].endswith('.xml'))
                
                # Verify XML structure
                xml_content = zf.read(files[0])
                root = ET.fromstring(xml_content)
                
                # Check namespace and structure (note: XML parser includes namespace)
                self.assertTrue(root.tag.endswith('questestinterop'))
                self.assertTrue(len(root.attrib) > 0)  # Has attributes
                
                # Check items
                items = root.findall('.//{http://www.imsglobal.org/xsd/ims_qtiasiv1p2}item')
                self.assertEqual(len(items), 2)
                
            # Cleanup
            os.unlink(qti_file)
            
    def test_empty_questions_error(self):
        """Test error handling for empty questions."""
        with self.assertRaises(ConversionError):
            self.generator.generate_qti_package([], 'test.zip', 'test')


class TestTxtToQtiConverter(unittest.TestCase):
    """Test the main converter functionality."""
    
    def setUp(self):
        self.converter = TxtToQtiConverter()
        self.sample_text = """Q1: What is the capital of France?
A) London
B) Paris  
C) Berlin
D) Madrid
RESPUESTA: B"""
        
    def test_convert_text(self):
        """Test text conversion."""
        with tempfile.NamedTemporaryFile(suffix='.zip', delete=False) as tmp:
            result = self.converter.convert_text(self.sample_text, tmp.name)
            
            self.assertEqual(result, tmp.name)
            self.assertTrue(os.path.exists(result))
            self.assertGreater(os.path.getsize(result), 0)
            
            # Verify it's a valid ZIP
            with zipfile.ZipFile(result, 'r') as zf:
                files = zf.namelist()
                self.assertEqual(len(files), 1)
                
            # Cleanup
            os.unlink(result)
            
    def test_convert_file(self):
        """Test file conversion."""
        # Create temporary input file
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False, encoding='utf-8') as tmp_input:
            tmp_input.write(self.sample_text)
            tmp_input.flush()
            
            with tempfile.NamedTemporaryFile(suffix='.zip', delete=False) as tmp_output:
                result = self.converter.convert_file(tmp_input.name, tmp_output.name)
                
                self.assertEqual(result, tmp_output.name)
                self.assertTrue(os.path.exists(result))
                
                # Cleanup
                os.unlink(tmp_input.name)
                os.unlink(result)


class TestConvenienceFunction(unittest.TestCase):
    """Test the module-level convenience function."""
    
    def test_convert_txt_to_qti(self):
        """Test the convenience function."""
        sample_text = """Q1: Test question?
A) Option A
B) Option B  
C) Option C
D) Option D
RESPUESTA: A"""
        
        # Create temporary input file
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False, encoding='utf-8') as tmp:
            tmp.write(sample_text)
            tmp.flush()
            
            # Convert using convenience function
            result = convert_txt_to_qti(tmp.name)
            
            self.assertTrue(os.path.exists(result))
            self.assertTrue(result.endswith('_canvas_qti.zip'))
            
            # Cleanup
            os.unlink(tmp.name)
            os.unlink(result)


class TestIntegrationWithRealData(unittest.TestCase):
    """Integration tests with real question files."""
    
    def test_real_question_file(self):
        """Test with actual question bank file."""
        # Use the real question bank file if it exists
        question_file = 'evaluaciones/bloque-1/canvas/banco-preguntas-bloque1.txt'
        
        if os.path.exists(question_file):
            converter = TxtToQtiConverter()
            
            with tempfile.NamedTemporaryFile(suffix='.zip', delete=False) as tmp:
                result = converter.convert_file(question_file, tmp.name)
                
                # Verify the conversion worked
                self.assertTrue(os.path.exists(result))
                self.assertGreater(os.path.getsize(result), 1000)  # Should be substantial
                
                # Check that it contains the expected number of questions
                questions = converter.get_last_questions()
                self.assertGreater(len(questions), 10)  # Should have many questions
                
                # Cleanup
                os.unlink(result)
        else:
            self.skipTest(f"Real question file not found: {question_file}")


if __name__ == '__main__':
    # Run the tests
    unittest.main(verbosity=2)