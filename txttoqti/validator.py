"""
Question validator for txt-to-qti library

Validates question data structure and content for QTI compatibility.
"""

from typing import List, Dict, Any, Optional
from .exceptions import ValidationError


class QuestionValidator:
    """
    Validates question data for QTI compatibility and quality.
    """
    
    def __init__(self):
        self.warnings = []
        self.errors = []
        
    def validate_questions(self, questions: List[Dict[str, Any]]) -> List[str]:
        """
        Validate a list of questions and return any issues found.
        
        Args:
            questions: List of question dictionaries to validate
            
        Returns:
            List of validation issue messages
        """
        self.warnings = []
        self.errors = []
        
        if not questions:
            self.errors.append("No questions found")
            return self.errors + self.warnings
            
        for i, question in enumerate(questions):
            self._validate_single_question(question, i + 1)
            
        return self.errors + self.warnings
        
    def _validate_single_question(self, question: Dict[str, Any], expected_num: int):
        """
        Validate a single question.
        
        Args:
            question: Question dictionary to validate
            expected_num: Expected question number for sequence validation
        """
        q_num = question.get('number', expected_num)
        
        # Check question structure
        required_fields = ['number', 'text', 'options', 'correct_answer']
        for field in required_fields:
            if field not in question:
                self.errors.append(f"Question {q_num}: Missing required field '{field}'")
                return
                
        # Check question numbering
        if question['number'] != expected_num:
            self.warnings.append(
                f"Question {q_num}: Non-sequential numbering "
                f"(expected {expected_num})"
            )
            
        # Check question text
        if not question['text'].strip():
            self.errors.append(f"Question {q_num}: Empty question text")
            
        # Check options
        options = question['options']
        if not isinstance(options, list):
            self.errors.append(f"Question {q_num}: Options must be a list")
            return
            
        # Count non-empty options
        non_empty_options = [opt for opt in options if opt.strip()]
        if len(non_empty_options) < 2:
            self.errors.append(
                f"Question {q_num}: At least 2 non-empty options required "
                f"(found {len(non_empty_options)})"
            )
            
        # Check for too many empty options
        empty_options = len(options) - len(non_empty_options)
        if empty_options > 2:
            self.warnings.append(
                f"Question {q_num}: Too many empty options ({empty_options})"
            )
            
        # Check correct answer
        correct_answer = question['correct_answer']
        if not correct_answer:
            self.errors.append(f"Question {q_num}: No correct answer specified")
            return
            
        if correct_answer not in 'ABCDE':
            self.errors.append(
                f"Question {q_num}: Invalid correct answer '{correct_answer}' "
                f"(must be A, B, C, D, or E)"
            )
            return
            
        # Check that correct answer corresponds to non-empty option
        correct_index = ord(correct_answer) - ord('A')
        if correct_index >= len(options) or not options[correct_index].strip():
            self.errors.append(
                f"Question {q_num}: Correct answer '{correct_answer}' "
                f"corresponds to empty option"
            )
            
        # Quality checks
        self._check_question_quality(question)
        
    def _check_question_quality(self, question: Dict[str, Any]):
        """
        Check question quality and provide warnings.
        
        Args:
            question: Question dictionary to check
        """
        q_num = question['number']
        text = question['text']
        options = question['options']
        
        # Check question text length
        if len(text.strip()) < 10:
            self.warnings.append(
                f"Question {q_num}: Very short question text ({len(text)} chars)"
            )
            
        if len(text) > 500:
            self.warnings.append(
                f"Question {q_num}: Very long question text ({len(text)} chars)"
            )
            
        # Check option lengths
        for i, option in enumerate(options):
            if option.strip():
                if len(option.strip()) < 2:
                    self.warnings.append(
                        f"Question {q_num}: Very short option {chr(65+i)} ({len(option)} chars)"
                    )
                    
        # Check for duplicate options
        non_empty_options = [opt.strip().lower() for opt in options if opt.strip()]
        if len(non_empty_options) != len(set(non_empty_options)):
            self.warnings.append(
                f"Question {q_num}: Possible duplicate options detected"
            )
            
        # Check answer distribution pattern
        correct_answer = question['correct_answer']
        if hasattr(self, '_answer_counts'):
            self._answer_counts[correct_answer] = self._answer_counts.get(correct_answer, 0) + 1
        else:
            self._answer_counts = {correct_answer: 1}
            
    def get_validation_summary(self) -> Dict[str, Any]:
        """
        Get a summary of validation results.
        
        Returns:
            Dictionary with validation summary
        """
        return {
            'total_errors': len(self.errors),
            'total_warnings': len(self.warnings),
            'errors': self.errors,
            'warnings': self.warnings,
            'is_valid': len(self.errors) == 0,
            'has_warnings': len(self.warnings) > 0
        }
        
    def validate_answer_distribution(self, questions: List[Dict[str, Any]]) -> List[str]:
        """
        Check answer distribution across questions for potential bias.
        
        Args:
            questions: List of questions to analyze
            
        Returns:
            List of warnings about answer distribution
        """
        if not questions:
            return []
            
        # Count answers
        answer_counts = {}
        for q in questions:
            answer = q.get('correct_answer')
            if answer:
                answer_counts[answer] = answer_counts.get(answer, 0) + 1
                
        total = len(questions)
        warnings = []
        
        # Check for heavily skewed distribution
        for answer, count in answer_counts.items():
            percentage = (count / total) * 100
            if percentage > 60:
                warnings.append(
                    f"Answer '{answer}' is correct in {percentage:.1f}% of questions "
                    f"({count}/{total}) - consider more balanced distribution"
                )
                
        # Check for unused answers
        available_answers = set('ABCD')  # Most common set
        used_answers = set(answer_counts.keys())
        unused = available_answers - used_answers
        
        if unused and total > 4:
            unused_str = ', '.join(sorted(unused))
            warnings.append(
                f"Answers {unused_str} never used as correct answers - "
                f"consider more balanced distribution"
            )
            
        return warnings