"""
Core QTI conversion functionality.
Orchestrates the entire conversion process from question banks to Canvas QTI.
"""

import os
import sys
from pathlib import Path
from typing import Optional

try:
    from txttoqti import TxtToQtiConverter
except ImportError as e:
    print("❌ Error: No se puede importar la librería txttoqti.")
    print("   Instala con: pip install txttoqti>=0.2.0")
    print(f"   Error específico: {e}")
    sys.exit(1)

from .utils import FileManager, BlockDetector
from .format_converter import FormatConverter


class QtiConverter:
    """Orchestrates the complete QTI conversion process."""
    
    def __init__(self, script_path: Optional[Path] = None):
        """
        Initialize the QTI converter.
        
        Args:
            script_path: Path to the calling script (for auto-detection)
        """
        self.file_manager = FileManager()
        self.format_converter = FormatConverter()
        
        # Auto-detect block information
        try:
            self.block_num, self.txt_file, self.qti_file = BlockDetector.detect_block_info(script_path)
            self.block_description = BlockDetector.get_block_description(self.block_num)
        except ValueError as e:
            print(f"❌ Error en detección automática: {e}")
            sys.exit(1)
    
    def show_status(self) -> None:
        """Muestra el estado actual del archivo y conversión."""
        if not os.path.exists(self.txt_file):
            print(f"❌ Error: Archivo {self.txt_file} no encontrado")
            return
        
        question_count = self.file_manager.count_questions(self.txt_file)
        qti_exists = os.path.exists(self.qti_file)
        needs_regeneration = self.file_manager.file_changed(self.txt_file) or not qti_exists
        
        print(f"📊 ESTADO DEL ARCHIVO - BLOQUE {self.block_num}:")
        print(f"   Descripción: {self.block_description}")
        print(f"   Fuente: {self.txt_file}")
        print(f"   Preguntas: {question_count}")
        print(f"   QTI: {self.qti_file} {'(existe)' if qti_exists else '(no existe)'}")
        
        if needs_regeneration:
            print("🔄 Regeneración requerida")
        else:
            print("✅ Sin cambios necesarios")
    
    def convert(self, force: bool = False) -> bool:
        """
        Ejecuta la conversión completa de QTI.
        
        Args:
            force: Si True, fuerza la regeneración aunque no haya cambios
            
        Returns:
            bool: True si la conversión fue exitosa
        """
        # Verificar archivo fuente
        if not os.path.exists(self.txt_file):
            print(f"❌ Error: Archivo {self.txt_file} no encontrado")
            return False
        
        question_count = self.file_manager.count_questions(self.txt_file)
        
        # Verificar si necesita regeneración
        needs_regeneration = (force or 
                             self.file_manager.file_changed(self.txt_file) or 
                             not os.path.exists(self.qti_file))
        
        if not needs_regeneration:
            print(f"✅ QTI está actualizado: {self.qti_file}")
            print(f"📊 {question_count} preguntas - sin cambios necesarios")
            return True
        
        try:
            print(f"🔄 Iniciando conversión para Bloque {self.block_num}")
            print(f"📝 {self.block_description}")
            
            # Validar formato antes de convertir
            with open(self.txt_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            is_valid, errors = self.format_converter.validate_question_format(content)
            if not is_valid:
                print("⚠️  Advertencias de formato encontradas:")
                for error in errors[:5]:  # Mostrar máximo 5 errores
                    print(f"   • {error}")
                if len(errors) > 5:
                    print(f"   • ... y {len(errors) - 5} más")
                
                response = input("¿Continuar con la conversión? (y/N): ")
                if response.lower() != 'y':
                    print("❌ Conversión cancelada por el usuario")
                    return False
            
            # Convertir formato
            print(f"🔄 Convirtiendo formato de {question_count} preguntas...")
            converted_file = self.txt_file.replace('.txt', '_txttoqti_format.txt')
            self.format_converter.convert_to_txttoqti_format(self.txt_file, converted_file)
            print(f"✅ Formato convertido")
            
            # Generar QTI
            print(f"🔄 Generando QTI con txttoqti v0.2.0+...")
            converter = TxtToQtiConverter()
            result = converter.convert_file(converted_file, self.qti_file)
            
            if result and os.path.exists(result):
                print(f"\n🎉 ¡{question_count} preguntas convertidas exitosamente!")
                print(f"📦 QTI generado: {Path(result).name}")
                file_size = Path(result).stat().st_size
                print(f"📏 Tamaño: {file_size:,} bytes")
                print(f"🎯 Bloque: {self.block_num} - {self.block_description}")
                
                # Limpiar archivo temporal
                try:
                    os.unlink(converted_file)
                except Exception:
                    pass
                
                return True
            else:
                print("❌ Error: No se pudo generar el archivo QTI")
                return False
                
        except Exception as e:
            print(f"\n❌ Error durante la conversión: {e}")
            import traceback
            traceback.print_exc()
            return False
    
    def get_file_info(self) -> dict:
        """Retorna información sobre los archivos del bloque actual."""
        return {
            'block_num': self.block_num,
            'block_description': self.block_description,
            'txt_file': self.txt_file,
            'qti_file': self.qti_file,
            'question_count': self.file_manager.count_questions(self.txt_file) if os.path.exists(self.txt_file) else 0,
            'qti_exists': os.path.exists(self.qti_file),
            'needs_regeneration': (self.file_manager.file_changed(self.txt_file) if os.path.exists(self.txt_file) else True) or not os.path.exists(self.qti_file)
        }