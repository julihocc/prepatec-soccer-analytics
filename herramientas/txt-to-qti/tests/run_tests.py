#!/usr/bin/env python3
"""
Test runner para la suite completa de tests del convertidor TXT→CSV→QTI
Ejecuta todos los tests y proporciona un reporte comprehensivo
"""

import unittest
import sys
import os
import time
from pathlib import Path
from io import StringIO

def run_test_suite():
    """Ejecuta la suite completa de tests"""
    
    # Configurar path
    test_dir = Path(__file__).parent
    sys.path.insert(0, str(test_dir.parent))
    
    # Descubrir y cargar todos los tests
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Cargar tests específicos
    test_modules = [
        'test_txt_to_csv',
        'test_csv_to_qti', 
        'test_integration'
    ]
    
    print("🔍 Cargando tests...")
    for module_name in test_modules:
        try:
            module = __import__(module_name)
            module_suite = loader.loadTestsFromModule(module)
            suite.addTest(module_suite)
            print(f"  ✅ {module_name}")
        except ImportError as e:
            print(f"  ❌ Error cargando {module_name}: {e}")
            return False
    
    # Ejecutar tests
    print(f"\n🧪 Ejecutando {suite.countTestCases()} tests...\n")
    
    # Configurar runner con verbosidad
    stream = StringIO()
    runner = unittest.TextTestRunner(
        stream=stream,
        verbosity=2,
        buffer=True,
        failfast=False
    )
    
    start_time = time.time()
    result = runner.run(suite)
    end_time = time.time()
    
    # Mostrar resultados
    print("="*70)
    print("📊 REPORTE DE TESTS")
    print("="*70)
    
    # Estadísticas generales
    total_tests = result.testsRun
    failures = len(result.failures)
    errors = len(result.errors)
    skipped = len(result.skipped) if hasattr(result, 'skipped') else 0
    success = total_tests - failures - errors - skipped
    
    print(f"Total de tests ejecutados: {total_tests}")
    print(f"✅ Exitosos: {success}")
    print(f"❌ Fallos: {failures}")
    print(f"🚫 Errores: {errors}")
    print(f"⏭️  Omitidos: {skipped}")
    print(f"⏱️  Tiempo total: {end_time - start_time:.2f}s")
    
    success_rate = (success / total_tests * 100) if total_tests > 0 else 0
    print(f"📈 Tasa de éxito: {success_rate:.1f}%")
    
    # Detalles de fallos
    if failures:
        print("\n" + "="*50)
        print("❌ DETALLES DE FALLOS")
        print("="*50)
        for test, traceback in result.failures:
            print(f"\n🔴 {test}")
            print("-" * 40)
            print(traceback)
    
    # Detalles de errores
    if errors:
        print("\n" + "="*50)
        print("🚫 DETALLES DE ERRORES")
        print("="*50)
        for test, traceback in result.errors:
            print(f"\n🔴 {test}")
            print("-" * 40)
            print(traceback)
    
    # Resumen final
    print("\n" + "="*70)
    if failures == 0 and errors == 0:
        print("🎉 TODOS LOS TESTS PASARON EXITOSAMENTE")
        print("✅ El sistema está funcionando correctamente")
    else:
        print("⚠️  SE ENCONTRARON PROBLEMAS")
        print("❗ Revisa los fallos y errores arriba")
    print("="*70)
    
    return failures == 0 and errors == 0

def run_specific_test(test_name):
    """Ejecuta un test específico"""
    
    test_dir = Path(__file__).parent
    sys.path.insert(0, str(test_dir.parent))
    
    try:
        # Cargar test específico
        if '.' in test_name:
            module_name, test_class = test_name.split('.', 1)
        else:
            module_name = test_name
            test_class = None
            
        module = __import__(module_name)
        
        if test_class:
            suite = unittest.TestSuite()
            if '.' in test_class:
                # Test específico: module.TestClass.test_method
                class_name, method_name = test_class.split('.', 1)
                test_case = getattr(module, class_name)(method_name)
                suite.addTest(test_case)
            else:
                # Clase de test: module.TestClass
                test_cls = getattr(module, test_class)
                suite.addTest(unittest.TestLoader().loadTestsFromTestCase(test_cls))
        else:
            # Módulo completo
            suite = unittest.TestLoader().loadTestsFromModule(module)
        
        # Ejecutar
        runner = unittest.TextTestRunner(verbosity=2)
        result = runner.run(suite)
        
        return result.wasSuccessful()
        
    except Exception as e:
        print(f"❌ Error ejecutando test '{test_name}': {e}")
        return False

def validate_environment():
    """Valida que el entorno esté configurado correctamente"""
    
    print("🔧 Validando entorno...")
    
    # Verificar archivos principales
    test_dir = Path(__file__).parent
    parent_dir = test_dir.parent
    
    required_files = [
        'txt_to_csv_direct.py',
        'csv_to_kansas_qti.py'
    ]
    
    missing_files = []
    for file_name in required_files:
        file_path = parent_dir / file_name
        if not file_path.exists():
            missing_files.append(file_name)
        else:
            print(f"  ✅ {file_name}")
    
    if missing_files:
        print(f"\n❌ Archivos faltantes: {', '.join(missing_files)}")
        return False
    
    # Verificar archivos de test
    test_files = [
        'test_questions_valid.txt',
        'test_questions_invalid.txt', 
        'test_questions_edge_cases.txt'
    ]
    
    for test_file in test_files:
        if not (test_dir / test_file).exists():
            print(f"  ⚠️  Archivo de test faltante: {test_file}")
        else:
            print(f"  ✅ {test_file}")
    
    print("  ✅ Entorno validado\n")
    return True

def show_help():
    """Muestra ayuda de uso"""
    print("""
🧪 Test Runner para Convertidor TXT→CSV→QTI

Uso:
    python run_tests.py                     # Ejecutar todos los tests
    python run_tests.py --help             # Mostrar esta ayuda
    python run_tests.py --validate         # Solo validar entorno
    python run_tests.py <test_name>        # Ejecutar test específico

Ejemplos de tests específicos:
    python run_tests.py test_txt_to_csv                    # Módulo completo
    python run_tests.py test_txt_to_csv.TestTxtToCSVConverter  # Clase de test
    python run_tests.py test_integration.TestFullPipeline.test_complete_pipeline_valid_questions  # Test específico

Archivos de test:
    test_txt_to_csv.py      - Tests del convertidor TXT→CSV
    test_csv_to_qti.py      - Tests del generador CSV→QTI
    test_integration.py     - Tests de integración del pipeline completo

Tests disponibles:
    • Validación de formato TXT
    • Conversión TXT→CSV
    • Generación QTI
    • Pipeline completo
    • Casos especiales y edge cases
    • Tests de rendimiento
""")

def main():
    """Función principal"""
    
    args = sys.argv[1:]
    
    if not args:
        # Ejecutar todos los tests
        if not validate_environment():
            sys.exit(1)
        success = run_test_suite()
        sys.exit(0 if success else 1)
        
    elif args[0] == '--help':
        show_help()
        
    elif args[0] == '--validate':
        success = validate_environment()
        sys.exit(0 if success else 1)
        
    else:
        # Ejecutar test específico
        test_name = args[0]
        if not validate_environment():
            sys.exit(1)
        success = run_specific_test(test_name)
        sys.exit(0 if success else 1)

if __name__ == '__main__':
    main()