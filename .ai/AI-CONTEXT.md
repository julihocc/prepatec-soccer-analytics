AI-CONTEXT: Contexto Completo para Asistentes de IA
====================================================

Este archivo proporciona orientación completa a los asistentes de codificación de IA (Claude Code, GitHub Copilot, etc.) cuando trabajen con código en este repositorio.

POLÍTICA CRÍTICA: SIN EMOJIS
=============================

*ESTRICTAMENTE PROHIBIDO:* No se permiten emojis en ninguna parte de este proyecto.

* SIN emojis en archivos de código (.py, .ipynb)
* SIN emojis en documentación (archivos .md)
* SIN emojis en comentarios o strings
* SIN emojis en mensajes de commit
* Mantener contenido profesional, limpio, sin emojis en todo momento

Visión General del Proyecto
============================

Este es un *curso educativo en español* sobre ciencia de datos aplicada al análisis de fútbol/soccer. El repositorio contiene materiales de curso completos para un programa de 15 semanas que enseña fundamentos de Python, conceptos básicos de ciencia de datos y modelado predictivo específicamente dentro del contexto de datos de fútbol.

Audiencia objetivo:: Estudiantes de nivel preparatoria (bachillerato)
Idioma:: Español (todas las variables, comentarios y contenido)
Contexto:: Análisis de datos de fútbol/soccer en todos los ejercicios

Estructura del Repositorio
===========================

Bloques Principales del Curso (3 niveles progresivos)
------------------------------------------------------

Ubicación: directorio `contenido/`

=== Bloque 1: `contenido/bloque-1/` - Prerrequisitos de Programación Python (Semanas 1-5)

* Fundamentos básicos de Python con contexto deportivo
* Notebooks de Jupyter cubriendo variables, estructuras de control, funciones, conceptos básicos de pandas/numpy, y matplotlib

=== Bloque 2: `contenido/bloque-2/` - Fundamentos de Ciencia de Datos con Datos de Fútbol (Semanas 6-10)

* Análisis exploratorio de datos de datasets reales de fútbol
* Análisis estadístico y visualización con seaborn

=== Bloque 3: `contenido/bloque-3/` - Primeras Predicciones con Datos de Fútbol (Semanas 11-15)

* Introducción a conceptos básicos de machine learning
* Modelos predictivos simples usando scikit-learn

Sistema de Evaluación (`evaluaciones/`)
----------------------------------------

*Característica clave:* Recientemente refactorizado para tener *un ejercicio por semana* con instrucciones detalladas y rúbricas precisas.

* Cada bloque tiene estructura de evaluación simplificada: `ejercicios/`, `proyecto/`, y `rubricas/`
* Rúbrica de calificación unificada: 40% corrección técnica + 30% aplicación práctica + 30% documentación
* 60 minutos tiempo estimado de completación por ejercicio
* Todos los ejercicios usan nombres de variables en español y contexto futbolístico

Materiales de Apoyo
--------------------

* `referencias/` - Bibliografía y guías de instalación
* Datasets específicos del curso - Datos de fútbol/soccer para ejercicios prácticos
* Dificultad progresiva - Cada semana construye sobre conceptos anteriores

Estructura Completa del Repositorio
====================================

[source]
----

/
├── contenido/                    # Contenido principal del curso
│   ├── bloque-1/                # Prerrequisitos de Programación Python (Semanas 1-5)
│   │   ├── README.md
│   │   ├── semana-1/            # Configuración y fundamentos
│   │   ├── semana-2/            # Estructuras de datos y flujo de control
│   │   ├── semana-3/            # Funciones y módulos
│   │   ├── semana-4/            # Introducción a Pandas y NumPy
│   │   └── semana-5/            # Visualización básica
│   ├── bloque-2/                # Fundamentos de Ciencia de Datos (Semanas 6-10)
│   │   ├── README.md
│   │   ├── semana-6/            # Exploración de datos
│   │   ├── semana-7/            # Tipos de datos de fútbol
│   │   ├── semana-8/            # Estadísticas descriptivas
│   │   ├── semana-9/            # Visualización de datos
│   │   └── semana-10/           # Análisis e interpretación
│   └── bloque-3/                # Primeras Predicciones (Semanas 11-15)
│       ├── README.md
│       ├── semana-11/           # Introducción al modelado predictivo
│       ├── semana-12/           # Modelos de clasificación avanzados
│       ├── semana-13/           # Métricas de evaluación avanzadas
│       ├── semana-14/           # Ingeniería de características y optimización
│       └── semana-15/           # Proyecto integrativo final
├── evaluaciones/                # Sistema completo de evaluación
│   ├── bloque-1/
│   │   ├── ejercicios/          # Ejercicios semanales (estructura simplificada)
│   │   ├── proyecto/            # Proyecto de bloque (estructura simplificada)
│   │   ├── datasets/            # Datasets específicos del bloque
│   │   └── rubricas/            # Rúbricas de evaluación
│   ├── bloque-2/
│   │   ├── ejercicios/          # Ejercicios preparatorios
│   │   ├── proyecto/            # Proyecto de análisis
│   │   ├── datasets/            # Datos de ligas europeas
│   │   └── rubricas/            # Rúbricas de evaluación
│   └── bloque-3/
│       ├── ejercicios/          # Ejercicios de práctica
│       ├── proyecto/            # Proyecto predictivo
│       ├── datasets/            # Datasets avanzados
│       └── rubricas/            # Rúbricas de evaluación
├── referencias/                 # Documentación de apoyo
│   ├── guia-instalacion.md      # Guía de instalación
│   └── bibliografia-recursos.md # Bibliografía y recursos
└── CLAUDE.md                    # Este archivo - Orientación completa para asistentes de IA
----

Configuración del Entorno de Desarrollo
========================================

Software Requerido
-------------------

[source,bash]
----

# Crear entorno virtual

python -m venv football-analytics
source football-analytics/bin/activate  # Linux/Mac

# football-analytics\Scripts\activate   # Windows

# Instalar dependencias principales

pip install pandas numpy matplotlib seaborn jupyter scikit-learn plotly
----

Verificación del Entorno
-------------------------

[source,python]
----

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn
print(" Todas las bibliotecas instaladas correctamente")
----

Datasets y Referencias Clave
=============================

* *Dataset principal:* <https://www.kaggle.com/datasets/julihocc/champs["champs>" en Kaggle]
* *Notebook de referencia:* <https://www.kaggle.com/code/julihocc/la-remontada["La> Remontada" en Kaggle]
* *Datos de ligas europeas:* `equipos-europa-2023-24.csv`, `jugadores-estrellas-2024.csv`

Estándares Educativos y Estilo
===============================

Audiencia y Contexto Objetivo
------------------------------

Este curso está dirigido a *estudiantes de preparatoria del Tecnológico de Monterrey* en su último año, explorando opciones de carrera en tecnología y datos. El objetivo es introducir conceptos básicos de programación y análisis de datos usando contexto futbolístico para hacer el aprendizaje más atractivo y relevante.

Requisitos de Estilo de Código
-------------------------------

* *Nombres de variables en español:* `goles_por_partido`, `equipos_favoritos`, `datos_futbol`
* *Comentarios educativos:* Explicar el propósito y contexto de cada sección de código en español
* *Contexto futbolístico:* Todos los ejemplos usan equipos reales (Barcelona, Real Madrid, Manchester City, Bayern Munich)
* *Nivel preparatoria:* Explicaciones apropiadas para estudiantes de bachillerato
* *Tono profesional:* Explicaciones claras y concisas sin jerga a menos que se defina
* *ABSOLUTAMENTE SIN EMOJIS:* Nunca usar emojis en código, comentarios, documentación o archivos markdown
* *Tema de seaborn:* Siempre usar `sns.set_theme(style="whitegrid", palette="viridis")`

Directrices de Contenido
------------------------

* Cada notebook combina teoría + práctica + ejercicios de laboratorio
* Complejidad progresiva desde Python básico hasta machine learning
* Tema futbolístico consistente a lo largo de todos los materiales
* Formato interactivo de Jupyter notebook para aprendizaje práctico
* *Cambios incrementales:* Hacer pequeñas mejoras en lugar de reescrituras grandes
* *Código ejecutable:* Asegurar que todo el código funcione en el entorno de Jupyter notebook
* *Restricciones de tiempo:* Ejercicios semanales ≤ 60 minutos, proyectos de bloque 2-3 horas

Metodología Socrática
---------------------

*IMPORTANTE:* Este curso sigue el método socrático de enseñanza, guiando a los estudiantes a descubrir conceptos a través de preguntas reflexivas.

### Principios del Método Socrático en el Curso

* *Preguntas guía:* Usar preguntas para introducir conceptos antes de explicarlos
* *Reflexión activa:* Promover que los estudiantes piensen antes de mostrar respuestas
* *Conexiones prácticas:* Relacionar conceptos abstractos con situaciones deportivas familiares
* *Descubrimiento guiado:* Permitir que los estudiantes "descubran" las respuestas
* *Pensamiento crítico:* Fomentar el análisis y la evaluación de información

### Estructura de Preguntas Socráticas

* *Preguntas de apertura:* `"¿Alguna vez te has preguntado...?"`, `"¿Qué pasaría si...?"`
* *Preguntas reflexivas:* `"¿Por qué crees que...?"`, `"¿Cómo podrías...?"`
* *Preguntas de conexión:* `"¿Ves la relación entre...?"`, `"¿Cómo se compara esto con...?"`
* *Preguntas de aplicación:* `"¿Dónde usarías esto en...?"`, `"¿Qué otros ejemplos puedes pensar?"`
* *Preguntas de síntesis:* `"¿Qué hemos descubierto?"`, `"¿Cómo conecta esto con...?"`

### Implementación en Notebooks

* Comenzar secciones con preguntas antes de explicaciones
* Usar analogías deportivas para conceptos abstractos
* Incluir "Pregunta de reflexión", "Desafío de pensamiento", "Pregunta guía"
* Promover autoevaluación: `"¿Cuál te resultó más difícil?"`
* Conectar con experiencias previas: `"¿Has visto esto en...?"`

### Tipos de Preguntas Socráticas por Propósito

**Generar Curiosidad:**
* `"¿Alguna vez te has preguntado cómo...?"`
* `"¿Qué pasaría si...?"`
* `"¿Has notado que...?"`

**Explorar Conceptos:**
* `"¿Por qué crees que esto sucede?"`
* `"¿Cómo explicarías...?"`
* `"¿Qué diferencias observas entre...?"`

**Conectar Ideas:**
* `"¿Cómo se relaciona esto con...?"`
* `"¿Ves algún patrón en...?"`
* `"¿En qué se parece esto a...?"`

**Aplicar Conocimiento:**
* `"¿Dónde más podrías usar esto?"`
* `"¿Cómo aplicarías esto para...?"`
* `"¿Qué problemas podrías resolver con...?"`

**Evaluar y Sintetizar:**
* `"¿Qué hemos descubierto hasta ahora?"`
* `"¿Cuál fue tu mayor sorpresa?"`
* `"¿Cómo ha cambiado tu perspectiva sobre...?"`

Patrones de Lenguaje y Comunicación
------------------------------------

* *Entusiasmo:* Usar `¡` y lenguaje motivacional (`¡Es como ser un analista deportivo!`)
* *Preguntas socráticas:* Introducir conceptos con preguntas reflexivas (`¿Por qué crees que...?`)
* *Explicaciones guiadas:* Explicar después de generar curiosidad (`¡Este gráfico nos muestra...!`)
* *Aliento:* Terminar con refuerzo positivo (`¡Felicitaciones!`, `¡Excelente progreso!`)
* *Reflexión:* Incluir preguntas de autoevaluación y síntesis

Estándares de Estructura de Notebooks
======================================

Estructura Estándar de Celdas
------------------------------

. *Título en markdown:* `# Semana X: [Título Descriptivo en Español]`
. *Objetivos de aprendizaje:* `**Lo que aprenderemos hoy:**`
. *Preguntas socráticas de apertura:* Introducir el tema con preguntas reflexivas
. *Sección de importaciones* con comentarios educativos
. *Ejemplos progresivos* construyendo complejidad con preguntas guía
. *Reflexiones intermedias:* Preguntas que conecten conceptos
. *Resumen socrático:* `### ¿Qué hemos descubierto juntos?`
. *Vista previa reflexiva:* `### ¿Qué preguntas queremos responder?`

Estructura Socrática por Sección
---------------------------------

Cada sección conceptual debe seguir este patrón:

1. *Pregunta de apertura:* Generar curiosidad sobre el tema
2. *Exploración guiada:* Preguntas que lleven al concepto
3. *Ejemplos prácticos:* Aplicación con contexto deportivo
4. *Preguntas de conexión:* Relacionar con conocimientos previos
5. *Síntesis reflexiva:* Consolidar aprendizaje con preguntas

Convenciones de Celdas de Código
---------------------------------

[source,python]
----

Patrones Socráticos en Código
-----------------------------

[source,python]
----
# Patrón de introducción socrática
print("¿Te has preguntado alguna vez cómo un entrenador decide su alineación?")
print("¡Vamos a descubrirlo usando datos!")

# Generar curiosidad antes de mostrar resultados
equipos = ['Barcelona', 'Real Madrid', 'Manchester City', 'Bayern Munich']
print(f"¿Cuántos equipos tenemos? Descubrámoslo: {len(equipos)}")

# Preguntas reflexivas después de código
print("¿Qué patrones observas en estos datos?")
print("¿Cómo podrías usar esta información para predecir resultados?")
----

Convenciones de Celdas de Código
---------------------------------

[source,python]
----
# Patrón de importación con comentarios educativos y preguntas

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ¿Por qué necesitamos estas herramientas?
# Cada una tiene un propósito específico en nuestro análisis

# Siempre configurar tema de seaborn
sns.set_theme(style="whitegrid", palette="viridis")

print("¡Herramientas listas! ¿Estás preparado para descubrir patrones?")
----
----

Patrón de Generación de Datos
------------------------------

[source,python]
----

# Crear datasets realistas de fútbol para cada ejercicio

import random
equipos = ['Barcelona', 'Real Madrid', 'Manchester City', 'Bayern Munich']
partidos = []
for i in range(30):
    equipo_local = random.choice(equipos)
    equipo_visitante = random.choice([e for e in equipos if e != equipo_local])
    partidos.append({
        'Equipo_Local': equipo_local,
        'Equipo_Visitante': equipo_visitante,
        'Goles_Local': random.randint(0, 3),
        'Goles_Visitante': random.randint(0, 3),
        'Temporada': random.choice(['2023-24', '2024-25'])
    })
datos_futbol = pd.DataFrame(partidos)
----

Estándares de Visualización
----------------------------

[source,python]
----

# Graficación estándar con etiquetas en español

plt.figure(figsize=(10, 6))
sns.countplot(data=datos, x='variable', palette='viridis')
plt.title('¿[Pregunta en Español]?', fontsize=16, fontweight='bold')
plt.xlabel('[Etiqueta en español]')
plt.ylabel('[Etiqueta en español]')
plt.show()
print("¡Este gráfico nos muestra [explicación]!")
----

Comandos de Gestión del Curso
==============================

Ejecutar Materiales del Curso
------------------------------

[source,bash]
----

# Iniciar entorno Jupyter

jupyter notebook

# Navegar a semana específica

cd contenido/bloque-1/semana-1
jupyter notebook configuracion-fundamentos.ipynb
----

Operaciones de Dataset
----------------------

[source,bash]
----

# Descargar desde Kaggle (requiere configuración de API)

pip install kaggle
kaggle datasets download -d julihocc/champs

# Verificar integridad del dataset

python -c "import pandas as pd; df = pd.read_csv('champs.csv'); print(f'Dataset cargado: {df.shape}')"
----

Notas de Arquitectura
=====================

Patrón de Diseño Educativo
---------------------------

* *Aprendizaje andamiado:* Cada semana construye sobre conceptos anteriores
* *Aprendizaje contextual:* Todos los conceptos de programación enseñados a través de ejemplos de fútbol
* *Basado en proyectos:* Culmina en proyectos integrados por bloque
* *Dirigido por evaluación:* Rúbricas claras y evaluaciones estructuradas

Arquitectura Técnica
---------------------

* *Centrado en Jupyter:* Todo el contenido del curso entregado vía notebooks interactivos
* *Progresión de bibliotecas:* matplotlib → seaborn → scikit-learn a medida que aumenta la complejidad
* *Pipeline de datos:* Archivos CSV → DataFrames de pandas → visualizaciones/modelos
* *Diseño modular:* Cada semana es independiente pero conecta con la progresión general

Arquitectura de Evaluación
---------------------------

* *Evaluación formativa:* Ejercicios semanales con retroalimentación inmediata
* *Evaluación sumativa:* Proyectos integrados de nivel de bloque
* *Basado en competencias:* Habilidades técnicas + aplicación práctica + comunicación

Trabajando con Este Repositorio
================================

Metodología Educativa
----------------------

Este curso sigue un enfoque pedagógico específico basado en el *método socrático*:

* *Aprendizaje por descubrimiento:* Los estudiantes descubren conceptos a través de preguntas guiadas
* *Pensamiento crítico:* Preguntas que fomentan análisis y reflexión profunda
* *Conexión experiencial:* Relacionar conceptos con experiencias deportivas familiares
* *Construcción progresiva:* Cada pregunta construye sobre conocimientos previos
* *Autoevaluación:* Promover reflexión sobre el propio aprendizaje

### Indicadores de Método Socrático Efectivo

**En el contenido:**
* Proporción alta de preguntas vs. declaraciones directas
* Preguntas que generan curiosidad antes de explicaciones
* Conexiones explícitas entre conceptos nuevos y conocidos
* Espacios para reflexión personal del estudiante

**En la progresión:**
* Conceptos complejos desglosados en preguntas simples
* Andamiaje desde experiencias familiares hacia conceptos abstractos
* Síntesis reflexiva al final de cada sección
* Preparación para el próximo nivel de preguntas

Criterios de Evaluación
------------------------

* *Corrección técnica:* Código funcional y uso apropiado de herramientas
* *Calidad de análisis:* Profundidad y rigor en el análisis de datos
* *Presentación y comunicación:* Claridad en visualizaciones y explicaciones
* *Aplicación contextual:* Relevancia y pertinencia del análisis deportivo

Al Modificar Materiales del Curso
----------------------------------

. *Mantener idioma español* en todo el contenido
. *Preservar contexto futbolístico* en ejemplos y datasets
. *Seguir progresión educativa* de básico a avanzado
. *Usar estructura de rúbrica consistente* para todas las evaluaciones
. *Probar notebooks interactivamente* antes de finalizar cambios
. *Mantener objetivo de 60 minutos de completación* para ejercicios
. *Hacer mejoras incrementales* en lugar de reescrituras grandes
. *Siempre ejecutar notebook completo* para asegurar que todo funciona
. *Usar mensajes de commit descriptivos* reflejando cambios realizados

Al Crear Contenido Nuevo
-------------------------

* Usar notebooks existentes como plantillas para estructura y estilo
* Obtener ejemplos futbolísticos de equipos y jugadores reconocibles
* Incluir tanto conceptos teóricos como aplicaciones prácticas
* Proporcionar objetivos de aprendizaje claros y criterios de evaluación
* Probar con comprensión de audiencia objetivo (nivel bachillerato)
* Asegurar convenciones de nombres consistentes (preferiblemente español)
* Incluir comentarios bien documentados explicando propósito de cada sección

Patrones de Nombrado de Funciones y Variables
==============================================

[source,python]
----

# Funciones con nombres en español y docstrings

def quien_gano(fila):
    """Determina el ganador de un partido"""
    if fila['Goles_Local'] > fila['Goles_Visitante']:
        return 'Ganó Local'
    elif fila['Goles_Local'] < fila['Goles_Visitante']:
        return 'Ganó Visitante'
    else:
        return 'Empate'

# Declaraciones print educativas explicando resultados

print("¡Este gráfico nos muestra qué tan seguido los equipos marcan goles!")
print(f"Promedio de goles por partido: {promedio:.1f}")
----

Comandos Personalizados
=======================

Comando `/commit`
-----------------

Realiza commits inteligentes de git con análisis automático de cambios y mensajes apropiados en español para este repositorio educativo.

=== Uso

[source]
----

/commit                           # Commit automático con mensaje generado
/commit "mensaje personalizado"   # Commit con mensaje específico
----

=== Proceso de Flujo de Trabajo

. *Pre-análisis:* Ejecutar `git status`, `git diff`, y `git log --oneline -3`
. *Generación de mensaje:* Analizar cambios considerando contexto educativo
. *Estilo español:* Usar verbos infinitivos (Agregar, Actualizar, Corregir)
. *Especificidad:* Mencionar bloques/semanas/ejercicios específicos cuando aplique

=== Formato de Mensaje de Commit

[source]
----

[Título descriptivo en español - máximo 50 caracteres]

[Descripción detallada opcional]
* Cambio específico 1
* Cambio específico 2
* Cambio específico 3

 Generado con [Claude Code](https://claude.ai/code)

Co-Authored-By: Claude <noreply@anthropic.com>
----

=== Reglas Específicas del Repositorio

* *Siempre usar español* en títulos y descripciones
* *Mencionar contexto deportivo* cuando sea relevante
* *Especificar bloque/semana* si los cambios son específicos a secciones del curso
* *Priorizar claridad educativa* sobre jerga técnica

=== Mensajes de Ejemplo

[source,bash]
----

# Cambios de ejercicios

"Actualizar ejercicios Semana 3: mejorar instrucciones de funciones"

# Cambios de documentación

"Mejorar documentación de instalación y configuración"

# Cambios de datasets

"Agregar nuevos datasets para análisis Bloque 2"
----

Recursos de Apoyo
==================

* Guía de instalación: `referencias/guia-instalacion.md`
* Bibliografía: `referencias/bibliografia-recursos.md`
* Resumen de refactorización de evaluación: `evaluaciones/RESUMEN-EJECUTIVO-REFACTORIZACION.md`
* Archivos README específicos de bloque para objetivos de aprendizaje detallados
