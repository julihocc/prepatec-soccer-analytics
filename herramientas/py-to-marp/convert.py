#!/usr/bin/env python3
"""
Script mejorado para convertir archivos py:percent a Marp con configuraciones predefinidas.
"""

import argparse
import sys
from pathlib import Path
from py_to_marp import PyToMarpConverter
from configs import get_config, list_configs, EDUCATIVO_PRINCIPAL


def main():
    """Función principal mejorada."""
    parser = argparse.ArgumentParser(
        description="Convierte archivos py:percent a presentaciones Marp con estilos predefinidos",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos de uso:
  %(prog)s contenido.py                    # Usa configuración educativa por defecto
  %(prog)s contenido.py --config taller    # Usa configuración para talleres
  %(prog)s contenido.py --config dark      # Usa tema oscuro
  %(prog)s contenido.py --list-configs     # Lista configuraciones disponibles
  
Configuraciones disponibles: educativo, ejecutivo, taller, evaluacion, dark
        """
    )
    
    parser.add_argument(
        "input_file",
        nargs="?",
        help="Archivo .py en formato percent de entrada"
    )
    parser.add_argument(
        "-o", "--output",
        help="Archivo .md de salida (por defecto: mismo nombre con extensión .md)"
    )
    parser.add_argument(
        "--config",
        choices=list_configs(),
        default="educativo",
        help="Configuración predefinida a usar (default: educativo)"
    )
    parser.add_argument(
        "--title",
        help="Título personalizado de la presentación"
    )
    parser.add_argument(
        "--list-configs",
        action="store_true",
        help="Lista todas las configuraciones disponibles y sale"
    )
    parser.add_argument(
        "--header",
        help="Header personalizado para todas las slides"
    )
    parser.add_argument(
        "--footer",
        help="Footer personalizado para todas las slides"
    )
    
    args = parser.parse_args()
    
    # Listar configuraciones si se solicita
    if args.list_configs:
        print("Configuraciones disponibles:")
        configs = list_configs()
        for config_name in configs:
            config = get_config(config_name)
            print(f"  {config_name:12} - {config.background_color} | {config.primary_color}")
        return 0
    
    # Validar que se proporcionó archivo de entrada
    if not args.input_file:
        parser.error("Se requiere un archivo de entrada (o usar --list-configs)")
    
    # Validar archivo de entrada
    input_path = Path(args.input_file)
    if not input_path.exists():
        print(f"❌ Error: El archivo {input_path} no existe.")
        return 1
    
    if input_path.suffix != '.py':
        print(f"⚠️  Advertencia: El archivo {input_path} no tiene extensión .py")
    
    # Determinar archivo de salida
    if args.output:
        output_path = Path(args.output)
    else:
        output_path = input_path.with_suffix('.md')
    
    # Leer contenido
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            py_content = f.read()
    except Exception as e:
        print(f"❌ Error leyendo {input_path}: {e}")
        return 1
    
    # Configurar presentación
    config = get_config(args.config)
    
    # Aplicar personalizaciones
    if args.header:
        config.header = args.header
    if args.footer:
        config.footer = args.footer
    
    # Convertir
    converter = PyToMarpConverter(config)
    
    # Generar título inteligente
    if args.title:
        title = args.title
    else:
        # Extraer de nombre de archivo o contenido
        title = input_path.stem.replace('-', ' ').replace('_', ' ').title()
        
        # Intentar extraer título del contenido
        title_match = py_content.find('# ')
        if title_match != -1:
            line_end = py_content.find('\n', title_match)
            potential_title = py_content[title_match+2:line_end].strip()
            if potential_title and len(potential_title) < 100:
                title = potential_title
    
    print(f"🔄 Convirtiendo {input_path.name} con configuración '{args.config}'...")
    marp_content = converter.convert_to_marp(py_content, title)
    
    # Escribir resultado
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(marp_content)
        
        slides_count = marp_content.count('---')
        print(f"✅ Presentación Marp generada: {output_path}")
        print(f"   📄 Slides: {slides_count}")
        print(f"   🎨 Configuración: {args.config}")
        print(f"   🎯 Tema: {config.primary_color} / {config.secondary_color}")
        print()
        print("Comandos útiles:")
        print(f"   👀 Visualizar: code {output_path}")
        print(f"   📱 Servidor Marp: marp -s {output_path}")
        print(f"   📄 Exportar PDF: marp {output_path} -o {output_path.with_suffix('.pdf')}")
        print(f"   🖼️  Exportar PNG: marp {output_path} --images png -o {output_path.stem}")
        
    except Exception as e:
        print(f"❌ Error escribiendo {output_path}: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
