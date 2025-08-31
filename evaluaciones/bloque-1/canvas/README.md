# Banco de Preguntas - Bloque 1 (Canvas)

Este directorio contiene el banco de preguntas específico para el Bloque 1 del curso, listo para ser convertido a formato QTI para Canvas LMS.

## 📄 Archivos

- `banco-preguntas-bloque1.txt` - Banco de 25 preguntas del Bloque 1
- `generar_qti.py` - Script local para regenerar QTI automáticamente
- `banco-preguntas-bloque1_kansas.csv` - Archivo CSV generado 
- `banco-preguntas-bloque1_canvas_qti.zip` - Paquete QTI listo para Canvas
- `README.md` - Esta documentación

## 📚 Contenido del Banco

**25 preguntas distribuidas en 5 semanas:**

- **Q1-Q5**: Semana 1 - Configuración y Fundamentos de Python
- **Q6-Q10**: Semana 2 - Estructuras de Control  
- **Q11-Q15**: Semana 3 - Funciones y Módulos
- **Q16-Q20**: Semana 4 - Pandas y NumPy Introducción
- **Q21-Q25**: Semana 5 - Visualización Básica

## 🔄 Regenerar Archivos QTI

### Opción 1: Script Local (Recomendado)
```bash
# Desde este directorio (evaluaciones/bloque-1/canvas/)
python generar_qti.py
```

Este script:
- ✅ Detecta automáticamente si hay cambios en el archivo TXT
- ✅ Regenera solo si es necesario
- ✅ Muestra el estado de todos los archivos
- ✅ Fuerza regeneración con `--force`

### Opción 2: Herramienta txttoqti (Recomendado)
```bash
# Desde cualquier directorio - usando la librería txttoqti
txt-to-qti evaluaciones/bloque-1/canvas/banco-preguntas-bloque1.txt

# Ver estado de archivos
txt-to-qti --status evaluaciones/bloque-1/canvas/banco-preguntas-bloque1.txt

# Forzar regeneración
txt-to-qti evaluaciones/bloque-1/canvas/banco-preguntas-bloque1.txt --force
```

### Opción 3: API de Python
```python
# Usar la API directamente en scripts
from txttoqti import convert_txt_to_qti
qti_file = convert_txt_to_qti('banco-preguntas-bloque1.txt')
print(f'QTI generado: {qti_file}')
```

## 📋 Importar a Canvas

1. **Archivo listo**: `banco-preguntas-bloque1_canvas_qti.zip`
2. **En Canvas**:
   - Ir a Configuración → Importar contenido del curso
   - Seleccionar "Paquete QTI"
   - Subir el archivo ZIP
   - Las 25 preguntas aparecerán en el banco de preguntas

## ✏️ Modificar Preguntas

1. **Editar**: Modifica `banco-preguntas-bloque1.txt`
2. **Regenerar**: Usa la herramienta de conversión
3. **Importar**: Sube el nuevo ZIP a Canvas

## 🔗 Herramientas de Conversión

La librería txttoqti proporciona conversión TXT→QTI:
```
txttoqti/
├── __init__.py           # API principal y funciones de conveniencia
├── parser.py             # Análisis de archivos de texto
├── validator.py          # Validación de preguntas
├── qti_generator.py      # Generación de XML QTI
├── smart_converter.py    # Conversión inteligente con detección de cambios
├── cli.py                # Interfaz de línea de comandos
└── tests/                # Suite de tests completa
```

La librería txttoqti es independiente y puede instalarse como paquete Python.

## 📊 Especificaciones Técnicas

- **Formato entrada**: Texto plano simple
- **Formato QTI**: 1.2 (máxima compatibilidad Canvas)
- **Encoding**: ISO-8859-1 (estándar Canvas)
- **Tipo preguntas**: Opción múltiple (2-4 opciones)
- **Puntuación**: 1.0 punto por pregunta

## 🧪 Validación

Para validar el banco de preguntas:

```bash
# Validar usando txttoqti
txt-to-qti --validate evaluaciones/bloque-1/canvas/banco-preguntas-bloque1.txt

# Ejecutar tests de la librería
python txttoqti/tests/test_core.py
```

## 📈 Historial de Versiones

- **v1.0**: Banco inicial de 50 preguntas
- **v2.0**: Reducido a 25 preguntas (5 por semana)
- **v2.1**: Separación de herramientas y contenido