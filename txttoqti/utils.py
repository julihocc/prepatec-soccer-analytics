"""
Utility functions for txt-to-qti library

Common utility functions used throughout the library.
"""

import os
import re
from pathlib import Path
from .exceptions import FileError


def clean_text(text):
    """
    Clean text for CSV/QTI output by removing problematic characters.
    
    Args:
        text (str): Raw text to clean
        
    Returns:
        str: Cleaned text safe for CSV and QTI formats
    """
    if not text:
        return ""
    
    # Convert to string and strip whitespace
    text = str(text).strip()
    
    # Normalize whitespace (collapse multiple spaces/tabs/newlines)
    text = re.sub(r'\s+', ' ', text)
    
    return text


def validate_file(file_path):
    """
    Validate that a file exists and is readable.
    
    Args:
        file_path (str): Path to file to validate
        
    Returns:
        Path: Validated Path object
        
    Raises:
        FileError: If file doesn't exist or isn't readable
    """
    path = Path(file_path)
    
    if not path.exists():
        raise FileError(f"File not found: {file_path}", file_path)
        
    if not path.is_file():
        raise FileError(f"Path is not a file: {file_path}", file_path)
        
    try:
        with open(path, 'r', encoding='utf-8') as f:
            # Try to read first few bytes to check readability
            f.read(1)
    except (OSError, UnicodeDecodeError) as e:
        raise FileError(f"Cannot read file: {e}", file_path)
        
    return path


def get_file_timestamp(file_path):
    """
    Get the modification timestamp of a file.
    
    Args:
        file_path (str): Path to file
        
    Returns:
        float: Modification timestamp, or 0 if file doesn't exist
    """
    try:
        return os.path.getmtime(file_path)
    except OSError:
        return 0


def generate_output_filename(input_file, suffix="_canvas_qti", extension=".zip"):
    """
    Generate an output filename based on input file.
    
    Args:
        input_file (str): Input file path
        suffix (str): Suffix to add before extension
        extension (str): New file extension
        
    Returns:
        str: Generated output filename
    """
    input_path = Path(input_file)
    return str(input_path.parent / f"{input_path.stem}{suffix}{extension}")


def map_answer_to_number(answer_letter):
    """
    Map answer letter (A, B, C, D) to number (1, 2, 3, 4).
    
    Args:
        answer_letter (str): Answer letter (A, B, C, D, or E)
        
    Returns:
        str: Corresponding number as string
    """
    answer_map = {'A': '1', 'B': '2', 'C': '3', 'D': '4', 'E': '5'}
    return answer_map.get(answer_letter.upper(), '1')


def ensure_directory(file_path):
    """
    Ensure the directory for a file path exists.
    
    Args:
        file_path (str): File path whose directory should be created
    """
    directory = Path(file_path).parent
    directory.mkdir(parents=True, exist_ok=True)


def format_timestamp(timestamp):
    """
    Format timestamp for human-readable display.
    
    Args:
        timestamp (float): Unix timestamp
        
    Returns:
        str: Formatted timestamp string
    """
    if timestamp == 0:
        return "not found"
    
    import datetime
    return datetime.datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S")