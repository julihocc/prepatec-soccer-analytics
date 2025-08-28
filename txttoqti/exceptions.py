"""
Exception classes for txt-to-qti library

This module defines all custom exceptions used throughout the library.
"""


class TxtToQtiError(Exception):
    """Base exception class for all txt-to-qti related errors."""
    pass


class ParseError(TxtToQtiError):
    """Raised when text parsing fails."""
    
    def __init__(self, message, line_number=None, question_number=None):
        super().__init__(message)
        self.line_number = line_number
        self.question_number = question_number
        
    def __str__(self):
        msg = super().__str__()
        if self.question_number:
            msg = f"Question {self.question_number}: {msg}"
        if self.line_number:
            msg = f"Line {self.line_number}: {msg}"
        return msg


class ValidationError(TxtToQtiError):
    """Raised when question validation fails."""
    
    def __init__(self, message, question_number=None, field=None):
        super().__init__(message)
        self.question_number = question_number
        self.field = field
        
    def __str__(self):
        msg = super().__str__()
        if self.question_number:
            msg = f"Question {self.question_number}: {msg}"
        if self.field:
            msg = f"{self.field} - {msg}"
        return msg


class ConversionError(TxtToQtiError):
    """Raised when QTI conversion fails."""
    
    def __init__(self, message, stage=None):
        super().__init__(message)
        self.stage = stage
        
    def __str__(self):
        msg = super().__str__()
        if self.stage:
            msg = f"{self.stage}: {msg}"
        return msg


class FileError(TxtToQtiError):
    """Raised when file operations fail."""
    
    def __init__(self, message, file_path=None):
        super().__init__(message)
        self.file_path = file_path
        
    def __str__(self):
        msg = super().__str__()
        if self.file_path:
            msg = f"{self.file_path}: {msg}"
        return msg