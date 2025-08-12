# TXT to QTI Converter - Herramienta Universal

Esta herramienta convierte bancos de preguntas en formato de texto simple a paquetes QTI compatibles con Canvas LMS. Permite a educadores crear exámenes en el formato más simple posible y desplegarlos directamente en Canvas.

## Descripción

Herramienta universal para convertir preguntas de texto plano a formato QTI de Canvas. Ideal para educadores que quieren crear exámenes sin complicaciones técnicas.

## Uso Rápido

### Smart Converter (Recomendado)
```bash
python smart_convert.py preguntas.txt
```

**Características inteligentes:**
- Solo regenera si hay cambios reales
- Muestra estado detallado con timestamps  
- Ejecutable desde cualquier directorio
- Opciones de forzado y solo-estado

### Script Todo-en-Uno Clásico
```bash
python convert.py preguntas.txt
python convert.py preguntas.txt --smart  # Con verificación de timestamps
```

### Uso por Etapas
```bash
# Paso 1: TXT -> CSV
python txt_to_csv_direct.py preguntas.txt

# Paso 2: CSV -> QTI
python csv_to_kansas_qti.py preguntas_kansas.csv
```

## Archivos de la Herramienta

### Scripts Principales
- `smart_convert.py` - **Convertidor inteligente** (recomendado)
- `convert.py` - Convertidor todo-en-uno clásico
- `txt_to_csv_direct.py` - Convertidor texto -> CSV
- `csv_to_kansas_qti.py` - Generador CSV -> QTI

### Documentación
- `README.md` - Esta guía
- `USAGE_GUIDE.md` - Guía detallada de uso
- `MARKDOWN_FORMAT.md` - Especificación del formato de texto
- `TECHNICAL_DETAILS.md` - Detalles técnicos de implementación
- `SOURCES_AND_REFERENCES.md` - Referencias y fuentes

### Tests
- `tests/` - Suite completa de tests
- `tests/run_tests.py` - Ejecutor de tests

## Formato de Preguntas

Crea un archivo `.txt` con este formato simple:

```
Q1: ¿Cuál es la capital de Francia?
A) Londres
B) París
C) Madrid
D) Roma
RESPUESTA: B

Q2: ¿Cuánto es 2 + 2?
A) 3
B) 4
C) 5
RESPUESTA: B
```

### Reglas del Formato
- Preguntas numeradas secuencialmente (Q1, Q2, Q3...)
- Mínimo 2 opciones (A, B), máximo 4 (A, B, C, D)
- Una respuesta correcta con `RESPUESTA: [letra]`
- Líneas en blanco separan preguntas (opcional)

## Importar a Canvas

1. **Ejecutar conversión**:
   ```bash
   python convert.py mis_preguntas.txt
   ```

2. **En Canvas**:
   - Ir a Configuración -> Importar contenido del curso
   - Seleccionar "Paquete QTI"
   - Subir el archivo ZIP generado
   - ¡Las preguntas aparecen en tu banco!

## Instalación

### Requisitos
- Python 3.7 o superior
- Solo librerías estándar (sin instalaciones adicionales)

### Descargar
```bash
# Clonar repositorio completo
git clone [url-repositorio]
cd herramientas/txt-to-qti

# O descargar solo esta carpeta
```

## Ejecutar Tests

```bash
# Todos los tests
python tests/run_tests.py

# Test específico  
python tests/run_tests.py test_txt_to_csv

# Validar entorno
python tests/run_tests.py --validate
```

## Características

### Lo que hace bien
- **Ultra simple**: Solo texto plano, sin formato complejo
- **Rápido**: Convierte 100 preguntas en segundos
- **Confiable**: Compatible con Canvas usando formato Kansas State probado
- **Validación**: Detecta errores automáticamente
- **Portable**: Solo Python estándar, sin dependencias

### Ideal para
- Profesores creando exámenes rápidos
- Bancos de preguntas institucionales
- Conversión masiva de preguntas existentes
- Integración en sistemas automatizados

### Características técnicas
- Formato QTI 1.2 (máxima compatibilidad Canvas)
- Encoding ISO-8859-1 (estándar Canvas)
- IDs reproducibles con hash MD5
- Validación automática de estructura
- Tests comprensivos incluidos

## Resolución de Problemas

### Error: "Sin respuesta correcta"
- Verifica que cada pregunta tenga `RESPUESTA: A` (o B, C, D)
- Revisa que no falte el `:` después de RESPUESTA

### Error: "Numeración no secuencial"  
- Las preguntas deben ser Q1, Q2, Q3... sin saltos
- Renumera si hay huecos

### Error de caracteres especiales
- Evita símbolos raros que no se mapean a ISO-8859-1
- Usa acentos normales (á, é, í, ó, ú, ñ) que sí funcionan

### Canvas no acepta el ZIP
- Verifica que subiste el archivo .zip (no el .xml interno)
- Asegúrate de seleccionar "Paquete QTI" en Canvas

## Ejemplos de Uso

### Uso Inteligente (Recomendado)
```bash
# Archivo: examen_matematicas.txt
Q1: ¿Cuánto es 5 x 3?
A) 12
B) 15  
C) 18
RESPUESTA: B

# Convertir inteligentemente
python smart_convert.py examen_matematicas.txt

# Solo muestra estado sin convertir
python smart_convert.py --status examen_matematicas.txt

# Forzar regeneración
python smart_convert.py examen_matematicas.txt --force
```

### Uso Clásico
```bash
# Conversión normal
python convert.py examen_matematicas.txt

# Con verificación de timestamps
python convert.py examen_matematicas.txt --smart

# Con nombre personalizado
python convert.py preguntas.txt mi_examen_final.zip
```

### Procesamiento por Lotes
```bash
# Conversión inteligente de múltiples archivos
for archivo in *.txt; do
    python smart_convert.py "$archivo"
done

# Conversión clásica
for archivo in *.txt; do
    python convert.py "$archivo"
done
```

## Documentación Adicional

- **[USAGE_GUIDE.md](USAGE_GUIDE.md)** - Guía completa con ejemplos
- **[TECHNICAL_DETAILS.md](TECHNICAL_DETAILS.md)** - Implementación técnica
- **[tests/README_TESTS.md](tests/README_TESTS.md)** - Documentación de tests

## Contribuir

### Reportar Problemas
1. Ejecutar tests: `python tests/run_tests.py`
2. Crear ejemplo mínimo que reproduzca el problema
3. Incluir mensaje de error completo

### Agregar Funcionalidad
1. Escribir tests primero
2. Implementar funcionalidad
3. Verificar que todos los tests pasen
4. Actualizar documentación

## Licencia

Herramienta educativa basada en estándares públicos:
- Especificación QTI: IMS Global (implementable libremente)
- Metodología Kansas State: Dominio público educativo
- Implementación: Uso educativo libre

## Arquitectura

```
TXT File -> [txt_to_csv_direct.py] -> CSV -> [csv_to_kansas_qti.py] -> QTI ZIP
    ↓                                ↓                              ↓
Texto simple              Formato Kansas State            Canvas-ready
```

La herramienta usa un pipeline de dos etapas para máxima confiabilidad y debugging sencillo.

## Rendimiento

- **Pequeño** (1-25 preguntas): < 1 segundo
- **Mediano** (26-100 preguntas): 1-3 segundos  
- **Grande** (100+ preguntas): 3-10 segundos

Tested con bancos de hasta 1000 preguntas exitosamente.