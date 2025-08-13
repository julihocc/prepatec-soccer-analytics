#!/usr/bin/env python3
"""
Tests unitarios para el convertidor py-to-marp.
"""

import unittest
import sys
import os
from pathlib import Path
import tempfile
import shutil

# Añadir el directorio padre al path para importar los módulos
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from py_to_marp import PyToMarpConverter
from configs import get_config, list_configs
from convert import convert_single_file, convert_directory


class TestMarpConfigs(unittest.TestCase):
    """Test para las configuraciones de Marp."""
    
    def test_list_configs(self):
        """Test que se pueden listar las configuraciones."""
        configs = list_configs()
        self.assertIsInstance(configs, list)
        self.assertGreater(len(configs), 0)
        self.assertIn('educativo', configs)
        self.assertIn('dark', configs)
        self.assertIn('taller', configs)
    
    def test_get_config_educativo(self):
        """Test configuración educativa."""
        config = get_config('educativo')
        self.assertEqual(config.primary_color, '#3498db')
        self.assertEqual(config.secondary_color, '#e74c3c')
        self.assertIn('Preparatoria', config.footer)
    
    def test_get_config_dark(self):
        """Test configuración dark."""
        config = get_config('dark')
        self.assertEqual(config.background_color, '#1a1a1a')
        self.assertEqual(config.color, '#e9ecef')
    
    def test_get_config_invalid(self):
        """Test configuración inválida."""
        with self.assertRaises(KeyError):
            get_config('configuracion_inexistente')


class TestPyToMarpConverter(unittest.TestCase):
    """Tests para el convertidor principal."""
    
    def setUp(self):
        """Setup para cada test."""
        self.config = get_config('educativo')
        self.converter = PyToMarpConverter(self.config)
        
        # Contenido de prueba simple
        self.simple_py_content = '''# %% [markdown]
# # Título de Prueba
# 
# Este es contenido de prueba.

# %%
print("Hola mundo")
x = 5 + 3
'''
    
    def test_converter_initialization(self):
        """Test inicialización del convertidor."""
        self.assertIsNotNone(self.converter)
        self.assertEqual(self.converter.config.primary_color, '#3498db')
    
    def test_extract_cells_basic(self):
        """Test extracción básica de celdas."""
        cells = self.converter.extract_cells(self.simple_py_content)
        self.assertGreater(len(cells), 0)
        
        # Verificar que hay al menos una celda markdown y una de código
        has_markdown = any(cell['type'] == 'markdown' for cell in cells)
        has_code = any(cell['type'] == 'code' for cell in cells)
        self.assertTrue(has_markdown)
        self.assertTrue(has_code)
    
    def test_convert_to_marp_basic(self):
        """Test conversión básica a Marp."""
        result = self.converter.convert_to_marp(self.simple_py_content, "Test Title")
        
        # Verificar que se genera contenido Marp válido
        self.assertIn('---', result)
        self.assertIn('marp: true', result)
        self.assertIn('Test Title', result)
        self.assertIn('print("Hola mundo")', result)
    
    def test_convert_empty_content(self):
        """Test conversión de contenido vacío."""
        result = self.converter.convert_to_marp("", "Empty Test")
        self.assertIn('marp: true', result)
        self.assertIn('Empty Test', result)
    
    def test_convert_only_markdown(self):
        """Test conversión solo con markdown."""
        markdown_only = '''# %% [markdown]
# # Solo Markdown
# 
# Este contenido solo tiene markdown.
'''
        result = self.converter.convert_to_marp(markdown_only, "Markdown Test")
        self.assertIn('marp: true', result)
        self.assertIn('Solo Markdown', result)
    
    def test_convert_only_code(self):
        """Test conversión solo con código."""
        code_only = '''# %%
print("Solo código")
x = 1 + 1
'''
        result = self.converter.convert_to_marp(code_only, "Code Test")
        self.assertIn('marp: true', result)
        self.assertIn('print("Solo código")', result)


class TestConvertFunctions(unittest.TestCase):
    """Tests para las funciones de conversión de archivos."""
    
    def setUp(self):
        """Setup para cada test."""
        # Crear directorio temporal para tests
        self.test_dir = tempfile.mkdtemp()
        
        # Crear archivo de prueba
        self.test_file = Path(self.test_dir) / "test_file.py"
        with open(self.test_file, 'w', encoding='utf-8') as f:
            f.write('''# %% [markdown]
# # Test File
# 
# Archivo de prueba para tests.

# %%
print("Test successful")
''')
    
    def tearDown(self):
        """Cleanup después de cada test."""
        shutil.rmtree(self.test_dir)
    
    def test_convert_single_file_success(self):
        """Test conversión exitosa de archivo único."""
        result = convert_single_file(
            str(self.test_file), 
            None, 
            'educativo', 
            quiet=True
        )
        
        self.assertEqual(result, 0)
        
        # Verificar que se creó el archivo .md
        md_file = self.test_file.with_suffix('.md')
        self.assertTrue(md_file.exists())
        
        # Verificar contenido
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
            self.assertIn('marp: true', content)
            self.assertIn('Test successful', content)
    
    def test_convert_single_file_nonexistent(self):
        """Test conversión de archivo inexistente."""
        result = convert_single_file(
            str(Path(self.test_dir) / "nonexistent.py"), 
            None, 
            'educativo', 
            quiet=True
        )
        
        self.assertEqual(result, 1)
    
    def test_convert_single_file_custom_output(self):
        """Test conversión con archivo de salida personalizado."""
        custom_output = Path(self.test_dir) / "custom_name.md"
        
        result = convert_single_file(
            str(self.test_file), 
            str(custom_output), 
            'taller', 
            quiet=True
        )
        
        self.assertEqual(result, 0)
        self.assertTrue(custom_output.exists())
    
    def test_convert_directory_success(self):
        """Test conversión de directorio."""
        # Crear archivo adicional
        additional_file = Path(self.test_dir) / "additional.py"
        with open(additional_file, 'w', encoding='utf-8') as f:
            f.write('''# %% [markdown]
# # Additional File

# %%
print("Additional test")
''')
        
        result = convert_directory(self.test_dir, 'dark')
        
        self.assertEqual(result, 0)
        
        # Verificar que se crearon los archivos .md
        md_files = list(Path(self.test_dir).glob("*.md"))
        self.assertEqual(len(md_files), 2)
    
    def test_convert_directory_nonexistent(self):
        """Test conversión de directorio inexistente."""
        result = convert_directory("/path/que/no/existe", 'educativo')
        self.assertEqual(result, 1)
    
    def test_convert_directory_empty(self):
        """Test conversión de directorio sin archivos .py."""
        empty_dir = Path(self.test_dir) / "empty"
        empty_dir.mkdir()
        
        result = convert_directory(str(empty_dir), 'educativo')
        self.assertEqual(result, 0)  # No es error, solo no hay archivos


class TestIntegration(unittest.TestCase):
    """Tests de integración completos."""
    
    def setUp(self):
        """Setup para tests de integración."""
        self.test_dir = tempfile.mkdtemp()
        
        # Crear archivo complejo de prueba
        self.complex_file = Path(self.test_dir) / "complex_test.py"
        with open(self.complex_file, 'w', encoding='utf-8') as f:
            f.write('''# ---
# marp: true
# theme: default
# ---

# %% [markdown]
# # Prueba Compleja
# 
# Este es un test de integración completo.
#
# ---
#
# ## Sección 1: Variables

# %%
# Variables de fútbol
jugador = "Messi"
goles = 800
promedio = goles / 20  # goles por año

# %% [markdown]
# ---
#
# ## Sección 2: Análisis

# %%
if goles > 500:
    categoria = "Leyenda"
else:
    categoria = "Promedio"

print(f"{jugador} es una {categoria}")

# %% [markdown]
# ---
#
# ## Conclusión
#
# Este test verifica la conversión completa.
''')
    
    def tearDown(self):
        """Cleanup después de tests de integración."""
        shutil.rmtree(self.test_dir)
    
    def test_full_conversion_all_configs(self):
        """Test conversión completa con todas las configuraciones."""
        configs = ['educativo', 'taller', 'dark', 'ejecutivo', 'evaluacion']
        
        for config_name in configs:
            with self.subTest(config=config_name):
                output_file = Path(self.test_dir) / f"output_{config_name}.md"
                
                result = convert_single_file(
                    str(self.complex_file),
                    str(output_file),
                    config_name,
                    "Test Completo",
                    quiet=True
                )
                
                self.assertEqual(result, 0)
                self.assertTrue(output_file.exists())
                
                # Verificar contenido específico por configuración
                with open(output_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    self.assertIn('marp: true', content)
                    self.assertIn('Test Completo', content)
                    
                    # Verificar colores específicos por configuración
                    config = get_config(config_name)
                    self.assertIn(config.primary_color, content)
    
    def test_conversion_preserves_code_structure(self):
        """Test que la conversión preserva la estructura del código."""
        result = convert_single_file(
            str(self.complex_file),
            None,
            'educativo',
            quiet=True
        )
        
        self.assertEqual(result, 0)
        
        md_file = self.complex_file.with_suffix('.md')
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
            
            # Verificar que se preservan las variables
            self.assertIn('jugador = "Messi"', content)
            self.assertIn('goles = 800', content)
            
            # Verificar que se preservan las estructuras de control
            self.assertIn('if goles > 500:', content)
            self.assertIn('categoria = "Leyenda"', content)
            
            # Verificar que se preservan los comentarios
            self.assertIn('# goles por año', content)


def run_all_tests():
    """Ejecuta todos los tests."""
    # Crear test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Añadir todos los test cases
    suite.addTests(loader.loadTestsFromTestCase(TestMarpConfigs))
    suite.addTests(loader.loadTestsFromTestCase(TestPyToMarpConverter))
    suite.addTests(loader.loadTestsFromTestCase(TestConvertFunctions))
    suite.addTests(loader.loadTestsFromTestCase(TestIntegration))
    
    # Ejecutar tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    return result.wasSuccessful()


if __name__ == '__main__':
    print("🧪 Ejecutando tests para py-to-marp...")
    print("=" * 50)
    
    success = run_all_tests()
    
    print("=" * 50)
    if success:
        print("✅ Todos los tests pasaron correctamente!")
    else:
        print("❌ Algunos tests fallaron.")
        sys.exit(1)
