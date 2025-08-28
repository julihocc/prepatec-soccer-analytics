"""
Main converter class for txt-to-qti library

Orchestrates the complete conversion process from text files to QTI packages.
"""

from typing import Dict, Any, Optional, Tuple, List
from pathlib import Path

from .parser import QuestionParser
from .validator import QuestionValidator
from .qti_generator import QTIGenerator
from .exceptions import TxtToQtiError, ConversionError
from .utils import validate_file, generate_output_filename


class TxtToQtiConverter:
    """
    Main converter class that orchestrates the complete conversion process.
    
    Converts plain text question files to QTI packages compatible with Canvas LMS.
    """
    
    def __init__(self, validate_questions: bool = True):
        """
        Initialize converter.
        
        Args:
            validate_questions: Whether to validate questions during conversion
        """
        self.validate_questions = validate_questions
        self.parser = QuestionParser()
        self.validator = QuestionValidator()
        self.qti_generator = QTIGenerator()
        
        # Conversion state
        self.last_questions = []
        self.last_validation_results = {}
        
    def convert_file(self, input_file: str, output_file: str = None, 
                    **kwargs) -> str:
        """
        Convert a text file to QTI package.
        
        Args:
            input_file: Path to input text file
            output_file: Path for output QTI ZIP file (optional)
            **kwargs: Additional options (base_name, etc.)
            
        Returns:
            Path to created QTI ZIP file
            
        Raises:
            TxtToQtiError: If conversion fails
        """
        # Validate input file
        input_path = validate_file(input_file)
        
        # Generate output filename if not provided
        if output_file is None:
            base_name = kwargs.get('base_name', input_path.stem)
            output_file = generate_output_filename(input_file, "_canvas_qti", ".zip")
        
        # Parse questions
        try:
            questions = self.parser.parse_file(str(input_path))
            self.last_questions = questions
        except Exception as e:
            raise ConversionError(f"Failed to parse questions: {e}", "Parsing")
            
        if not questions:
            raise ConversionError("No valid questions found in file", "Parsing")
            
        # Validate questions if enabled
        if self.validate_questions:
            issues = self.validator.validate_questions(questions)
            self.last_validation_results = self.validator.get_validation_summary()
            
            if self.last_validation_results['total_errors'] > 0:
                error_msg = "; ".join(self.last_validation_results['errors'][:3])
                raise ConversionError(f"Question validation failed: {error_msg}", "Validation")
                
        # Generate QTI package
        base_name = kwargs.get('base_name', input_path.stem)
        qti_file, question_count, xml_filename = self.qti_generator.generate_qti_package(
            questions, output_file, base_name
        )
        
        return qti_file
        
    def convert_text(self, text_content: str, output_file: str = None,
                    base_name: str = "questions", **kwargs) -> str:
        """
        Convert text content directly to QTI package.
        
        Args:
            text_content: Raw text content containing questions
            output_file: Path for output QTI ZIP file (optional)
            base_name: Base name for generated files
            **kwargs: Additional options
            
        Returns:
            Path to created QTI ZIP file
        """
        # Generate output filename if not provided
        if output_file is None:
            output_file = f"{base_name}_canvas_qti.zip"
            
        # Parse questions from text
        try:
            questions = self.parser.parse_text(text_content)
            self.last_questions = questions
        except Exception as e:
            raise ConversionError(f"Failed to parse questions: {e}", "Parsing")
            
        if not questions:
            raise ConversionError("No valid questions found in text", "Parsing")
            
        # Validate questions if enabled
        if self.validate_questions:
            issues = self.validator.validate_questions(questions)
            self.last_validation_results = self.validator.get_validation_summary()
            
            if self.last_validation_results['total_errors'] > 0:
                error_msg = "; ".join(self.last_validation_results['errors'][:3])
                raise ConversionError(f"Question validation failed: {error_msg}", "Validation")
                
        # Generate QTI package
        qti_file, question_count, xml_filename = self.qti_generator.generate_qti_package(
            questions, output_file, base_name
        )
        
        return qti_file
        
    def get_last_questions(self) -> List[Dict[str, Any]]:
        """
        Get the questions from the last conversion.
        
        Returns:
            List of question dictionaries from last conversion
        """
        return self.last_questions.copy()
        
    def get_last_validation_results(self) -> Dict[str, Any]:
        """
        Get validation results from the last conversion.
        
        Returns:
            Dictionary with validation results
        """
        return self.last_validation_results.copy()
        
    def get_conversion_stats(self) -> Dict[str, Any]:
        """
        Get statistics about the last conversion.
        
        Returns:
            Dictionary with conversion statistics
        """
        if not self.last_questions:
            return {'total_questions': 0}
            
        # Basic stats
        stats = {
            'total_questions': len(self.last_questions),
            'parsing_stats': self.parser.get_parsing_stats()
        }
        
        # Add validation stats if available
        if self.last_validation_results:
            stats['validation_stats'] = self.last_validation_results
            
        return stats
        
    def preview_conversion(self, input_file: str) -> Dict[str, Any]:
        """
        Preview what would happen during conversion without creating output.
        
        Args:
            input_file: Path to input text file
            
        Returns:
            Dictionary with preview information
        """
        # Validate input file
        input_path = validate_file(input_file)
        
        # Parse questions
        try:
            questions = self.parser.parse_file(str(input_path))
        except Exception as e:
            return {
                'success': False,
                'error': str(e),
                'stage': 'parsing'
            }
            
        if not questions:
            return {
                'success': False,
                'error': 'No valid questions found',
                'stage': 'parsing'
            }
            
        # Validate questions
        issues = self.validator.validate_questions(questions)
        validation_results = self.validator.get_validation_summary()
        
        # Get parsing stats
        parsing_stats = self.parser.get_parsing_stats()
        
        # Check answer distribution
        distribution_warnings = self.validator.validate_answer_distribution(questions)
        
        return {
            'success': validation_results['total_errors'] == 0,
            'total_questions': len(questions),
            'parsing_stats': parsing_stats,
            'validation_results': validation_results,
            'answer_distribution_warnings': distribution_warnings,
            'estimated_output_file': generate_output_filename(input_file, "_canvas_qti", ".zip"),
            'questions_preview': [
                {
                    'number': q['number'],
                    'text': q['text'][:100] + '...' if len(q['text']) > 100 else q['text'],
                    'options_count': len([opt for opt in q['options'] if opt.strip()]),
                    'correct_answer': q['correct_answer']
                }
                for q in questions[:5]  # First 5 questions
            ]
        }