"""
Text parser for txt-to-qti library

Handles parsing of plain text question files into structured data.
"""

import re
from typing import List, Dict, Any, Optional
from .exceptions import ParseError
from .utils import clean_text


class QuestionParser:
    """
    Parser for converting plain text question files into structured question data.
    
    Supports the following format:
        Q1: Question text here?
        A) Option A text
        B) Option B text  
        C) Option C text
        D) Option D text
        RESPUESTA: B
        
        Q2: Next question?
        ...
    """
    
    def __init__(self):
        self.questions = []
        self.current_line = 0
        
    def parse_file(self, file_path: str) -> List[Dict[str, Any]]:
        """
        Parse a text file containing questions.
        
        Args:
            file_path: Path to text file to parse
            
        Returns:
            List of question dictionaries
            
        Raises:
            ParseError: If parsing fails
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except (OSError, UnicodeDecodeError) as e:
            raise ParseError(f"Cannot read file: {e}")
            
        return self.parse_text(content)
        
    def parse_text(self, text: str) -> List[Dict[str, Any]]:
        """
        Parse text content containing questions.
        
        Args:
            text: Raw text content to parse
            
        Returns:
            List of question dictionaries
        """
        self.questions = []
        self.current_line = 0
        
        lines = text.split('\n')
        current_question = None
        
        for line_num, line in enumerate(lines, 1):
            self.current_line = line_num
            line = line.strip()
            
            if not line:
                # Empty line - may indicate end of question
                if current_question and current_question.get('correct_answer'):
                    self._save_question(current_question)
                    current_question = None
                continue
                
            # Detect question start (Q1:, Q2:, etc.)
            question_match = re.match(r'^Q(\d+):\s*(.*)', line)
            if question_match:
                # Save previous question if exists
                if current_question:
                    self._save_question(current_question)
                    
                # Start new question
                question_num = int(question_match.group(1))
                question_text = question_match.group(2).strip()
                
                current_question = {
                    'number': question_num,
                    'text': clean_text(question_text),
                    'options': [],
                    'correct_answer': None,
                    'line_number': line_num
                }
                continue
                
            # Detect options (A), B), C), D))
            option_match = re.match(r'^([ABCDE])\)\s*(.*)', line)
            if option_match and current_question:
                option_text = option_match.group(2).strip()
                current_question['options'].append(clean_text(option_text))
                continue
                
            # Detect answer (RESPUESTA: B)
            answer_match = re.match(r'^RESPUESTA:\s*([ABCDE])', line)
            if answer_match and current_question:
                current_question['correct_answer'] = answer_match.group(1)
                continue
                
        # Save last question if exists
        if current_question:
            self._save_question(current_question)
            
        return self.questions
        
    def _save_question(self, question: Dict[str, Any]):
        """
        Validate and save a parsed question.
        
        Args:
            question: Question dictionary to validate and save
            
        Raises:
            ParseError: If question validation fails
        """
        question_num = question['number']
        line_num = question.get('line_number', 0)
        
        # Check for correct answer
        if not question['correct_answer']:
            raise ParseError(
                f"Question {question_num} missing correct answer (RESPUESTA: X)",
                line_num,
                question_num
            )
            
        # Check for minimum options
        if len(question['options']) < 2:
            raise ParseError(
                f"Question {question_num} needs at least 2 options",
                line_num, 
                question_num
            )
            
        # Ensure exactly 4 options (pad with empty strings if needed)
        while len(question['options']) < 4:
            question['options'].append("")
            
        # Limit to 4 options maximum
        question['options'] = question['options'][:4]
        
        # Validate correct answer is within available options
        correct_index = ord(question['correct_answer']) - ord('A')
        if correct_index >= len([opt for opt in question['options'] if opt.strip()]):
            raise ParseError(
                f"Question {question_num} correct answer '{question['correct_answer']}' "
                f"refers to non-existent option",
                line_num,
                question_num
            )
            
        self.questions.append(question)
        
    def get_parsing_stats(self) -> Dict[str, Any]:
        """
        Get statistics about the parsing process.
        
        Returns:
            Dictionary with parsing statistics
        """
        if not self.questions:
            return {
                'total_questions': 0,
                'questions_with_issues': 0,
                'average_options': 0,
                'answer_distribution': {}
            }
            
        # Calculate statistics
        total = len(self.questions)
        options_counts = [len([opt for opt in q['options'] if opt.strip()]) 
                         for q in self.questions]
        avg_options = sum(options_counts) / total if total > 0 else 0
        
        # Answer distribution
        answer_dist = {}
        for q in self.questions:
            answer = q['correct_answer']
            answer_dist[answer] = answer_dist.get(answer, 0) + 1
            
        return {
            'total_questions': total,
            'average_options': round(avg_options, 1),
            'answer_distribution': answer_dist,
            'min_options': min(options_counts) if options_counts else 0,
            'max_options': max(options_counts) if options_counts else 0
        }