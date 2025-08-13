#!/usr/bin/env python3
"""
Test Runner para Notebook to PDF Converter

Suite de tests para verificar funcionamiento correcto de todas las
herramientas de conversión.

Autor: Curso de Ciencia de Datos aplicada al Fútbol
Versión: 1.0.0
"""

import argparse
import unittest
import sys
import os
from pathlib import Path
import tempfile
import shutil
from typing import Optional

# Agregar directorio padre al path para imports
sys.path.insert(0, str(Path(__file__).parent.parent))

class TestRunner:
    """Ejecutor principal de tests."""
    
    def __init__(self):
        self.test_dir = Path(__file__).parent
        self.temp_dir: Optional[Path] = None
        self.coverage_enabled = False
    
    def setup_test_environment(self):
        """Configura el entorno de testing."""
        # Crear directorio temporal
        self.temp_dir = Path(tempfile.mkdtemp(prefix='notebook_test_'))
        
        # Crear notebooks de prueba
        self._create_test_notebooks()
        
        return self.temp_dir
    
    def _create_test_notebooks(self):
        """Crea notebooks de prueba para testing."""
        if self.temp_dir is None:
            raise ValueError("temp_dir no está configurado")
            
        # Notebook básico
        basic_notebook = {
            "cells": [
                {
                    "cell_type": "markdown",
                    "metadata": {},
                    "source": ["# Test Notebook\n", "\n", "Este es un notebook de prueba."]
                },
                {
                    "cell_type": "code",
                    "execution_count": 1,
                    "metadata": {},
                    "outputs": [],
                    "source": ["print('Hello, World!')"]
                }
            ],
            "metadata": {
                "kernelspec": {
                    "display_name": "Python 3",
                    "language": "python",
                    "name": "python3"
                },
                "language_info": {
                    "name": "python",
                    "version": "3.8.0"
                }
            },
            "nbformat": 4,
            "nbformat_minor": 4
        }
        
        # Notebook con contenido en español
        spanish_notebook = {
            "cells": [
                {
                    "cell_type": "markdown",
                    "metadata": {},
                    "source": ["# Análisis de Fútbol\n", "\n", "Estudio de datos deportivos con acentos: árbitro, goleó, técnico."]
                },
                {
                    "cell_type": "code",
                    "execution_count": 1,
                    "metadata": {},
                    "outputs": [],
                    "source": ["equipos = ['Real Madrid', 'Barcelona', 'Atlético']\n", "print(f'Equipos españoles: {equipos}')"]
                }
            ],
            "metadata": {
                "kernelspec": {
                    "display_name": "Python 3",
                    "language": "python",
                    "name": "python3"
                },
                "language_info": {
                    "name": "python",
                    "version": "3.8.0"
                }
            },
            "nbformat": 4,
            "nbformat_minor": 4
        }
        
        # Guardar notebooks
        import json
        
        with open(self.temp_dir / 'basic_test.ipynb', 'w', encoding='utf-8') as f:
            json.dump(basic_notebook, f, indent=2, ensure_ascii=False)
        
        with open(self.temp_dir / 'spanish_test.ipynb', 'w', encoding='utf-8') as f:
            json.dump(spanish_notebook, f, indent=2, ensure_ascii=False)
        
        # Crear subdirectorio con otro notebook
        subdir = self.temp_dir / 'subdir'
        subdir.mkdir()
        
        with open(subdir / 'nested_test.ipynb', 'w', encoding='utf-8') as f:
            json.dump(basic_notebook, f, indent=2, ensure_ascii=False)
    
    def cleanup_test_environment(self):
        """Limpia el entorno de testing."""
        if self.temp_dir and self.temp_dir.exists():
            shutil.rmtree(self.temp_dir)
    
    def discover_tests(self, pattern='test_*.py'):
        """Descubre tests automáticamente."""
        loader = unittest.TestLoader()
        suite = loader.discover(str(self.test_dir), pattern=pattern)
        return suite
    
    def run_specific_test(self, test_name):
        """Ejecuta un test específico."""
        try:
            # Importar módulo de test
            module_name = f'test_{test_name}' if not test_name.startswith('test_') else test_name
            if module_name.endswith('.py'):
                module_name = module_name[:-3]
            
            module = __import__(module_name)
            loader = unittest.TestLoader()
            suite = loader.loadTestsFromModule(module)
            return suite
        except ImportError as e:
            print(f"Error importando test {test_name}: {e}")
            return None
    
    def run_tests(self, test_suite, verbose=True):
        """Ejecuta suite de tests."""
        runner = unittest.TextTestRunner(
            verbosity=2 if verbose else 1,
            stream=sys.stdout,
            buffer=True
        )
        
        result = runner.run(test_suite)
        return result.wasSuccessful()
    
    def validate_environment(self):
        """Valida que el entorno esté listo para tests."""
        print("Validando entorno de testing...")
        
        # Verificar Python
        print(f"✓ Python {sys.version}")
        
        # Verificar imports necesarios
        try:
            import subprocess
            print("✓ subprocess disponible")
        except ImportError:
            print("✗ subprocess no disponible")
            return False
        
        # Verificar que existan los scripts principales
        parent_dir = Path(__file__).parent.parent
        required_files = ['convert.py', 'smart_convert.py', 'convert.sh']
        
        for file in required_files:
            file_path = parent_dir / file
            if file_path.exists():
                print(f"✓ {file} encontrado")
            else:
                print(f"✗ {file} no encontrado")
                return False
        
        # Verificar pandoc (opcional para algunos tests)
        try:
            result = subprocess.run(['pandoc', '--version'], 
                                  capture_output=True, text=True)
            if result.returncode == 0:
                print("✓ pandoc disponible")
            else:
                print("! pandoc no disponible (algunos tests se saltarán)")
        except FileNotFoundError:
            print("! pandoc no encontrado (algunos tests se saltarán)")
        
        print("Entorno validado correctamente")
        return True


def main():
    """Función principal del test runner."""
    parser = argparse.ArgumentParser(
        description='Ejecutor de tests para Notebook to PDF Converter',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos:
  %(prog)s                           # Ejecutar todos los tests
  %(prog)s test_conversion           # Test específico
  %(prog)s --validate                # Solo validar entorno
  %(prog)s --coverage                # Ejecutar con coverage
  %(prog)s --list                    # Listar tests disponibles
        """)
    
    parser.add_argument('test_name', nargs='?',
                       help='Nombre del test específico a ejecutar')
    parser.add_argument('--validate', action='store_true',
                       help='Solo validar entorno y salir')
    parser.add_argument('--coverage', action='store_true',
                       help='Ejecutar tests con coverage (requiere coverage.py)')
    parser.add_argument('--list', action='store_true',
                       help='Listar tests disponibles')
    parser.add_argument('--verbose', '-v', action='store_true',
                       help='Output verboso')
    parser.add_argument('--temp-dir',
                       help='Directorio temporal personalizado')
    
    args = parser.parse_args()
    
    # Crear runner
    runner = TestRunner()
    
    # Solo validar entorno
    if args.validate:
        success = runner.validate_environment()
        sys.exit(0 if success else 1)
    
    # Listar tests disponibles
    if args.list:
        test_files = list(Path(__file__).parent.glob('test_*.py'))
        print("Tests disponibles:")
        for test_file in sorted(test_files):
            test_name = test_file.stem
            print(f"  {test_name}")
        sys.exit(0)
    
    # Validar entorno antes de ejecutar tests
    if not runner.validate_environment():
        print("Entorno no válido para testing")
        sys.exit(1)
    
    # Configurar entorno de test
    try:
        temp_dir = runner.setup_test_environment()
        print(f"Directorio temporal: {temp_dir}")
        
        # Determinar qué tests ejecutar
        if args.test_name:
            # Test específico
            test_suite = runner.run_specific_test(args.test_name)
            if test_suite is None:
                print(f"Test '{args.test_name}' no encontrado")
                sys.exit(1)
        else:
            # Todos los tests
            test_suite = runner.discover_tests()
        
        # Ejecutar tests
        if args.coverage:
            try:
                import coverage
                cov = coverage.Coverage()
                cov.start()
                success = runner.run_tests(test_suite, verbose=args.verbose)
                cov.stop()
                cov.save()
                print("\nReporte de coverage:")
                cov.report()
            except ImportError:
                print("Coverage no disponible, ejecutando sin coverage")
                success = runner.run_tests(test_suite, verbose=args.verbose)
        else:
            success = runner.run_tests(test_suite, verbose=args.verbose)
        
        # Resultado final
        if success:
            print("\n✓ Todos los tests pasaron")
            sys.exit(0)
        else:
            print("\n✗ Algunos tests fallaron")
            sys.exit(1)
    
    except KeyboardInterrupt:
        print("\nTests cancelados por el usuario")
        sys.exit(1)
    except Exception as e:
        print(f"\nError ejecutando tests: {e}")
        sys.exit(1)
    finally:
        # Limpiar entorno
        runner.cleanup_test_environment()


if __name__ == '__main__':
    main()
