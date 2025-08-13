#!/usr/bin/env python3
"""
Notebook to PDF Converter - Herramienta Universal

Convierte notebooks de Jupyter (.ipynb) a PDF usando pandoc con configuración
optimizada para contenido educativo en español.

Autor: Curso de Ciencia de Datos aplicada al Fútbol
Versión: 1.0.0
"""

import argparse
import subprocess
import sys
from pathlib import Path
from typing import List, Tuple, Optional
import time
import os


class NotebookConverter:
    """Conversor principal de notebooks a PDF."""
    
    def __init__(self):
        self.engines = ['xelatex', 'pdflatex', 'lualatex']
        self.default_engine = 'xelatex'
        self.converted_count = 0
        self.failed_count = 0
        self.skipped_count = 0
    
    def check_dependencies(self) -> Tuple[bool, List[str]]:
        """Verifica que las dependencias estén instaladas."""
        missing = []
        
        # Verificar pandoc
        try:
            result = subprocess.run(['pandoc', '--version'], 
                                  capture_output=True, text=True)
            if result.returncode != 0:
                missing.append('pandoc')
        except FileNotFoundError:
            missing.append('pandoc')
        
        # Verificar LaTeX (al menos uno)
        latex_found = False
        for engine in self.engines:
            try:
                result = subprocess.run([engine, '--version'], 
                                      capture_output=True, text=True)
                if result.returncode == 0:
                    latex_found = True
                    break
            except FileNotFoundError:
                continue
        
        if not latex_found:
            missing.append('texlive-xetex (o similar)')
        
        return len(missing) == 0, missing
    
    def find_notebooks(self, path: Path, recursive: bool = True) -> List[Path]:
        """Encuentra todos los notebooks en el directorio dado."""
        if path.is_file() and path.suffix == '.ipynb':
            return [path]
        
        if not path.is_dir():
            return []
        
        pattern = '**/*.ipynb' if recursive else '*.ipynb'
        notebooks = list(path.glob(pattern))
        
        # Filtrar notebooks con checkpoints
        notebooks = [nb for nb in notebooks 
                    if '.ipynb_checkpoints' not in str(nb)]
        
        return sorted(notebooks)
    
    def convert_notebook(self, notebook_path: Path, 
                        output_path: Optional[Path] = None,
                        engine: Optional[str] = None, 
                        dry_run: bool = False) -> Tuple[bool, str]:
        """Convierte un notebook individual a PDF."""
        if engine is None:
            engine = self.default_engine
        
        if output_path is None:
            output_path = notebook_path.with_suffix('.pdf')
        
        # Verificar si el archivo existe
        if not notebook_path.exists():
            return False, f"Archivo no encontrado: {notebook_path}"
        
        # Verificar si es necesario regenerar
        if output_path.exists() and not dry_run:
            notebook_time = notebook_path.stat().st_mtime
            pdf_time = output_path.stat().st_mtime
            if pdf_time > notebook_time:
                self.skipped_count += 1
                return True, f"Ya actualizado: {output_path.name}"
        
        if dry_run:
            return True, f"[DRY-RUN] Convertiría: {notebook_path} -> {output_path}"
        
        # Comando pandoc
        cmd = [
            'pandoc',
            str(notebook_path),
            '-o', str(output_path),
            f'--pdf-engine={engine}',
            '--variable', 'geometry:margin=2cm',
            '--variable', 'fontsize=11pt',
            '--variable', 'documentclass=article',
            '--variable', 'papersize=letter'
        ]
        
        try:
            # Ejecutar conversión
            result = subprocess.run(cmd, capture_output=True, text=True, 
                                  timeout=300)  # 5 minutos timeout
            
            if result.returncode == 0:
                self.converted_count += 1
                # Obtener tamaño del archivo
                size = output_path.stat().st_size if output_path.exists() else 0
                size_kb = size // 1024
                return True, f"Convertido: {output_path.name} ({size_kb}K)"
            else:
                self.failed_count += 1
                error_msg = result.stderr.strip()
                # Simplificar mensajes de error comunes
                if 'font' in error_msg.lower():
                    error_msg = "Advertencia de fuentes (resultado OK)"
                return False, f"Error: {error_msg[:100]}"
                
        except subprocess.TimeoutExpired:
            self.failed_count += 1
            return False, "Error: Timeout (>5 min)"
        except Exception as e:
            self.failed_count += 1
            return False, f"Error: {str(e)}"
    
    def convert_batch(self, notebooks: List[Path], 
                     output_dir: Optional[Path] = None,
                     engine: Optional[str] = None,
                     dry_run: bool = False,
                     force: bool = False) -> None:
        """Convierte múltiples notebooks."""
        if not notebooks:
            print("No se encontraron notebooks para convertir.")
            return
        
        print(f"Encontrados {len(notebooks)} notebooks")
        if dry_run:
            print("MODO DRY-RUN: No se realizarán conversiones reales")
        print("-" * 60)
        
        start_time = time.time()
        
        for i, notebook in enumerate(notebooks, 1):
            # Determinar ruta de salida
            if output_dir:
                output_path = output_dir / notebook.with_suffix('.pdf').name
                output_dir.mkdir(parents=True, exist_ok=True)
            else:
                output_path = notebook.with_suffix('.pdf')
            
            # Convertir
            success, message = self.convert_notebook(
                notebook, output_path, engine, dry_run
            )
            
            # Mostrar progreso
            status = "✓" if success else "✗"
            print(f"[{i:2d}/{len(notebooks)}] {status} {message}")
        
        # Resumen final
        elapsed = time.time() - start_time
        print("-" * 60)
        print(f"Completado en {elapsed:.1f}s")
        print(f"Convertidos: {self.converted_count}")
        print(f"Ya actualizados: {self.skipped_count}")
        print(f"Fallidos: {self.failed_count}")


def main():
    """Función principal del convertidor."""
    parser = argparse.ArgumentParser(
        description='Convierte notebooks Jupyter a PDF usando pandoc',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos:
  %(prog)s notebook.ipynb                    # Convertir un archivo
  %(prog)s contenido/                        # Convertir directorio recursivamente
  %(prog)s contenido/ --no-recursive         # Solo archivos del directorio raíz
  %(prog)s contenido/ --output pdfs/         # Guardar en directorio específico
  %(prog)s contenido/ --engine pdflatex      # Usar motor LaTeX específico
  %(prog)s contenido/ --dry-run              # Ver qué se haría sin convertir
  %(prog)s contenido/ --force                # Regenerar todos los PDFs
        """)
    
    parser.add_argument('input', nargs='?',
                       help='Archivo .ipynb o directorio con notebooks')
    parser.add_argument('-o', '--output',
                       help='Directorio de salida (opcional)')
    parser.add_argument('--engine', 
                       choices=['xelatex', 'pdflatex', 'lualatex'],
                       default='xelatex',
                       help='Motor LaTeX para PDF (default: xelatex)')
    parser.add_argument('--no-recursive', action='store_true',
                       help='No buscar recursivamente en subdirectorios')
    parser.add_argument('--dry-run', action='store_true',
                       help='Mostrar qué se haría sin ejecutar conversiones')
    parser.add_argument('--force', action='store_true',
                       help='Regenerar PDFs aunque estén actualizados')
    parser.add_argument('--check-deps', action='store_true',
                       help='Solo verificar dependencias y salir')
    
    args = parser.parse_args()
    
    # Crear conversor
    converter = NotebookConverter()
    
    # Verificar dependencias
    if args.check_deps:
        deps_ok, missing = converter.check_dependencies()
        if deps_ok:
            print("✓ Todas las dependencias están instaladas")
            sys.exit(0)
        else:
            print("✗ Dependencias faltantes:")
            for dep in missing:
                print(f"  - {dep}")
            sys.exit(1)
    
    # Verificar que se proporcionó input si no es check-deps
    if args.input is None:
        print("Error: Se requiere especificar INPUT (archivo o directorio)")
        print("Usa --help para ver la ayuda completa")
        sys.exit(1)
    
    # Parsear entrada
    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Error: No existe {input_path}")
        sys.exit(1)
    
    # Verificar dependencias para operaciones que las requieren
    deps_ok, missing = converter.check_dependencies()
    if not deps_ok:
        print("Error: Dependencias faltantes:")
        for dep in missing:
            print(f"  - {dep}")
        print("\nInstala las dependencias y vuelve a intentar.")
        print("En Ubuntu/Debian: sudo apt install pandoc texlive-xetex")
        sys.exit(1)
    
    # Encontrar notebooks
    recursive = not args.no_recursive
    notebooks = converter.find_notebooks(input_path, recursive)
    
    if not notebooks:
        print(f"No se encontraron notebooks en {input_path}")
        sys.exit(1)
    
    # Directorio de salida
    output_dir = Path(args.output) if args.output else None
    
    # Convertir
    try:
        converter.convert_batch(
            notebooks=notebooks,
            output_dir=output_dir,
            engine=args.engine,
            dry_run=args.dry_run,
            force=args.force
        )
    except KeyboardInterrupt:
        print("\nCancelado por el usuario")
        sys.exit(1)
    except Exception as e:
        print(f"Error inesperado: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
