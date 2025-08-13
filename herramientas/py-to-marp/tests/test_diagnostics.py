#!/usr/bin/env python3
"""
Test simple para identificar problemas en py-to-marp.
"""

import sys
import os
from pathlib import Path

# Añadir el directorio actual al path
sys.path.insert(0, '.')

def test_imports():
    """Test que los módulos se pueden importar."""
    print("🧪 Probando imports...")
    
    try:
        from py_to_marp import PyToMarpConverter
        print("✅ py_to_marp importado correctamente")
    except Exception as e:
        print(f"❌ Error importando py_to_marp: {e}")
        return False
    
    try:
        from configs import get_config, list_configs
        print("✅ configs importado correctamente")
    except Exception as e:
        print(f"❌ Error importando configs: {e}")
        return False
    
    try:
        import convert
        print("✅ convert importado correctamente")
    except Exception as e:
        print(f"❌ Error importando convert: {e}")
        return False
    
    return True

def test_configs():
    """Test que las configuraciones funcionan."""
    print("\n🧪 Probando configuraciones...")
    
    try:
        from configs import get_config, list_configs
        
        configs = list_configs()
        print(f"✅ Configuraciones disponibles: {configs}")
        
        for config_name in ['educativo', 'taller', 'dark']:
            config = get_config(config_name)
            print(f"✅ Configuración '{config_name}': {config.primary_color}")
        
        return True
    except Exception as e:
        print(f"❌ Error en configuraciones: {e}")
        return False

def test_basic_conversion():
    """Test conversión básica."""
    print("\n🧪 Probando conversión básica...")
    
    try:
        from py_to_marp import PyToMarpConverter
        from configs import get_config
        
        # Contenido simple de prueba
        py_content = '''# %% [markdown]
# # Test Simple
# 
# Prueba básica.

# %%
print("Hola mundo")
'''
        
        config = get_config('educativo')
        converter = PyToMarpConverter(config)
        
        result = converter.convert_to_marp(py_content, "Test Simple")
        
        if 'marp: true' in result and 'Hola mundo' in result:
            print("✅ Conversión básica exitosa")
            return True
        else:
            print("❌ Conversión básica falló")
            return False
            
    except Exception as e:
        print(f"❌ Error en conversión básica: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_cli_functions():
    """Test funciones CLI."""
    print("\n🧪 Probando funciones CLI...")
    
    try:
        import convert
        
        # Verificar que las funciones existen
        if hasattr(convert, 'convert_single_file'):
            print("✅ convert_single_file existe")
        else:
            print("❌ convert_single_file no existe")
            return False
            
        if hasattr(convert, 'main'):
            print("✅ main existe")
        else:
            print("❌ main no existe")
            return False
            
        return True
        
    except Exception as e:
        print(f"❌ Error en funciones CLI: {e}")
        return False

def test_file_conversion():
    """Test conversión de archivo real."""
    print("\n🧪 Probando conversión de archivo...")
    
    try:
        import convert
        
        # Crear archivo de prueba
        test_file = Path("test_temp.py")
        with open(test_file, 'w') as f:
            f.write('''# %% [markdown]
# # Test File
# 
# Archivo de prueba.

# %%
print("Test exitoso")
''')
        
        # Probar conversión
        result = convert.convert_single_file(
            str(test_file),
            "test_temp.md",
            'educativo',
            quiet=True
        )
        
        if result == 0 and Path("test_temp.md").exists():
            print("✅ Conversión de archivo exitosa")
            
            # Limpiar
            test_file.unlink()
            Path("test_temp.md").unlink()
            return True
        else:
            print("❌ Conversión de archivo falló")
            # Limpiar
            if test_file.exists():
                test_file.unlink()
            if Path("test_temp.md").exists():
                Path("test_temp.md").unlink()
            return False
            
    except Exception as e:
        print(f"❌ Error en conversión de archivo: {e}")
        import traceback
        traceback.print_exc()
        
        # Limpiar en caso de error
        if Path("test_temp.py").exists():
            Path("test_temp.py").unlink()
        if Path("test_temp.md").exists():
            Path("test_temp.md").unlink()
        return False

def main():
    """Ejecutar todos los tests."""
    print("🚀 Iniciando tests diagnósticos para py-to-marp")
    print("=" * 50)
    
    tests = [
        test_imports,
        test_configs,
        test_basic_conversion,
        test_cli_functions,
        test_file_conversion
    ]
    
    results = []
    for test in tests:
        result = test()
        results.append(result)
        if not result:
            print(f"\n⚠️  Test {test.__name__} falló. Deteniendo tests.")
            break
    
    print("\n" + "=" * 50)
    passed = sum(results)
    total = len(results)
    
    if all(results):
        print(f"🎉 Todos los tests pasaron! ({passed}/{total})")
        return True
    else:
        print(f"❌ Algunos tests fallaron. ({passed}/{total})")
        return False

if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)
