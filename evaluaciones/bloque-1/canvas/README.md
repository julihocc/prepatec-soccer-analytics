# Banco de Preguntas - Bloque 1 (Canvas)

Este directorio contiene el banco de preguntas específico para el Bloque 1 del curso, listo para ser convertido a formato QTI para Canvas LMS.

## 📄 Archivos

- `banco-preguntas-bloque1.txt` - Banco de 25 preguntas del Bloque 1
- `banco-preguntas-bloque1_kansas.csv` - Archivo CSV generado 
- `banco-preguntas-bloque1_kansas_kansas_qti.zip` - Paquete QTI listo para Canvas
- `README.md` - Esta documentación

## 📚 Contenido del Banco

**25 preguntas distribuidas en 5 semanas:**

- **Q1-Q5**: Semana 1 - Configuración y Fundamentos de Python
- **Q6-Q10**: Semana 2 - Estructuras de Control  
- **Q11-Q15**: Semana 3 - Funciones y Módulos
- **Q16-Q20**: Semana 4 - Pandas y NumPy Introducción
- **Q21-Q25**: Semana 5 - Visualización Básica

## 🔄 Regenerar Archivos QTI

Para actualizar o regenerar los archivos QTI, usa la herramienta de conversión:

### Opción 1: Script Todo-en-Uno (Recomendado)
```bash
# Desde el directorio raíz del proyecto
python herramientas/txt-to-qti/convert.py evaluaciones/bloque-1/canvas/banco-preguntas-bloque1.txt
```

### Opción 2: Por Etapas
```bash
# Paso 1: TXT → CSV
python herramientas/txt-to-qti/txt_to_csv_direct.py banco-preguntas-bloque1.txt

# Paso 2: CSV → QTI  
python herramientas/txt-to-qti/csv_to_kansas_qti.py banco-preguntas-bloque1_kansas.csv
```

## 📋 Importar a Canvas

1. **Archivo listo**: `banco-preguntas-bloque1_kansas_kansas_qti.zip`
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

Las herramientas de conversión TXT→QTI están en:
```
herramientas/txt-to-qti/
├── convert.py              # Script principal todo-en-uno
├── txt_to_csv_direct.py   # Convertidor TXT→CSV
├── csv_to_kansas_qti.py   # Generador CSV→QTI
├── tests/                 # Suite de tests
└── *.md                   # Documentación técnica
```

Ver [herramientas/txt-to-qti/README.md](../../herramientas/txt-to-qti/README.md) para documentación completa de las herramientas.

## 📊 Especificaciones Técnicas

- **Formato entrada**: Texto plano simple
- **Formato QTI**: 1.2 (máxima compatibilidad Canvas)
- **Encoding**: ISO-8859-1 (estándar Canvas)
- **Tipo preguntas**: Opción múltiple (2-4 opciones)
- **Puntuación**: 1.0 punto por pregunta

## 🧪 Validación

Para validar el banco de preguntas:

```bash
# Validar formato y estructura
python herramientas/txt-to-qti/tests/run_tests.py --validate

# Ejecutar todos los tests
python herramientas/txt-to-qti/tests/run_tests.py
```

## 📈 Historial de Versiones

- **v1.0**: Banco inicial de 50 preguntas
- **v2.0**: Reducido a 25 preguntas (5 por semana)
- **v2.1**: Separación de herramientas y contenido