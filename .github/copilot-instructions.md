# Instrucciones para GitHub Copilot

**Proyecto**: PS5005 Programación Básica 1 - Ciencia de Datos aplicada al Fútbol  
**Institución**: Prepa Tec  
**Unidad de Formación**: PS5005 Programación Básica 1  
**Versión**: 5.4.0+ (Arquitectura Modular Completada)  
**Branch Actual**: `splitting-evaluation-concerns`  
**Autor**: Juliho Castillo Colmenares  
**Email**: julihocc@tec.mx  
**Idioma**: Español completo (código, comentarios, documentación)  
**Contexto**: Análisis deportivo con datos reales de fútbol  
**Metodología**: Enfoque reflexivo + 3 sesiones de 50 minutos por semana
**Stack**: Python + Jupyter + txttoqti (externa) + herramientas modulares

## ARQUITECTURA MODULAR (v5.4.0+)

### Repositorios Separados
- **Principal**: `prepatec-soccer-analytics` - Contenido educativo y herramientas
- **Evaluaciones**: Submodule privado con bancos de preguntas y Canvas QTI
- **txttoqti**: Repositorio externo `github.com/julihocc/txttoqti` - Motor QTI independiente

### Estructura del Repositorio Principal
```
contenido/              # Material educativo por semana (3 bloques × 5 semanas)
evaluaciones/          # SUBMODULE PRIVADO - Sistema evaluativo completo
herramientas/          # Scripts de conversión y utilidades independientes
├── notebook-to-pdf/   # Conversión profesional de notebooks
└── py-to-marp/       # Presentaciones desde código Python
referencias/           # Material de apoyo y documentación
temario/              # Syllabus y planificación académica
```

### Dependencias Críticas Actuales
- **txttoqti**: Repositorio externo independiente (`pip install git+https://github.com/julihocc/txttoqti.git`)
- **Python ≥3.10**: Requerimiento para compatibilidad completa
- **pandas/numpy/matplotlib/seaborn**: Stack de análisis de datos
- **pandoc + XeLaTeX**: Para generación profesional de PDFs
- **Jupyter**: Entorno de desarrollo interactivo

### 🚀 MIGRACIÓN txttoqti v0.3.0 COMPLETADA 
- **Eliminación 96.7% código**: 924 → 30 líneas (wrappers minimalistas)
- **Cero mantenimiento**: Equipo oficial txttoqti mantiene toda lógica QTI
- **Funcionalidad mejorada**: CLI enhancado, mejor validación, manejo errores
- **Backward Compatibility**: Interface idéntica `python generar_qti.py` preservada

## CONTEXTO EDUCATIVO CRÍTICO

**CURSO INTRODUCTORIO PARA PREPARATORIA**: Este es un curso de NIVEL BÁSICO para estudiantes de 15-18 años SIN experiencia previa en programación.

### Características del Estudiante Objetivo:
- **Edad**: 15-18 años (preparatoria/bachillerato)
- **Experiencia previa**: CERO programación, CERO ciencia de datos
- **Nivel matemático**: Álgebra básica de preparatoria
- **Contexto cultural**: México, familiarizados con fútbol
- **Motivación**: Conectar tecnología con deportes

### RESTRICCIÓN TEMPORAL CRÍTICA:
- **Duración máxima por sesión**: 50 minutos reales de contenido
- **Planificación**: 15 min teoría + 25 min práctica + 10 min síntesis
- **Prueba obligatoria**: Cada notebook debe ejecutarse completamente en máximo 45 minutos
- **Principio rector**: "Si no cabe en 50 minutos, es demasiado para una sesión"  

## REGLA CRÍTICA: PROHIBIDOS LOS EMOJIS

**ESTRICTAMENTE PROHIBIDO**: No se permiten emojis en ninguna parte de este proyecto.
- SIN emojis en archivos de código (.py, .ipynb)
- SIN emojis en documentación (archivos .md)
- SIN emojis en comentarios o strings
- SIN emojis en print statements
- SIN emojis en mensajes de commit
## FLUJOS DE DESARROLLO ACTUALES

### Gestión de Submodules
```bash
# Inicializar submodules tras clonar repositorio
git submodule update --init --recursive

# Actualizar submodule de evaluaciones (solo con permisos)
cd evaluaciones && git pull origin master && cd ..
git add evaluaciones && git commit -m "docs: update evaluaciones submodule"

# Verificar estado submodules
git submodule status
```

### Conversión QTI (Canvas) - txttoqti Externo
```bash
# Instalar txttoqti desde repositorio externo
pip install git+https://github.com/julihocc/txttoqti.git

# Usar wrappers en evaluaciones/ (si tienes acceso al submodule)
cd evaluaciones/bloque-1/canvas/ && python generar_qti.py
cd evaluaciones/bloque-2/canvas/ && python generar_qti.py
cd evaluaciones/bloque-3/canvas/ && python generar_qti.py

# Comando directo txttoqti (si está instalado globalmente)
txttoqti-edu --path evaluaciones/ --status
txttoqti-edu --path evaluaciones/bloque-1/canvas/
```

**Arquitectura actual**:
- **Wrappers minimalistas**: Scripts generar_qti.py son interfaces de 90 líneas
- **txttoqti independiente**: Motor QTI manejado por repositorio externo
- **Submodule evaluaciones**: Contenido evaluativo en repositorio privado separado
- **Zero local maintenance**: Toda lógica QTI en repositorio txttoqti oficial

### Generación de PDFs Profesionales
```bash
# Conversión inteligente (solo regenera cuando hay cambios)
python herramientas/notebook-to-pdf/smart_convert.py contenido/
python herramientas/notebook-to-pdf/smart_convert.py contenido/ --status
```
**Motor recomendado**: XeLaTeX para caracteres españoles  
**Cache inteligente**: Solo regenera cuando hay cambios reales  
**Tiempo típico**: 30-60 segundos por notebook

### Presentaciones Automáticas
```bash
# Convierte archivos .py percent a presentaciones Marp
python herramientas/py-to-marp/convert.py archivo.py --config educativo
```

## PATRONES DE CÓDIGO OBLIGATORIOS

### Variables y Naming
```python
# CORRECTO - Nombres en español
goles_por_partido = df['goles'].mean()
jugadores_barcelona = df[df['equipo'] == 'Barcelona']
modelo_prediccion = LogisticRegression()

# INCORRECTO - Nombres en inglés
goals_per_match = df['goals'].mean()
barcelona_players = df[df['team'] == 'Barcelona']  
prediction_model = LogisticRegression()
```

### Visualizaciones Estándar
```python
# Configuración obligatoria
sns.set_theme(style="whitegrid", palette="viridis")
plt.figure(figsize=(10, 6))

# Títulos siempre en español con contexto futbolístico
plt.title('Distribución de Goles por Jugador - Barcelona 2023')
plt.xlabel('Minutos Jugados')
plt.ylabel('Goles Marcados')
```

### Comentarios Educativos
```python
# OBLIGATORIO - Explicar el "por qué" futbolístico
# Calculamos el promedio de posesión porque los equipos como Barcelona
# que dominan el balón tienden a crear más oportunidades de gol
promedio_posesion = df['posesion'].mean()

# Filtramos jugadores con más de 1000 minutos porque necesitamos
# una muestra representativa del rendimiento, similar a como
# los scouts evalúan jugadores con suficiente tiempo de juego
jugadores_regulares = df[df['minutos'] > 1000]
```

## INTEGRACIÓN DE HERRAMIENTAS

### Sistema de Evaluación
- **Canvas QTI**: Generación automática desde texto plano con `generar_qti.py`
- **Bancos de preguntas**: Formato `Q1: A) B) C) D) RESPUESTA: X` convertido automáticamente
- **Detección de cambios**: Hash-based para regeneración inteligente
- **Distribución cognitiva**: [R] Recuerdo, [C] Comprensión, [A] Aplicación, [S] Socrática

### Gestión de Contenido
- **Formato principal**: Notebooks (.ipynb) para desarrollo interactivo
- **Versionado**: Archivos .py percent para control de versiones
- **Distribución**: PDFs profesionales generados automáticamente
- **Presentaciones**: Marp desde código Python cuando sea necesario

### Stack Técnico Integrado
```python
# Librerías core (siempre importar en este orden)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Solo en Bloque 3 - Machine Learning
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
```

## DOCUMENTACIÓN OBLIGATORIA DE CAMBIOS

**Política crítica**: Todo cambio que afecte evaluaciones, cronogramas, o contenido educativo debe documentarse inmediatamente en el mismo commit.

### Alcance de Documentación:
- **Cambios en bancos**: Actualizar README del bloque + conteo de preguntas
- **Modificaciones de rúbricas**: Reflejar nuevos pesos en documentación
- **Ajustes de cronograma**: Actualizar README principal si es cambio global
- **Nuevos métodos de evaluación**: Documentar en evaluaciones/README.md

### Formato de Commits:
```bash
# Prefijos obligatorios
feat(banco-bloque2): añadir 15 preguntas Extended [S] interpretación
docs(rubrica-bloque3): actualizar pesos 40/30/30 nueva distribución
refactor(notebook): optimizar tiempo ejecución semana-4 a 45min
```

### Checklist Pre-Commit:
1. ¿Cambio altera evaluación estudiantil? → Actualizar rúbrica + README
2. ¿Afecta distribución de preguntas? → Documentar conteo en README del bloque  
3. ¿Modifica tiempos o duración? → Validar constraint 50 minutos
4. ¿Respeta prohibición de emojis + español? → Verificación final
5. ¿Notebooks ejecutan en <45 min? → Prueba de tiempo real
## ARCHIVOS CRÍTICOS DE REFERENCIA

### Estructura de Contenido
- **Ejemplo base**: `contenido/bloque-1/semana-1/configuracion-fundamentos.py`
- **Evaluaciones**: `evaluaciones/*/README.md` para políticas por bloque
- **Herramientas**: `herramientas/notebook-to-pdf/` y `herramientas/py-to-marp/`

### Scripts de QTI (Evaluaciones Canvas) - 🚀 txttoqti v0.3.0 MIGRADO
- **Ubicación**: `evaluaciones/bloque-*/canvas/generar_qti.py` (wrappers minimalistas)
- **Implementación nueva**: Wrappers de 30 líneas que llaman `txttoqti-edu`
- **Función crítica**: Preserva interface original + auto-detección de txttoqti v0.3.0
- **Dependencia externa**: txttoqti v0.3.0 con módulo educacional completo
- **Output**: Archivos ZIP compatibles con Canvas LMS
- **Eliminación código**: 96.7% reducción (924 → 30 líneas por wrapper)
- **Características mejoradas**: CLI enhancado, mejor validación, cero mantenimiento local

### Dataset Principal
- **Fuente**: [Champs - Kaggle](https://www.kaggle.com/datasets/julihocc/champs)
- **Referencia**: [Notebook "La Remontada"](https://www.kaggle.com/code/julihocc/la-remontada)
- **Uso**: Datos reales Champions League para ejercicios y proyectos

## METODOLOGÍA SOCRÁTICA INTEGRADA

### Estructura Obligatoria por Notebook:
1. **Pregunta motivadora**: "¿Cómo harías X como entrenador del Barcelona?"
2. **Descubrimiento guiado**: Paso a paso con preguntas reflexivas
3. **Aplicación práctica**: Código con datos reales de fútbol
4. **Síntesis reflexiva**: "¿Qué significa esto para el análisis deportivo?"

### Analogías Futbolísticas Recurrentes:
- **Variables** = Estadísticas de jugadores (goles, asistencias, minutos)
- **Funciones** = Jugadas ensayadas que se pueden repetir
- **Loops** = Entrenamientos repetitivos para perfeccionar técnica
- **DataFrames** = Fichas técnicas completas de equipos como Real Madrid
- **Modelos ML** = Entrenadores digitales que aprenden de datos históricos

## COMANDOS DE VALIDACIÓN FINAL

```bash
# Verificar que notebooks ejecutan en tiempo límite
jupyter nbconvert --execute --to notebook contenido/bloque-1/semana-1/archivo.ipynb

# Validar generación QTI (requiere acceso al submodule evaluaciones)
cd evaluaciones/bloque-1/canvas/ && python generar_qti.py --status
# O instalar txttoqti directamente: pip install git+https://github.com/julihocc/txttoqti.git

# Probar conversión PDF con cache inteligente
python herramientas/notebook-to-pdf/smart_convert.py contenido/ --status

# Verificar dependencias críticas
python -c "import txttoqti; print('txttoqti externo OK')"
```

## ⚡ ESTADO ACTUAL - txttoqti v0.3.0 MIGRACIÓN COMPLETADA

**Estado v5.2.0 (Migración Exitosa)**:
- **txttoqti v0.3.0 integrado**: Librería oficial con módulo educacional
- **Eliminación 96.7% código local**: 924 → 30 líneas (wrappers preservan interface)  
- **Cero mantenimiento**: Equipo txttoqti mantiene toda lógica QTI
- **Funcionalidad mejorada**: CLI enhancado, mejor validación, manejo errores
- **Backward compatibility perfecta**: `python generar_qti.py` interface preservada

**Características nuevas disponibles**:
- **`txttoqti-edu` CLI**: Comando directo con auto-detección educacional
- **Módulo Python**: `from txttoqti.educational import QtiConverter`
- **Mejores validaciones**: Interactive troubleshooting mode mejorado
- **Opciones CLI expandidas**: `--verbose`, `--path`, `--interactive`
- **File naming adaptation**: Symlinks preservan naming original del proyecto

**PRINCIPIO RECTOR**: "Cada línea de código debe enseñar algo sobre fútbol, cada ejercicio debe resolver un problema real de análisis deportivo, y cada sesión debe completarse en exactamente 50 minutos."

---

## INFORMACIÓN DEL AUTOR

**Autor**: Juliho Castillo Colmenares  
**Institución**: Prepa Tec  
**Email**: julihocc@tec.mx  
**Repositorio**: https://github.com/julihocc/prepatec-soccer-analytics