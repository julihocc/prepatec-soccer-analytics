# Tests para el Convertidor TXT→CSV→QTI

Esta suite de tests asegura que el convertidor funcione correctamente y detecta regresiones cuando se modifica el código.

## Estructura de Tests

### **Archivos de Test**

- `test_txt_to_csv.py` - Tests unitarios para el convertidor TXT→CSV
- `test_csv_to_qti.py` - Tests unitarios para el generador CSV→QTI  
- `test_integration.py` - Tests de integración del pipeline completo
- `run_tests.py` - Runner principal para ejecutar todos los tests

### **Datos de Test**

- `test_questions_valid.txt` - Preguntas válidas para tests positivos
- `test_questions_invalid.txt` - Preguntas inválidas para tests de validación
- `test_questions_edge_cases.txt` - Casos especiales y edge cases

## Ejecutar Tests

### **Todos los tests**
```bash
python tests/run_tests.py
```

### **Test específico**
```bash
# Módulo completo
python tests/run_tests.py test_txt_to_csv

# Clase específica
python tests/run_tests.py test_txt_to_csv.TestTxtToCSVConverter

# Test individual
python tests/run_tests.py test_integration.TestFullPipeline.test_complete_pipeline_valid_questions
```

### **Validar entorno**
```bash
python tests/run_tests.py --validate
```

### **Ayuda**
```bash
python tests/run_tests.py --help
```

## Cobertura de Tests

### **Tests Unitarios - TXT→CSV** (`test_txt_to_csv.py`)

**Funcionalidad básica:**
- ✅ Parsing de preguntas válidas
- ✅ Validación de preguntas inválidas
- ✅ Mapeo de respuestas (A→1, B→2, etc.)
- ✅ Limpieza de texto
- ✅ Generación de filas CSV

**Validaciones:**
- ✅ Numeración secuencial
- ✅ Mínimo 2 opciones por pregunta
- ✅ Respuestas correctas válidas
- ✅ Detección de problemas

**Casos especiales:**
- ✅ Preguntas con 2-4 opciones
- ✅ Caracteres especiales
- ✅ Archivos vacíos
- ✅ Archivos inexistentes

### **Tests Unitarios - CSV→QTI** (`test_csv_to_qti.py`)

**Generación QTI:**
- ✅ Creación de items QTI válidos
- ✅ Estructura de assessment
- ✅ Metadatos Canvas-específicos
- ✅ Formateo XML estilo Kansas State

**Cumplimiento QTI:**
- ✅ Namespaces correctos
- ✅ IDs únicos y reproducibles
- ✅ Procesamiento de respuestas
- ✅ Encoding ISO-8859-1

**Manejo de errores:**
- ✅ Archivos CSV inexistentes
- ✅ CSV vacío o mal formateado
- ✅ Validación de estructura

### **Tests de Integración** (`test_integration.py`)

**Pipeline completo:**
- ✅ TXT → CSV → QTI funcional
- ✅ Preservación de datos a través del pipeline
- ✅ Validación del QTI final

**Casos reales:**
- ✅ Banco de preguntas del proyecto (25 preguntas)
- ✅ Caracteres especiales y acentos
- ✅ Preguntas con comillas y comas

**Rendimiento:**
- ✅ Test con 100 preguntas
- ✅ Tiempo de procesamiento < 10 segundos
- ✅ Uso eficiente de memoria

## Tipos de Validación

### **1. Validaciones de Entrada**
- Formato de archivo TXT correcto
- Numeración secuencial de preguntas
- Presencia de respuestas correctas
- Mínimo de opciones por pregunta

### **2. Validaciones de Procesamiento**
- Conversión correcta TXT→CSV
- Mapeo de respuestas A/B/C/D → 1/2/3/4
- Limpieza y normalización de texto
- Generación de filas CSV válidas

### **3. Validaciones de Salida**
- Estructura QTI 1.2 válida
- Namespaces y metadatos correctos
- Encoding ISO-8859-1 apropiado
- ZIP bien formado con XML único

### **4. Validaciones de Integración**
- Pipeline completo funcional
- Consistencia de datos extremo-a-extremo
- Manejo correcto de caracteres especiales
- Compatibilidad con Canvas LMS

## Casos de Test Cubiertos

### **Casos Positivos**
- ✅ Preguntas con 2, 3, y 4 opciones
- ✅ Respuestas A, B, C, D
- ✅ Caracteres acentuados (á, é, í, ó, ú, ñ)
- ✅ Comillas simples y dobles
- ✅ Símbolos matemáticos básicos
- ✅ Comas en texto de preguntas

### **Casos Negativos**
- ✅ Preguntas sin respuesta
- ✅ Preguntas con una sola opción
- ✅ Numeración no secuencial
- ✅ Archivos vacíos o corruptos
- ✅ CSV mal formateado

### **Casos Edge**
- ✅ Preguntas muy largas
- ✅ Opciones muy largas
- ✅ Caracteres que no se mapean a ISO-8859-1
- ✅ Bancos de preguntas grandes (100+)

## Reportes de Test

El runner genera reportes detallados que incluyen:

- **Estadísticas generales**: Total, exitosos, fallos, errores
- **Tasa de éxito**: Porcentaje de tests que pasan
- **Tiempo de ejecución**: Duración total y por test
- **Detalles de fallos**: Información específica de errores
- **Recomendaciones**: Pasos para resolver problemas

## Ejemplo de Salida

```
🔍 Cargando tests...
  ✅ test_txt_to_csv
  ✅ test_csv_to_qti
  ✅ test_integration

🧪 Ejecutando 45 tests...

======================================================================
📊 REPORTE DE TESTS
======================================================================
Total de tests ejecutados: 45
✅ Exitosos: 45
❌ Fallos: 0
🚫 Errores: 0
⏭️  Omitidos: 0
⏱️  Tiempo total: 3.24s
📈 Tasa de éxito: 100.0%

======================================================================
🎉 TODOS LOS TESTS PASARON EXITOSAMENTE
✅ El sistema está funcionando correctamente
======================================================================
```

## Agregar Nuevos Tests

### **Para nueva funcionalidad:**

1. **Crear test unitario**:
   ```python
   def test_nueva_funcionalidad(self):
       # Configurar datos de test
       # Ejecutar funcionalidad
       # Verificar resultados
       self.assertEqual(resultado_esperado, resultado_actual)
   ```

2. **Agregar datos de test** si es necesario:
   - Crear archivo `.txt` con casos específicos
   - Documentar propósito del test

3. **Test de integración** si afecta el pipeline:
   ```python
   def test_pipeline_con_nueva_funcionalidad(self):
       # Test extremo-a-extremo
   ```

### **Para casos edge:**

1. **Identificar caso límite**
2. **Crear datos de test mínimos**
3. **Verificar comportamiento esperado**
4. **Documentar el caso**

## Automatización

### **CI/CD Integration**
Los tests pueden integrarse en pipelines de CI/CD:

```bash
# En GitHub Actions, GitLab CI, etc.
python tests/run_tests.py
if [ $? -ne 0 ]; then
    echo "❌ Tests fallaron - deteniendo deployment"
    exit 1
fi
```

### **Pre-commit Hooks**
```bash
# En .git/hooks/pre-commit
#!/bin/bash
cd evaluaciones/bloque-1/canvas
python tests/run_tests.py
```

## Mantenimiento

### **Ejecutar tests regularmente:**
- Antes de commits importantes
- Después de modificar código
- Antes de releases
- Cuando se reportan bugs

### **Actualizar tests cuando:**
- Se agregue nueva funcionalidad
- Se cambien formatos de entrada/salida
- Se modifiquen validaciones
- Se detecten nuevos casos edge

### **Revisar cobertura:**
- Todos los métodos públicos deben tener tests
- Casos positivos y negativos cubiertos
- Edge cases documentados y probados