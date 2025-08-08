#!/usr/bin/env python3
"""
Script de ins    print("
Actualizando pip...")
    try:
        subprocess.run([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'], 
                      capture_output=True, text=True, check=True)
        print("pip actualizado correctamente")
    except subprocess.CalledProcessError:
        print("Advertencia: No se pudo actualizar pip")n automática para el curso de Ciencia de Datos Aplicada al Fútbol
Tecnológico de Monterrey - Tópicos de Ciencia de Datos

Este script instala automáticamente todas las dependencias necesarias
para ejecutar los notebooks del curso.
"""

import subprocess
import sys
import os
from pathlib import Path

def main():
    print("🏈 INSTALADOR DE DEPENDENCIAS - CIENCIA DE DATOS APLICADA AL FÚTBOL")
    print("=" * 70)
    print("Tecnológico de Monterrey - Tópicos de Ciencia de Datos")
    print("=" * 70)
    
    # Verificar que Python está disponible
    python_version = sys.version_info
    print(f"🐍 Python {python_version.major}.{python_version.minor}.{python_version.micro}")
    
    if python_version < (3, 8):
        print("Error: Se requiere Python 3.8 o superior")
        print("Por favor actualice su versión de Python")
        return False
    
    # Buscar archivo requirements.txt
    script_dir = Path(__file__).parent
    requirements_file = script_dir / 'requirements.txt'
    
    if not requirements_file.exists():
        print(f"Archivo requirements.txt no encontrado en: {requirements_file}")
        return False
    
    print(f"📋 Archivo de requerimientos: {requirements_file}")
    
    # Actualizar pip primero
    print("\nActualizando pip...")
    try:
        subprocess.run([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'], 
                      check=True, capture_output=True)
        print("pip actualizado correctamente")
    except subprocess.CalledProcessError as e:
        print("Advertencia: No se pudo actualizar pip")
    
    # Instalar dependencias
    print("\nInstalando dependencias del curso...")
    try:
        result = subprocess.run([
            sys.executable, '-m', 'pip', 'install', '-r', str(requirements_file)
        ], check=True, capture_output=True, text=True)
        
        print("Todas las dependencias instaladas correctamente")
        
    except subprocess.CalledProcessError as e:
        print("Error durante la instalación:")
        print(f"Código de error: {e.returncode}")
        print(f"Error: {e.stderr}")
        return False
    
    # Verificar instalación
    print("\nVerificando instalación...")
    packages_to_verify = [
        'pandas', 'numpy', 'matplotlib', 'seaborn', 
        'scikit-learn', 'scipy', 'jupyter'
    ]
    
    all_installed = True
    for package in packages_to_verify:
        try:
            if package == 'scikit-learn':
                __import__('sklearn')
            else:
                __import__(package)
            print(f"{package}")
        except ImportError:
            print(f"{package} - NO DISPONIBLE")
            all_installed = False
    
    if all_installed:
        print("\n¡INSTALACIÓN COMPLETADA EXITOSAMENTE!")
        print("Todos los paquetes necesarios están disponibles")
        print("Ya puedes ejecutar los notebooks del curso")
        print("\nPara iniciar Jupyter Notebook ejecuta:")
        print("   jupyter notebook")
    else:
        print("\nAlgunos paquetes no se instalaron correctamente")
        print("Intenta ejecutar manualmente:")
        print("   pip install -r requirements.txt")
    
    print("\n" + "=" * 70)
    return all_installed

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
