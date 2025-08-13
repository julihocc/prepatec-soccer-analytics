#!/usr/bin/env python3
"""
Convertidor de archivos py:percent a Markdown compatible con Marp.

Convierte archivos .py en formato percent a presentaciones Marp con estilos
configurables para contenido educativo de ciencia de datos aplicada al fútbol.
"""

import re
import argparse
import os
from pathlib import Path
from typing import List, Dict, Optional
from dataclasses import dataclass


@dataclass
class MarpConfig:
    """Configuración para la presentación Marp."""
    theme: str = "default"
    size: str = "16:9"
    paginate: bool = True
    header: Optional[str] = None
    footer: Optional[str] = None
    class_: Optional[str] = None
    background_color: str = "#ffffff"
    text_color: str = "#333333"
    primary_color: str = "#1e88e5"
    secondary_color: str = "#43a047"


class PyToMarpConverter:
    """Convertidor principal de py:percent a Marp."""
    
    def __init__(self, config: Optional[MarpConfig] = None):
        self.config = config or MarpConfig()
        self.slide_count = 0
        
    def extract_cells_from_py(self, content: str) -> List[Dict[str, str]]:
        """Extrae las celdas de un archivo py:percent."""
        cells = []
        
        # Patrones para detectar celdas
        markdown_pattern = r"# %% \[markdown\]\s*\n(.*?)(?=# %%|\Z)"
        code_pattern = r"# %%(?!\s*\[markdown\])\s*\n(.*?)(?=# %%|\Z)"
        
        # Encontrar todas las celdas markdown
        for match in re.finditer(markdown_pattern, content, re.DOTALL):
            cell_content = match.group(1).strip()
            # Limpiar comentarios de Python en markdown
            cell_content = re.sub(r'^# """\s*\n', '', cell_content, flags=re.MULTILINE)
            cell_content = re.sub(r'\n# """\s*$', '', cell_content, flags=re.MULTILINE)
            cell_content = re.sub(r'^# ', '', cell_content, flags=re.MULTILINE)
            
            cells.append({
                'type': 'markdown',
                'content': cell_content
            })
        
        # Encontrar todas las celdas de código
        for match in re.finditer(code_pattern, content, re.DOTALL):
            cell_content = match.group(1).strip()
            cells.append({
                'type': 'code',
                'content': cell_content
            })
        
        return cells
    
    def generate_marp_header(self) -> str:
        """Genera el header YAML de Marp."""
        header_lines = [
            "---",
            "marp: true",
            f"theme: {self.config.theme}",
            f"size: {self.config.size}",
            f"paginate: {self.config.paginate}".lower(),
            f"backgroundColor: {self.config.background_color}",
            f"color: {self.config.text_color}"
        ]
        
        if self.config.header:
            header_lines.append(f"header: '{self.config.header}'")
        
        if self.config.footer:
            header_lines.append(f"footer: '{self.config.footer}'")
            
        if self.config.class_:
            header_lines.append(f"class: {self.config.class_}")
        
        header_lines.extend([
            "style: |",
            "  h1 { color: " + self.config.primary_color + "; }",
            "  h2 { color: " + self.config.secondary_color + "; }",
            "  .highlight { background-color: #fff3cd; padding: 10px; border-radius: 5px; }",
            "  .question { background-color: #d1ecf1; padding: 15px; border-radius: 5px; border-left: 4px solid " + self.config.primary_color + "; }",
            "  .code-small { font-size: 0.8em; }",
            "  .center { text-align: center; }",
            "---",
            ""
        ])
        
        return "\n".join(header_lines)
    
    def is_new_slide_marker(self, content: str) -> bool:
        """Determina si el contenido marca el inicio de un nuevo slide."""
        # Nuevos slides en:
        # - Títulos de sesión (## SESIÓN)
        # - Títulos principales (# )
        # - Subtítulos importantes (## que no sean SESIÓN)
        patterns = [
            r'^# [^#]',  # Título principal
            r'^## SESIÓN',  # Título de sesión
            r'^## ¿.*\?',  # Preguntas principales
        ]
        
        for pattern in patterns:
            if re.match(pattern, content.strip(), re.MULTILINE):
                return True
        return False
    
    def format_code_cell(self, content: str) -> str:
        """Formatea una celda de código para Marp."""
        # Añadir syntax highlighting y estilo
        return f"```python\n{content}\n```"
    
    def format_markdown_cell(self, content: str) -> str:
        """Formatea una celda markdown para Marp."""
        # Convertir preguntas en cajas destacadas
        content = re.sub(
            r'(\*\*Pregunta[^:]*\*\*:.*?)(?=\n\n|\n\*\*|\Z)',
            r'<div class="question">\n\n\1\n\n</div>',
            content,
            flags=re.DOTALL
        )
        
        # Destacar contenido importante
        content = re.sub(
            r'(\*\*[^*]+\*\*)',
            r'<span class="highlight">\1</span>',
            content
        )
        
        return content
    
    def convert_to_marp(self, py_content: str, title: str = "Presentación") -> str:
        """Convierte contenido py:percent a Markdown Marp."""
        cells = self.extract_cells_from_py(py_content)
        
        if not cells:
            return self.generate_marp_header() + f"# {title}\n\nNo se encontró contenido válido."
        
        marp_content = [self.generate_marp_header()]
        
        # Slide de título
        if cells and cells[0]['type'] == 'markdown':
            first_cell = cells[0]['content']
            # Extraer título principal
            title_match = re.search(r'^# (.+)', first_cell, re.MULTILINE)
            if title_match:
                title = title_match.group(1)
                marp_content.append(f"# {title}")
                marp_content.append("")
                marp_content.append('<div class="center">')
                marp_content.append("")
                marp_content.append("**Ciencia de Datos aplicada al Fútbol**")
                marp_content.append("")
                marp_content.append("*Preparatoria / Bachillerato*")
                marp_content.append("")
                marp_content.append("</div>")
                marp_content.append("")
                marp_content.append("---")
                marp_content.append("")
                cells = cells[1:]  # Remover la primera celda ya procesada
        
        current_slide = []
        
        for cell in cells:
            if cell['type'] == 'markdown':
                formatted_content = self.format_markdown_cell(cell['content'])
                
                # Si es marcador de nuevo slide, finalizar slide actual
                if self.is_new_slide_marker(cell['content']) and current_slide:
                    marp_content.extend(current_slide)
                    marp_content.append("---")
                    marp_content.append("")
                    current_slide = []
                
                current_slide.append(formatted_content)
                
            elif cell['type'] == 'code':
                formatted_code = self.format_code_cell(cell['content'])
                current_slide.append(formatted_code)
            
            current_slide.append("")
        
        # Añadir último slide
        if current_slide:
            marp_content.extend(current_slide)
        
        return "\n".join(marp_content)


def get_educational_config() -> MarpConfig:
    """Configuración predeterminada para contenido educativo."""
    return MarpConfig(
        theme="default",
        size="16:9",
        paginate=True,
        footer="Ciencia de Datos aplicada al Fútbol | Preparatoria",
        background_color="#ffffff",
        text_color="#2c3e50",
        primary_color="#3498db",
        secondary_color="#e74c3c"
    )


def main():
    """Función principal."""
    parser = argparse.ArgumentParser(
        description="Convierte archivos py:percent a presentaciones Marp"
    )
    parser.add_argument(
        "input_file",
        help="Archivo .py en formato percent de entrada"
    )
    parser.add_argument(
        "-o", "--output",
        help="Archivo .md de salida (por defecto: mismo nombre con extensión .md)"
    )
    parser.add_argument(
        "--theme",
        default="default",
        help="Tema de Marp a usar"
    )
    parser.add_argument(
        "--title",
        help="Título de la presentación"
    )
    
    args = parser.parse_args()
    
    # Validar archivo de entrada
    input_path = Path(args.input_file)
    if not input_path.exists():
        print(f"Error: El archivo {input_path} no existe.")
        return 1
    
    if not input_path.suffix == '.py':
        print(f"Advertencia: El archivo {input_path} no tiene extensión .py")
    
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
        print(f"Error leyendo {input_path}: {e}")
        return 1
    
    # Configurar y convertir
    config = get_educational_config()
    config.theme = args.theme
    
    converter = PyToMarpConverter(config)
    
    title = args.title or input_path.stem.replace('-', ' ').title()
    marp_content = converter.convert_to_marp(py_content, title)
    
    # Escribir resultado
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(marp_content)
        print(f"✅ Presentación Marp generada: {output_path}")
        print(f"   Slides aproximados: {marp_content.count('---')}")
        print(f"   Para visualizar: code {output_path}")
        print(f"   Para exportar: marp {output_path} -o {output_path.with_suffix('.pdf')}")
    except Exception as e:
        print(f"Error escribiendo {output_path}: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())
