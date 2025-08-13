#!/usr/bin/env python3
"""
Tests para el convertidor principal de notebooks.

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

# Agregar directorio padre al path
sys.path.insert(0, str(Path(__file__).parent.parent))

try:
    from convert import NotebookConverter
except ImportError:
    NotebookConverter = None


class TestNotebookConverter(unittest.TestCase):
    """Tests para la clase NotebookConverter."""
    
    def setUp(self):
        """Configuración para cada test."""
        self.temp_dir = Path(tempfile.mkdtemp(prefix='test_convert_'))
        self.converter = NotebookConverter() if NotebookConverter else None
        
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
                    "source": ["# Test Notebook\n", "Este es un test."]
                },
                {
                    "cell_type": "code",
                    "execution_count": 1,
                    "metadata": {},
                    "outputs": [],
                    "source": ["print('Hola, mundo!')"]
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
        
        self.test_notebook = self.temp_dir / 'test.ipynb'
        with open(self.test_notebook, 'w', encoding='utf-8') as f:
            json.dump(notebook_content, f, indent=2, ensure_ascii=False)
    
    def test_converter_initialization(self):
        """Test inicialización del convertidor."""
        if self.converter is None:
            self.skipTest("NotebookConverter no disponible")
        
        self.assertIsNotNone(self.converter)
        self.assertEqual(self.converter.default_engine, 'xelatex')
        self.assertIn('xelatex', self.converter.engines)
        self.assertEqual(self.converter.converted_count, 0)
    
    def test_check_dependencies_method(self):
        """Test verificación de dependencias."""
        if self.converter is None:
            self.skipTest("NotebookConverter no disponible")
        
        deps_ok, missing = self.converter.check_dependencies()
        self.assertIsInstance(deps_ok, bool)
        self.assertIsInstance(missing, list)
        
        # Si faltan dependencias, pandoc debe estar en la lista
        if not deps_ok:
            dependency_names = ' '.join(missing).lower()
            self.assertTrue('pandoc' in dependency_names or 'latex' in dependency_names)
    
    def test_find_notebooks_file(self):
        """Test búsqueda de notebook individual."""
        if self.converter is None:
            self.skipTest("NotebookConverter no disponible")
        
        notebooks = self.converter.find_notebooks(self.test_notebook)
        self.assertEqual(len(notebooks), 1)
        self.assertEqual(notebooks[0], self.test_notebook)
    
    def test_find_notebooks_directory(self):
        """Test búsqueda en directorio."""
        if self.converter is None:
            self.skipTest("NotebookConverter no disponible")
        
        # Crear notebook adicional
        notebook2 = self.temp_dir / 'test2.ipynb'
        shutil.copy(self.test_notebook, notebook2)
        
        notebooks = self.converter.find_notebooks(self.temp_dir)
        self.assertEqual(len(notebooks), 2)
        self.assertIn(self.test_notebook, notebooks)
        self.assertIn(notebook2, notebooks)
    
    def test_find_notebooks_recursive(self):
        """Test búsqueda recursiva."""
        if self.converter is None:
            self.skipTest("NotebookConverter no disponible")
        
        # Crear subdirectorio con notebook
        subdir = self.temp_dir / 'subdir'
        subdir.mkdir()
        notebook_sub = subdir / 'test_sub.ipynb'
        shutil.copy(self.test_notebook, notebook_sub)
        
        # Búsqueda recursiva
        notebooks = self.converter.find_notebooks(self.temp_dir, recursive=True)
        self.assertEqual(len(notebooks), 2)
        
        # Búsqueda no recursiva
        notebooks = self.converter.find_notebooks(self.temp_dir, recursive=False)
        self.assertEqual(len(notebooks), 1)
    
    def test_convert_notebook_dry_run(self):
        """Test conversión en modo dry run."""
        if self.converter is None:
            self.skipTest("NotebookConverter no disponible")
        
        output_path = self.test_notebook.with_suffix('.pdf')
        success, message = self.converter.convert_notebook(
            self.test_notebook, output_path, dry_run=True
        )
        
        self.assertTrue(success)
        self.assertIn('[DRY-RUN]', message)
        self.assertFalse(output_path.exists())  # No debe crear el archivo
    
    @unittest.skipIf(not shutil.which('pandoc'), "pandoc no disponible")
    def test_convert_notebook_real(self):
        """Test conversión real (requiere pandoc)."""
        if self.converter is None:
            self.skipTest("NotebookConverter no disponible")
        
        output_path = self.test_notebook.with_suffix('.pdf')
        success, message = self.converter.convert_notebook(
            self.test_notebook, output_path
        )
        
        # Verificar resultado
        if success:
            self.assertTrue(output_path.exists())
            self.assertGreater(output_path.stat().st_size, 0)
            self.assertIn('Convertido', message)
        else:
            # Si falla, debe ser por dependencias faltantes
            self.assertIn('Error', message)


class TestConverterScript(unittest.TestCase):
    """Tests para el script convert.py."""
    
    def setUp(self):
        """Configuración para cada test."""
        self.script_path = Path(__file__).parent.parent / 'convert.py'
        
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
        self.assertIn('notebook', result.stdout.lower())
    
    def test_script_check_deps(self):
        """Test verificación de dependencias."""
        result = subprocess.run([
            sys.executable, str(self.script_path), '--check-deps'
        ], capture_output=True, text=True)
        
        # Debe exitir con 0 (deps OK) o 1 (deps faltantes)
        self.assertIn(result.returncode, [0, 1])
        
        if result.returncode == 0:
            self.assertIn('dependencias están instaladas', result.stdout)
        else:
            self.assertIn('dependencias faltantes', result.stdout)
    
    def test_script_invalid_input(self):
        """Test con entrada inválida."""
        result = subprocess.run([
            sys.executable, str(self.script_path), '/path/inexistente'
        ], capture_output=True, text=True)
        
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('Error', result.stderr)


class TestEngineSupport(unittest.TestCase):
    """Tests para soporte de diferentes motores LaTeX."""
    
    def test_xelatex_available(self):
        """Test disponibilidad de XeLaTeX."""
        result = subprocess.run(['which', 'xelatex'], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            # Verificar versión
            version_result = subprocess.run(['xelatex', '--version'],
                                          capture_output=True, text=True)
            self.assertEqual(version_result.returncode, 0)
            self.assertIn('xetex', version_result.stdout.lower())
    
    def test_pdflatex_available(self):
        """Test disponibilidad de PDFLaTeX."""
        result = subprocess.run(['which', 'pdflatex'], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            # Verificar versión
            version_result = subprocess.run(['pdflatex', '--version'],
                                          capture_output=True, text=True)
            self.assertEqual(version_result.returncode, 0)
    
    def test_pandoc_available(self):
        """Test disponibilidad de pandoc."""
        result = subprocess.run(['which', 'pandoc'], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            # Verificar versión
            version_result = subprocess.run(['pandoc', '--version'],
                                          capture_output=True, text=True)
            self.assertEqual(version_result.returncode, 0)
            self.assertIn('pandoc', version_result.stdout.lower())


if __name__ == '__main__':
    unittest.main()
