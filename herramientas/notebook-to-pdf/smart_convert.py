#!/usr/bin/env python3
"""
Smart Notebook to PDF Converter

Convertidor inteligente que solo regenera PDFs cuando es necesario,
con estado detallado y verificación de timestamps.

Autor: Curso de Ciencia de Datos aplicada al Fútbol
Versión: 1.0.0
"""

import argparse
import sys
from pathlib import Path
from typing import List, Dict, Tuple, Optional
import time
import hashlib
import json
from convert import NotebookConverter


class SmartConverter(NotebookConverter):
    """Conversor inteligente con cache y estado."""
    
    def __init__(self, cache_file: str = '.conversion_cache.json'):
        super().__init__()
        self.cache_file = Path(cache_file)
        self.cache = self._load_cache()
    
    def _load_cache(self) -> Dict:
        """Carga el cache de conversiones previas."""
        if self.cache_file.exists():
            try:
                with open(self.cache_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                return {}
        return {}
    
    def _save_cache(self) -> None:
        """Guarda el cache de conversiones."""
        try:
            with open(self.cache_file, 'w', encoding='utf-8') as f:
                json.dump(self.cache, f, indent=2)
        except IOError:
            pass  # Continuar si no se puede guardar
    
    def _get_file_hash(self, path: Path) -> str:
        """Calcula hash del contenido del archivo."""
        try:
            with open(path, 'rb') as f:
                content = f.read()
            return hashlib.md5(content).hexdigest()
        except IOError:
            return ""
    
    def _needs_conversion(self, notebook_path: Path, 
                         pdf_path: Path, force: bool = False) -> Tuple[bool, str]:
        """Determina si es necesario convertir el notebook."""
        if force:
            return True, "Forzada"
        
        # Si no existe PDF, convertir
        if not pdf_path.exists():
            return True, "PDF no existe"
        
        # Verificar timestamps
        notebook_time = notebook_path.stat().st_mtime
        pdf_time = pdf_path.stat().st_mtime
        
        if notebook_time > pdf_time:
            return True, "Notebook más reciente"
        
        # Verificar hash en cache
        notebook_str = str(notebook_path.absolute())
        current_hash = self._get_file_hash(notebook_path)
        
        if notebook_str in self.cache:
            cached_info = self.cache[notebook_str]
            if cached_info.get('hash') != current_hash:
                return True, "Contenido modificado"
            if not pdf_path.exists():
                return True, "PDF eliminado"
        else:
            return True, "Primera conversión"
        
        return False, "Actualizado"
    
    def show_status(self, notebooks: List[Path], 
                   output_dir: Optional[Path] = None) -> None:
        """Muestra el estado de conversión de los notebooks."""
        print(f"Estado de conversión ({len(notebooks)} notebooks)")
        print("=" * 60)
        
        needs_conversion = []
        up_to_date = []
        
        for notebook in notebooks:
            if output_dir:
                pdf_path = output_dir / notebook.with_suffix('.pdf').name
            else:
                pdf_path = notebook.with_suffix('.pdf')
            
            needs_conv, reason = self._needs_conversion(notebook, pdf_path)
            
            status = "PENDIENTE" if needs_conv else "OK"
            size_info = ""
            
            if pdf_path.exists():
                size = pdf_path.stat().st_size // 1024
                mtime = time.strftime('%Y-%m-%d %H:%M', 
                                    time.localtime(pdf_path.stat().st_mtime))
                size_info = f" ({size}K, {mtime})"
            
            print(f"{status:>9} | {notebook.name:<40} | {reason}{size_info}")
            
            if needs_conv:
                needs_conversion.append(notebook)
            else:
                up_to_date.append(notebook)
        
        print("=" * 60)
        print(f"Necesitan conversión: {len(needs_conversion)}")
        print(f"Actualizados: {len(up_to_date)}")
    
    def smart_convert_batch(self, notebooks: List[Path],
                           output_dir: Optional[Path] = None,
                           engine: Optional[str] = None,
                           force: bool = False,
                           dry_run: bool = False) -> None:
        """Conversión inteligente por lotes."""
        if not notebooks:
            print("No se encontraron notebooks para convertir.")
            return
        
        # Determinar qué notebooks necesitan conversión
        to_convert = []
        for notebook in notebooks:
            if output_dir:
                pdf_path = output_dir / notebook.with_suffix('.pdf').name
                output_dir.mkdir(parents=True, exist_ok=True)
            else:
                pdf_path = notebook.with_suffix('.pdf')
            
            needs_conv, reason = self._needs_conversion(notebook, pdf_path, force)
            if needs_conv or dry_run:
                to_convert.append((notebook, pdf_path, reason))
        
        if not to_convert and not dry_run:
            print("Todos los PDFs están actualizados.")
            return
        
        print(f"Conversión inteligente: {len(to_convert)} notebooks")
        if dry_run:
            print("MODO DRY-RUN: No se realizarán conversiones reales")
        print("-" * 60)
        
        start_time = time.time()
        
        for i, (notebook, pdf_path, reason) in enumerate(to_convert, 1):
            success, message = self.convert_notebook(
                notebook, pdf_path, engine, dry_run
            )
            
            status = "✓" if success else "✗"
            print(f"[{i:2d}/{len(to_convert)}] {status} {message} ({reason})")
            
            # Actualizar cache si la conversión fue exitosa
            if success and not dry_run:
                notebook_str = str(notebook.absolute())
                self.cache[notebook_str] = {
                    'hash': self._get_file_hash(notebook),
                    'converted_at': time.time(),
                    'pdf_path': str(pdf_path)
                }
        
        # Guardar cache
        if not dry_run:
            self._save_cache()
        
        # Resumen
        elapsed = time.time() - start_time
        print("-" * 60)
        print(f"Completado en {elapsed:.1f}s")
        print(f"Convertidos: {self.converted_count}")
        print(f"Ya actualizados: {self.skipped_count}")
        print(f"Fallidos: {self.failed_count}")


def main():
    """Función principal del convertidor inteligente."""
    parser = argparse.ArgumentParser(
        description='Convertidor inteligente de notebooks a PDF',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos:
  %(prog)s contenido/                        # Conversión inteligente
  %(prog)s contenido/ --status               # Solo mostrar estado
  %(prog)s contenido/ --force                # Regenerar todo
  %(prog)s contenido/ --dry-run              # Ver qué se haría
  %(prog)s notebook.ipynb                    # Convertir archivo específico
        """)
    
    parser.add_argument('input',
                       help='Archivo .ipynb o directorio con notebooks')
    parser.add_argument('-o', '--output',
                       help='Directorio de salida (opcional)')
    parser.add_argument('--engine',
                       choices=['xelatex', 'pdflatex', 'lualatex'],
                       default='xelatex',
                       help='Motor LaTeX para PDF (default: xelatex)')
    parser.add_argument('--no-recursive', action='store_true',
                       help='No buscar recursivamente en subdirectorios')
    parser.add_argument('--force', action='store_true',
                       help='Regenerar todos los PDFs')
    parser.add_argument('--dry-run', action='store_true',
                       help='Mostrar qué se haría sin ejecutar')
    parser.add_argument('--status', action='store_true',
                       help='Solo mostrar estado sin convertir')
    parser.add_argument('--cache-file', default='.conversion_cache.json',
                       help='Archivo de cache (default: .conversion_cache.json)')
    
    args = parser.parse_args()
    
    # Crear conversor inteligente
    converter = SmartConverter(args.cache_file)
    
    # Verificar dependencias
    if not args.status:
        deps_ok, missing = converter.check_dependencies()
        if not deps_ok:
            print("Error: Dependencias faltantes:")
            for dep in missing:
                print(f"  - {dep}")
            print("\nInstala: sudo apt install pandoc texlive-xetex")
            sys.exit(1)
    
    # Parsear entrada
    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Error: No existe {input_path}")
        sys.exit(1)
    
    # Encontrar notebooks
    recursive = not args.no_recursive
    notebooks = converter.find_notebooks(input_path, recursive)
    
    if not notebooks:
        print(f"No se encontraron notebooks en {input_path}")
        sys.exit(1)
    
    # Directorio de salida
    output_dir = Path(args.output) if args.output else None
    
    try:
        if args.status:
            # Solo mostrar estado
            converter.show_status(notebooks, output_dir)
        else:
            # Conversión inteligente
            converter.smart_convert_batch(
                notebooks=notebooks,
                output_dir=output_dir,
                engine=args.engine,
                force=args.force,
                dry_run=args.dry_run
            )
    except KeyboardInterrupt:
        print("\nCancelado por el usuario")
        sys.exit(1)
    except Exception as e:
        print(f"Error inesperado: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
