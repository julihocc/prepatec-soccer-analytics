"""
Utility functions for QTI conversion operations.
"""

import os
import hashlib
import re
from pathlib import Path
from typing import Tuple


class FileManager:
    """Handles file operations and change detection for QTI conversion."""
    
    @staticmethod
    def count_questions(filepath: str) -> int:
        """Cuenta preguntas en el archivo"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            questions = re.findall(r'^Q\d+:', content, re.MULTILINE)
            return len(questions)
        except Exception:
            return 0
    
    @staticmethod
    def file_changed(filepath: str, checksum_file: str = None) -> bool:
        """Verifica si un archivo ha cambiado usando checksums MD5"""
        if checksum_file is None:
            checksum_file = filepath + ".checksum"
        
        if not os.path.exists(filepath):
            return True
        
        with open(filepath, 'rb') as f:
            current_checksum = hashlib.md5(f.read()).hexdigest()
        
        if os.path.exists(checksum_file):
            with open(checksum_file, 'r') as f:
                previous_checksum = f.read().strip()
            
            if current_checksum == previous_checksum:
                return False
        
        with open(checksum_file, 'w') as f:
            f.write(current_checksum)
        
        return True


class BlockDetector:
    """Auto-detects block information from directory structure."""
    
    @staticmethod
    def detect_block_info(script_path: Path = None) -> Tuple[str, str, str]:
        """
        Auto-detecta información del bloque basado en la ubicación del directorio.
        
        Returns:
            tuple: (block_number, txt_file, qti_file)
        """
        if script_path is None:
            script_path = Path.cwd()
        else:
            script_path = Path(script_path).parent
        
        # Extraer número de bloque del path: evaluaciones/bloque-X/canvas/
        path_str = str(script_path)
        block_match = re.search(r'bloque-(\d+)', path_str)
        
        if not block_match:
            # Fallback: try to detect from any .txt file in directory
            txt_files = list(script_path.glob("banco-preguntas-bloque*.txt"))
            if txt_files:
                filename = txt_files[0].name
                block_match = re.search(r'bloque(\d+)', filename)
        
        if not block_match:
            raise ValueError(f"No se puede detectar el número de bloque desde: {script_path}")
        
        block_num = block_match.group(1)
        txt_file = f"banco-preguntas-bloque{block_num}.txt"
        qti_file = f"banco-preguntas-bloque{block_num}_canvas_qti.zip"
        
        return block_num, txt_file, qti_file
    
    @staticmethod
    def get_block_description(block_num: str) -> str:
        """Retorna descripción del bloque para logging"""
        descriptions = {
            "1": "Python fundamentals",
            "2": "Data exploration with football data", 
            "3": "Predictive modeling and machine learning"
        }
        return descriptions.get(block_num, f"Bloque {block_num}")