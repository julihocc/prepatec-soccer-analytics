#!/usr/bin/env python3
"""
Tests para el convertidor inteligente de notebooks.

Autor: Curso de Ciencia de Datos aplicada al Fútbol
Versión: 1.0.0
"""

import unittest
import subprocess
import sys
from pathlib import Path
import tempfile
import shutil
import json
import time

# Agregar directorio padre al path
sys.path.insert(0, str(Path(__file__).parent.parent))

try:
    from smart_convert import SmartConverter
except ImportError:
    SmartConverter = None


class TestSmartConverter(unittest.TestCase):
    """Tests para la clase SmartConverter."""
    
    def setUp(self):
        """Configuración para cada test."""
        self.temp_dir = Path(tempfile.mkdtemp(prefix='test_smart_'))
        self.cache_file = self.temp_dir / 'test_cache.json'
        self.converter = SmartConverter(str(self.cache_file)) if SmartConverter else None
        
        # Crear notebook de prueba
        self._create_test_notebook()
    
    def tearDown(self):
        """Limpieza después de cada test."""
        if self.temp_dir.exists():
            shutil.rmtree(self.temp_dir)
    
    def _create_test_notebook(self):
        """Crea un notebook de prueba."""
        notebook_content = {
            "cells": [
                {
                    "cell_type": "markdown",
                    "metadata": {},
                    "source": ["# Smart Test Notebook\n", "Test para conversión inteligente."]
                },
                {
                    "cell_type": "code",
                    "execution_count": 1,
                    "metadata": {},
                    "outputs": [],
                    "source": ["import pandas as pd\n", "print('Smart conversion test')"]
                }
            ],
            "metadata": {
                "kernelspec": {
                    "display_name": "Python 3",
                    "language": "python",
                    "name": "python3"
                }
            },
            "nbformat": 4,
            "nbformat_minor": 4
        }
        
        self.test_notebook = self.temp_dir / 'smart_test.ipynb'
        with open(self.test_notebook, 'w', encoding='utf-8') as f:
            json.dump(notebook_content, f, indent=2, ensure_ascii=False)
    
    def test_smart_converter_initialization(self):
        """Test inicialización del convertidor inteligente."""
        if self.converter is None:
            self.skipTest("SmartConverter no disponible")
        
        self.assertIsNotNone(self.converter)
        self.assertEqual(self.converter.cache_file, self.cache_file)
        self.assertIsInstance(self.converter.cache, dict)
    
    def test_file_hash_calculation(self):
        """Test cálculo de hash de archivos."""
        if self.converter is None:
            self.skipTest("SmartConverter no disponible")
        
        # Calcular hash inicial
        hash1 = self.converter._get_file_hash(self.test_notebook)
        self.assertIsInstance(hash1, str)
        self.assertEqual(len(hash1), 32)  # MD5 hash length
        
        # Hash debe ser consistente
        hash2 = self.converter._get_file_hash(self.test_notebook)
        self.assertEqual(hash1, hash2)
        
        # Modificar archivo y verificar cambio de hash
        with open(self.test_notebook, 'a', encoding='utf-8') as f:
            f.write('\n# Modificación')
        
        hash3 = self.converter._get_file_hash(self.test_notebook)
        self.assertNotEqual(hash1, hash3)
    
    def test_needs_conversion_new_file(self):
        """Test necesidad de conversión para archivo nuevo."""
        if self.converter is None:
            self.skipTest("SmartConverter no disponible")
        
        pdf_path = self.test_notebook.with_suffix('.pdf')
        needs_conv, reason = self.converter._needs_conversion(
            self.test_notebook, pdf_path
        )
        
        self.assertTrue(needs_conv)
        self.assertEqual(reason, "PDF no existe")
    
    def test_needs_conversion_force(self):
        """Test conversión forzada."""
        if self.converter is None:
            self.skipTest("SmartConverter no disponible")
        
        pdf_path = self.test_notebook.with_suffix('.pdf')
        
        # Crear PDF ficticio (más reciente)
        pdf_path.touch()
        time.sleep(0.1)  # Asegurar timestamp diferente
        
        needs_conv, reason = self.converter._needs_conversion(
            self.test_notebook, pdf_path, force=True
        )
        
        self.assertTrue(needs_conv)
        self.assertEqual(reason, "Forzada")
    
    def test_needs_conversion_timestamp(self):
        """Test verificación por timestamp."""
        if self.converter is None:
            self.skipTest("SmartConverter no disponible")
        
        pdf_path = self.test_notebook.with_suffix('.pdf')
        
        # Crear PDF más antiguo
        pdf_path.touch()
        time.sleep(0.1)
        
        # Modificar notebook (más reciente)
        with open(self.test_notebook, 'a', encoding='utf-8') as f:
            f.write('\n# Timestamp test')
        
        needs_conv, reason = self.converter._needs_conversion(
            self.test_notebook, pdf_path
        )
        
        self.assertTrue(needs_conv)
        self.assertEqual(reason, "Notebook más reciente")
    
    def test_cache_operations(self):
        """Test operaciones de cache."""
        if self.converter is None:
            self.skipTest("SmartConverter no disponible")
        
        # Cache inicial debe estar vacío
        self.assertEqual(len(self.converter.cache), 0)
        
        # Agregar entrada al cache
        notebook_str = str(self.test_notebook.absolute())
        test_hash = 'test_hash_123'
        self.converter.cache[notebook_str] = {
            'hash': test_hash,
            'converted_at': time.time(),
            'pdf_path': 'test.pdf'
        }
        
        # Guardar cache
        self.converter._save_cache()
        self.assertTrue(self.cache_file.exists())
        
        # Crear nuevo converter y verificar carga
        if SmartConverter is None:
            self.skipTest("SmartConverter no disponible")
        converter2 = SmartConverter(str(self.cache_file))
        self.assertEqual(len(converter2.cache), 1)
        self.assertIn(notebook_str, converter2.cache)
        self.assertEqual(converter2.cache[notebook_str]['hash'], test_hash)
    
    def test_status_display(self):
        """Test mostrar estado de notebooks."""
        if self.converter is None:
            self.skipTest("SmartConverter no disponible")
        
        # Crear lista de notebooks
        notebooks = [self.test_notebook]
        
        # Capturar output (esto es básico, en producción usaríamos mocking)
        # Por ahora solo verificamos que el método no falle
        try:
            self.converter.show_status(notebooks)
            # Si llegamos aquí, el método no falló
            self.assertTrue(True)
        except Exception as e:
            self.fail(f"show_status falló: {e}")


class TestSmartConverterScript(unittest.TestCase):
    """Tests para el script smart_convert.py."""
    
    def setUp(self):
        """Configuración para cada test."""
        self.script_path = Path(__file__).parent.parent / 'smart_convert.py'
    
    def test_script_exists(self):
        """Test que el script existe."""
        self.assertTrue(self.script_path.exists())
        self.assertTrue(self.script_path.is_file())
    
    def test_script_help(self):
        """Test que el script muestra ayuda."""
        result = subprocess.run([
            sys.executable, str(self.script_path), '--help'
        ], capture_output=True, text=True)
        
        self.assertEqual(result.returncode, 0)
        self.assertIn('usage:', result.stdout.lower())
        self.assertIn('inteligente', result.stdout.lower())
    
    def test_script_status_nonexistent(self):
        """Test status con directorio inexistente."""
        result = subprocess.run([
            sys.executable, str(self.script_path), 
            '/directorio/inexistente', '--status'
        ], capture_output=True, text=True)
        
        self.assertNotEqual(result.returncode, 0)


class TestCacheConsistency(unittest.TestCase):
    """Tests para consistencia del cache."""
    
    def setUp(self):
        """Configuración para cada test."""
        self.temp_dir = Path(tempfile.mkdtemp(prefix='test_cache_'))
        self.cache_file = self.temp_dir / 'consistency_cache.json'
        
    def tearDown(self):
        """Limpieza después de cada test."""
        if self.temp_dir.exists():
            shutil.rmtree(self.temp_dir)
    
    def test_cache_corruption_handling(self):
        """Test manejo de cache corrupto."""
        if SmartConverter is None:
            self.skipTest("SmartConverter no disponible")
        
        # Crear cache corrupto
        with open(self.cache_file, 'w') as f:
            f.write('{"invalid": json}')
        
        # Converter debe manejar el cache corrupto graciosamente
        converter = SmartConverter(str(self.cache_file))
        self.assertIsInstance(converter.cache, dict)
        self.assertEqual(len(converter.cache), 0)
    
    def test_cache_missing_file(self):
        """Test cache con archivo faltante."""
        if SmartConverter is None:
            self.skipTest("SmartConverter no disponible")
        
        # Cache file no existe
        converter = SmartConverter(str(self.cache_file))
        self.assertIsInstance(converter.cache, dict)
        self.assertEqual(len(converter.cache), 0)


if __name__ == '__main__':
    unittest.main()
