Instrucciones para GitHub Copilot
=================================

// @copilot:include always
// CRITICAL: Estas instrucciones DEBEN aplicarse en todo momento
// Nivel: Preparatoria (High School)
// Idioma: Español
// Contexto: Ciencia de datos aplicada al fútbol
// Estructura: 3 sesiones de 50 minutos por semana
// PROHIBIDO: Emojis en cualquier contenido


Contexto Centralizado del Proyecto
===================================

*Para información completa del proyecto, consulta:* link:../.ai/AI-CONTEXT.md[AI-CONTEXT.md]


Instrucciones Específicas para GitHub Copilot
==============================================


Contexto del Proyecto
----------------------

Este es un curso educativo de ciencia de datos aplicada al fútbol en *español* dirigido a estudiantes de preparatoria del Tecnológico de Monterrey.

**ESTRUCTURA CRÍTICA:** Cada semana debe organizarse en **3 sesiones de 50 minutos cada una**:
* **Sesión 1:** Introducción y conceptos fundamentales
* **Sesión 2:** Práctica y desarrollo de habilidades  
* **Sesión 3:** Aplicación práctica con datos reales de fútbol


Directrices de Código
---------------------

* *Variables en español:* `goles_por_partido`, `equipos_favoritos`, `datos_futbol`
* *Contexto futbolístico:* Usar equipos reales (Barcelona, Real Madrid, Manchester City)
* *Nivel educativo:* Explicaciones claras para estudiantes de preparatoria
* *ABSOLUTAMENTE SIN EMOJIS:* Mantener tono profesional y limpio sin emojis
* *Estructura de tiempo:* Cada sesión debe ser completable en exactamente 50 minutos
* *Progresión pedagógica:* Sesión 1→2→3 con dificultad incremental dentro de cada semana


Patrones de Código Preferidos
==============================

[source,python]
----
# Patrón de importación estándar
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración de seaborn
sns.set_theme(style="whitegrid", palette="viridis")

# Variables descriptivas en español
datos_futbol = pd.DataFrame(...)
goles_por_equipo = datos_futbol.groupby('equipo')['goles'].sum()

# Comentarios educativos
print("Este análisis nos muestra los patrones de goles!")
----


Estructura de Notebooks
========================

* Título en español: `# Semana X: [Título Descriptivo]`
* Objetivos de aprendizaje: `**Lo que aprenderemos hoy:**`
* Resumen: `### Lo que Aprendimos Hoy`
* Vista previa: `### Próxima Semana`

**Estructura Obligatoria por Semana (3 sesiones de 50 minutos):**

### Sesión 1: Introducción y Conceptos Fundamentales
* Duración: 50 minutos exactos
* Enfoque: Introducir conceptos teóricos con preguntas socráticas
* Actividades: Reflexión, exploración conceptual, ejemplos básicos

### Sesión 2: Práctica y Desarrollo de Habilidades  
* Duración: 50 minutos exactos
* Enfoque: Aplicación práctica de conceptos con ejercicios guiados
* Actividades: Programación, resolución de problemas, práctica supervisada

### Sesión 3: Aplicación Práctica con Datos Reales de Fútbol
* Duración: 50 minutos exactos
* Enfoque: Integración y aplicación con datasets deportivos reales
* Actividades: Análisis completo, interpretación, síntesis de aprendizajes


Datasets y Referencias
======================

* Dataset principal: "champs" en Kaggle
* Datos de ligas europeas para ejercicios avanzados
* Ejemplos con equipos reconocibles internacionalmente


*Contexto completo en:* link:../.ai/AI-CONTEXT.md[AI-CONTEXT.md]