"""
Smart converter for txt-to-qti library

Provides intelligent conversion with change detection and timestamp checking.
"""

import os
from typing import Dict, Any, Optional, Tuple
from pathlib import Path

from .converter import TxtToQtiConverter
from .exceptions import TxtToQtiError
from .utils import get_file_timestamp, format_timestamp, validate_file


class SmartConverter:
    """
    Smart converter that only regenerates files when necessary.
    
    Provides timestamp-based change detection to avoid unnecessary regeneration
    and detailed status reporting.
    """
    
    def __init__(self, **converter_kwargs):
        """
        Initialize smart converter.
        
        Args:
            **converter_kwargs: Arguments passed to TxtToQtiConverter
        """
        self.converter = TxtToQtiConverter(**converter_kwargs)
        
    def convert_with_intelligence(self, input_file: str, output_file: str = None,
                                force: bool = False, status_only: bool = False,
                                **kwargs) -> Tuple[str, int, bool]:
        """
        Convert file with intelligent change detection.
        
        Args:
            input_file: Path to input text file
            output_file: Path for output QTI ZIP file (optional)
            force: Force regeneration even if files are up to date
            status_only: Only show status without converting
            **kwargs: Additional conversion options
            
        Returns:
            Tuple of (qti_file_path, question_count, was_regenerated)
        """
        # Validate input file
        input_path = validate_file(input_file)
        
        # Determine output file path
        if output_file is None:
            output_file = self._generate_output_filename(input_file)
            
        # Check if regeneration is needed
        needs_regen = self._needs_regeneration(str(input_path), output_file)
        
        if status_only:
            return output_file, self._count_existing_questions(output_file), False
            
        if not needs_regen and not force:
            # Files are up to date
            question_count = self._count_existing_questions(output_file)
            return output_file, question_count, False
            
        # Perform conversion
        qti_file = self.converter.convert_file(str(input_path), output_file, **kwargs)
        question_count = len(self.converter.get_last_questions())
        
        return qti_file, question_count, True
        
    def get_file_status(self, input_file: str, output_file: str = None) -> Dict[str, Any]:
        """
        Get detailed status of input and output files.
        
        Args:
            input_file: Path to input text file
            output_file: Path to output QTI file (optional)
            
        Returns:
            Dictionary with file status information
        """
        input_path = Path(input_file)
        
        if output_file is None:
            output_file = self._generate_output_filename(input_file)
            
        output_path = Path(output_file)
        
        # Get timestamps
        input_time = get_file_timestamp(str(input_path))
        output_time = get_file_timestamp(str(output_path))
        
        # Determine status
        input_exists = input_path.exists()
        output_exists = output_path.exists()
        needs_regen = self._needs_regeneration(str(input_path), str(output_path))
        
        return {
            'input_file': {
                'path': str(input_path),
                'name': input_path.name,
                'exists': input_exists,
                'timestamp': input_time,
                'formatted_time': format_timestamp(input_time),
                'size': input_path.stat().st_size if input_exists else 0
            },
            'output_file': {
                'path': str(output_path),
                'name': output_path.name,
                'exists': output_exists,
                'timestamp': output_time,
                'formatted_time': format_timestamp(output_time),
                'size': output_path.stat().st_size if output_exists else 0
            },
            'needs_regeneration': needs_regen,
            'is_up_to_date': not needs_regen,
            'age_difference_seconds': input_time - output_time if input_time and output_time else 0
        }
        
    def batch_convert(self, input_files: list, force: bool = False, 
                     **kwargs) -> Dict[str, Any]:
        """
        Convert multiple files with smart detection.
        
        Args:
            input_files: List of input file paths
            force: Force regeneration for all files
            **kwargs: Additional conversion options
            
        Returns:
            Dictionary with batch conversion results
        """
        results = {
            'total_files': len(input_files),
            'converted': 0,
            'skipped': 0,
            'failed': 0,
            'details': []
        }
        
        for input_file in input_files:
            try:
                qti_file, question_count, was_regenerated = self.convert_with_intelligence(
                    input_file, force=force, **kwargs
                )
                
                if was_regenerated:
                    results['converted'] += 1
                    status = 'converted'
                else:
                    results['skipped'] += 1
                    status = 'up_to_date'
                    
                results['details'].append({
                    'input_file': input_file,
                    'output_file': qti_file,
                    'question_count': question_count,
                    'status': status,
                    'error': None
                })
                
            except Exception as e:
                results['failed'] += 1
                results['details'].append({
                    'input_file': input_file,
                    'output_file': None,
                    'question_count': 0,
                    'status': 'failed',
                    'error': str(e)
                })
                
        return results
        
    def _needs_regeneration(self, input_file: str, output_file: str) -> bool:
        """
        Check if output file needs regeneration based on timestamps.
        
        Args:
            input_file: Path to input file
            output_file: Path to output file
            
        Returns:
            True if regeneration is needed
        """
        # Check if input file exists
        if not os.path.exists(input_file):
            return False
            
        # If output doesn't exist, need to generate
        if not os.path.exists(output_file):
            return True
            
        # Compare timestamps
        input_time = get_file_timestamp(input_file)
        output_time = get_file_timestamp(output_file)
        
        # If input is newer than output, need to regenerate
        return input_time > output_time
        
    def _generate_output_filename(self, input_file: str) -> str:
        """Generate output filename based on input."""
        input_path = Path(input_file)
        return str(input_path.parent / f"{input_path.stem}_canvas_qti.zip")
        
    def _count_existing_questions(self, qti_file: str) -> int:
        """
        Try to count questions in existing QTI file.
        
        Args:
            qti_file: Path to QTI ZIP file
            
        Returns:
            Number of questions, or 0 if cannot determine
        """
        if not os.path.exists(qti_file):
            return 0
            
        try:
            import zipfile
            import xml.etree.ElementTree as ET
            
            with zipfile.ZipFile(qti_file, 'r') as zf:
                # Find the XML file
                xml_files = [name for name in zf.namelist() if name.endswith('.xml')]
                if not xml_files:
                    return 0
                    
                # Parse XML and count items
                with zf.open(xml_files[0]) as xml_file:
                    tree = ET.parse(xml_file)
                    root = tree.getroot()
                    
                    # Count item elements
                    items = root.findall('.//{http://www.imsglobal.org/xsd/ims_qtiasiv1p2}item')
                    return len(items)
                    
        except Exception:
            # If we can't parse the file, assume 0 questions
            return 0
            
    def preview_batch_conversion(self, input_files: list) -> Dict[str, Any]:
        """
        Preview what would happen in batch conversion.
        
        Args:
            input_files: List of input file paths
            
        Returns:
            Dictionary with batch preview information
        """
        results = {
            'total_files': len(input_files),
            'would_convert': 0,
            'would_skip': 0,
            'invalid_files': 0,
            'details': []
        }
        
        for input_file in input_files:
            try:
                # Check if file is valid
                validate_file(input_file)
                
                # Check if needs regeneration
                output_file = self._generate_output_filename(input_file)
                needs_regen = self._needs_regeneration(input_file, output_file)
                
                if needs_regen:
                    results['would_convert'] += 1
                    status = 'would_convert'
                else:
                    results['would_skip'] += 1
                    status = 'up_to_date'
                    
                # Get file status
                file_status = self.get_file_status(input_file, output_file)
                
                results['details'].append({
                    'input_file': input_file,
                    'output_file': output_file,
                    'status': status,
                    'file_status': file_status,
                    'error': None
                })
                
            except Exception as e:
                results['invalid_files'] += 1
                results['details'].append({
                    'input_file': input_file,
                    'output_file': None,
                    'status': 'invalid',
                    'file_status': None,
                    'error': str(e)
                })
                
        return results