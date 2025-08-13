#!/usr/bin/env python3
"""
Script mejorado para convertir archivos py:percent a Marp con configuraciones predefinidas.
"""

import argparse
import sys
from pathlib import Path
from typing import Optional
from py_to_marp import PyToMarpConverter
from configs import get_config, list_configs


def convert_single_file(input_file: str, output_file: Optional[str] = None, config_name: str = "educativo", 
                       title: Optional[str] = None, custom_header: Optional[str] = None, 
                       custom_footer: Optional[str] = None, quiet: bool = False) -> int:
    """Convierte un archivo individual."""
    # Validar archivo de entrada
    input_path = Path(input_file)
    if not input_path.exists():
        if not quiet:
            print(f"❌ Error: El archivo {input_path} no existe.")
        return 1
    
    if input_path.suffix != '.py' and not quiet:
        print(f"⚠️  Advertencia: El archivo {input_path} no tiene extensión .py")
    
    # Determinar archivo de salida
    if output_file:
        output_path = Path(output_file)
    else:
        output_path = input_path.with_suffix('.md')
    
    # Leer contenido
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            py_content = f.read()
    except Exception as e:
        if not quiet:
            print(f"❌ Error leyendo {input_path}: {e}")
        return 1
    
    # Configurar presentación
    config = get_config(config_name)
    
    # Convertir
    converter = PyToMarpConverter(config)
    
    # Generar título inteligente
    if title:
        final_title = title
    else:
        # Extraer de nombre de archivo o contenido
        final_title = input_path.stem.replace('-', ' ').replace('_', ' ').title()
        
        # Intentar extraer título del contenido
        title_match = py_content.find('# ')
        if title_match != -1:
            line_end = py_content.find('\n', title_match)
            potential_title = py_content[title_match+2:line_end].strip()
            if potential_title and len(potential_title) < 100:
                final_title = potential_title
    
    if not quiet:
        print(f"🔄 Convirtiendo {input_path.name} con configuración '{config_name}'...")
    
    marp_content = converter.convert_to_marp(py_content, final_title)
    
    # Escribir resultado
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(marp_content)
        
        if not quiet:
            slides_count = marp_content.count('---')
            print(f"✅ Presentación Marp generada: {output_path}")
            print(f"   📄 Slides: {slides_count}")
            print(f"   🎨 Configuración: {config_name}")
            
    except Exception as e:
        if not quiet:
            print(f"❌ Error escribiendo {output_path}: {e}")
        return 1
    
    return 0


def main():
    """Función principal."""
    parser = argparse.ArgumentParser(description="Convierte archivos py:percent a presentaciones Marp")
    
    parser.add_argument("input_file", nargs="?", help="Archivo .py en formato percent de entrada")
    parser.add_argument("-o", "--output", help="Archivo .md de salida")
    parser.add_argument("--config", choices=list_configs(), default="educativo", help="Configuración predefinida")
    parser.add_argument("--title", help="Título personalizado")
    parser.add_argument("--list-configs", action="store_true", help="Lista configuraciones disponibles")
    
    args = parser.parse_args()
    
    if args.list_configs:
        print("Configuraciones disponibles:")
        configs = list_configs()
        for config_name in configs:
            config = get_config(config_name)
            print(f"  {config_name:12} - {config.primary_color}")
        return 0
    
    if not args.input_file:
        parser.error("Se requiere un archivo de entrada")
    
    return convert_single_file(args.input_file, args.output, args.config, args.title)


if __name__ == "__main__":
    sys.exit(main())
