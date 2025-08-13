#!/usr/bin/env python3
"""
Script para ejecutar todos los tests de py-to-marp.
"""

import os
import sys
import tempfile
import shutil
from pathlib import Path

# Añadir el directorio padre al path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def test_basic_functionality():
    """Test funcionalidad básica."""
    print("🧪 Test básico de funcionalidad...")
    
    try:
        from py_to_marp import PyToMarpConverter
        from configs import get_config
        from convert import convert_single_file
        
        # Crear archivo temporal
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
            f.write('''# %% [markdown]
# # Test Básico
# 
# Este es un test básico.

# %%
print("Hola mundo desde test")
x = 5 + 3
print(f"Resultado: {x}")
''')
            temp_py = f.name
        
        # Convertir
        result = convert_single_file(temp_py, None, 'educativo', quiet=True)
        
        # Verificar
        temp_md = Path(temp_py).with_suffix('.md')
        success = (result == 0 and temp_md.exists())
        
        if success:
            with open(temp_md, 'r') as f:
                content = f.read()
                success = ('marp: true' in content and 'Hola mundo desde test' in content)
        
        # Limpiar
        Path(temp_py).unlink()
        if temp_md.exists():
            temp_md.unlink()
        
        if success:
            print("✅ Test básico pasó")
            return True
        else:
            print("❌ Test básico falló")
            return False
            
    except Exception as e:
        print(f"❌ Error en test básico: {e}")
        return False

def test_all_configurations():
    """Test todas las configuraciones."""
    print("🧪 Test de todas las configuraciones...")
    
    try:
        from configs import list_configs
        from convert import convert_single_file
        
        # Crear archivo temporal
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
            f.write('''# %% [markdown]
# # Test Configuraciones
# 
# Probando todas las configuraciones.

# %%
for i in range(3):
    print(f"Iteración {i}")
''')
            temp_py = f.name
        
        configs = list_configs()
        success_count = 0
        
        for config_name in configs:
            try:
                base_path = Path(temp_py)
                output_file = base_path.parent / f"{base_path.stem}_{config_name}.md"
                result = convert_single_file(temp_py, str(output_file), config_name, quiet=True)
                
                if result == 0 and output_file.exists():
                    success_count += 1
                    output_file.unlink()  # Limpiar inmediatamente
                    
            except Exception as e:
                print(f"   ❌ Error con configuración {config_name}: {e}")
        
        # Limpiar
        Path(temp_py).unlink()
        
        if success_count == len(configs):
            print(f"✅ Test de configuraciones pasó ({success_count}/{len(configs)})")
            return True
        else:
            print(f"❌ Test de configuraciones falló ({success_count}/{len(configs)})")
            return False
            
    except Exception as e:
        print(f"❌ Error en test de configuraciones: {e}")
        return False

def test_cli_functionality():
    """Test funcionalidad CLI."""
    print("🧪 Test de CLI...")
    
    try:
        import subprocess
        
        # Test --list-configs
        result = subprocess.run([
            'python3', 'convert.py', '--list-configs'
        ], capture_output=True, text=True, cwd='.')
        
        if result.returncode == 0 and 'educativo' in result.stdout:
            print("✅ Test CLI --list-configs pasó")
            return True
        else:
            print("❌ Test CLI falló")
            return False
            
    except Exception as e:
        print(f"❌ Error en test CLI: {e}")
        return False

def test_real_file_conversion():
    """Test conversión de archivo real."""
    print("🧪 Test de conversión de archivo real...")
    
    try:
        from convert import convert_single_file
        
        # Usar el archivo de muestra existente
        sample_file = Path(__file__).parent / 'test_sample.py'
        
        # Convertir
        base_path = Path(sample_file)
        output_file = base_path.parent / f"{base_path.stem}_real_test.md"
        result = convert_single_file(str(sample_file), str(output_file), 'taller', quiet=True)
        
        success = False
        if result == 0 and output_file.exists():
            success = True
            # Limpiar
            output_file.unlink()
        
        if success:
            print("✅ Test de archivo real pasó")
            return True
        else:
            print("❌ Test de archivo real falló")
            return False
            
    except Exception as e:
        print(f"❌ Error en test de archivo real: {e}")
        return False

def run_all_tests():
    """Ejecutar todos los tests."""
    print("🚀 Ejecutando tests para py-to-marp")
    print("=" * 50)
    
    tests = [
        test_basic_functionality,
        test_all_configurations,
        test_cli_functionality,
        test_real_file_conversion
    ]
    
    results = []
    for test in tests:
        try:
            result = test()
            results.append(result)
        except Exception as e:
            print(f"❌ Error ejecutando {test.__name__}: {e}")
            results.append(False)
        print()
    
    print("=" * 50)
    passed = sum(results)
    total = len(results)
    
    if all(results):
        print(f"🎉 Todos los tests pasaron! ({passed}/{total})")
        return True
    else:
        print(f"❌ Algunos tests fallaron. ({passed}/{total})")
        return False

if __name__ == '__main__':
    success = run_all_tests()
    sys.exit(0 if success else 1)
