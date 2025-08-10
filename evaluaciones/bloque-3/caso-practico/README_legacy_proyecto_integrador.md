Proyecto Integrador Final
========================
Sistema de Análisis Predictivo para Fútbol


Información Básica
------------------

Modalidad:: Individual
Ponderación:: 30% de la calificación final
Duración:: 2 semanas (Semana 14-15)
Entrega:: Jupyter Notebook único con 3 secciones


Descripción General
-------------------

Este proyecto integrador constituye la evaluación final del curso, donde los estudiantes demostrarán los conocimientos básicos de Python para análisis de datos deportivos adquiridos durante las 15 semanas. Cada estudiante desarrollará un análisis completo de datos de fútbol que combine conceptos fundamentales de programación, análisis de datos y predicciones básicas.


Contexto del Proyecto
---------------------

Eres un analista junior de fútbol y tu primera tarea es crear un reporte completo sobre la Liga de Campeones usando Python. Tu análisis debe demostrar que puedes:

. Explorar y limpiar datos de partidos de fútbol
. Crear visualizaciones que muestren patrones interesantes
. Hacer predicciones básicas sobre resultados de partidos
. Comunicar hallazgos de forma clara y profesional


Objetivos de Aprendizaje
------------------------

Al completar este proyecto, el estudiante será capaz de:

* Usar pandas para cargar, limpiar y manipular datos de fútbol
* Aplicar matplotlib y seaborn para crear gráficos informativos
* Calcular estadísticas básicas y encontrar patrones en los datos
* Crear un modelo de predicción simple usando scikit-learn
* Organizar su análisis en un notebook de Jupyter bien estructurado
* Explicar sus hallazgos usando lenguaje claro y apropiado


Estructura del Proyecto
========================


Sección 1: Exploración de Datos (40%)
--------------------------------------

Tiempo estimado:: 3-4 horas

=== Objetivos

* Cargar y explorar el dataset de Champions League
* Limpiar datos básicos (valores faltantes, duplicados)
* Calcular estadísticas descriptivas simples

=== Entregables en el notebook

* Carga de datos con pandas
* Exploración básica (shape, info, describe)
* Limpieza de datos sencilla
* 3-5 gráficos descriptivos con matplotlib/seaborn

=== Tareas específicas

==== 1.1 Carga de Datos

[source,python]
----
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Configurar tema de seaborn (como visto en clase)
sns.set_theme(style="whitegrid", palette="viridis")

# Cargar datos
datos_champions = pd.read_csv('champions_league_matches.csv')

# Exploración básica
print(f"El dataset tiene {datos_champions.shape[0]} filas y {datos_champions.shape[1]} columnas")
print("\nPrimeras 5 filas:")
print(datos_champions.head())
----

==== 1.2 Análisis Básico de Datos

* Ver información general del dataset (`.info()`, `.describe()`)
* Identificar valores faltantes simples
* Contar equipos únicos y temporadas
* Calcular estadísticas básicas de goles

==== 1.3 Limpieza Simple de Datos

* Eliminar filas duplicadas si las hay
* Rellenar valores faltantes básicos
* Crear una nueva columna simple como:
  - `total_goles`: suma de goles local + visitante
  - `resultado`: 'Local', 'Visitante', 'Empate'


Sección 2: Visualización y Análisis (35%)
------------------------------------------

Tiempo estimado:: 2-3 horas

=== Objetivos

* Crear gráficos que muestren patrones en los datos
* Responder preguntas básicas sobre el fútbol
* Usar matplotlib y seaborn efectivamente

=== Entregables en el notebook

* 5-7 visualizaciones diferentes (barras, histogramas, boxplots)
* Análisis escrito de cada gráfico
* Al menos 3 conclusiones interesantes sobre Champions League

=== Tareas específicas

==== 2.1 Gráficos Requeridos (ejemplos)

[source,python]
----
# 1. Gráfico de barras - Equipos con más goles
plt.figure(figsize=(10, 6))
goles_por_equipo = datos_champions.groupby('equipo_local')['goles_local'].sum()
goles_por_equipo.head(10).plot(kind='bar')
plt.title('Top 10 Equipos con Más Goles en Champions League')
plt.ylabel('Total de Goles')
plt.show()

# 2. Histograma - Distribución de goles por partido
plt.figure(figsize=(8, 6))
plt.hist(datos_champions['total_goles'], bins=10, color='skyblue')
plt.title('¿Cuántos goles se marcan normalmente en Champions?')
plt.xlabel('Goles por Partido')
plt.ylabel('Frecuencia')
plt.show()
----

==== 2.2 Análisis Descriptivo Simple

* Comparar goles como local vs visitante
* Identificar los equipos más exitosos
* Analizar patrones por temporada
* Describir tendencias básicas observadas

==== 2.3 Estadísticas Básicas

* Promedio de goles por partido
* Equipo con mejor record como local
* Temporada con más/menos goles
* Porcentaje de empates, victorias locales y visitantes


Sección 3: Predicción Simple (25%)
-----------------------------------

Tiempo estimado:: 2-3 horas

=== Objetivos

* Crear un modelo básico de predicción
* Usar scikit-learn para clasificación simple
* Evaluar qué tan bien funciona el modelo

=== Entregables en el notebook

* Un modelo de clasificación simple (como decidir si ganará local o visitante)
* Evaluación básica del modelo (precisión)
* Explicación en español de los resultados

=== Tareas específicas

==== 3.1 Preparar Datos para Predicción

[source,python]
----
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Preparar variables simples para el modelo
# Por ejemplo: goles promedio del equipo, si juega como local/visitante
X = datos_champions[['goles_promedio_local', 'goles_promedio_visitante']]
y = datos_champions['resultado']  # 'Local', 'Visitante', 'Empate'

# Dividir datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
----

==== 3.2 Crear Modelo Simple

* Usar RandomForestClassifier (más fácil que regresión logística para principiantes)
* Entrenar con datos históricos
* Hacer predicciones en datos de prueba
* Calcular precisión del modelo

==== 3.3 Interpretar Resultados

* ¿Qué tan bien predice el modelo?
* ¿Qué variables son más importantes?
* ¿Es mejor que adivinar al azar?
* Escribir conclusiones en español sencillo


Dataset Proporcionado
======================


Dataset Principal: Champions League Matches
--------------------------------------------

Fuente:: https://www.kaggle.com/datasets/julihocc/champs[Kaggle - Champions League Matches]

Este dataset contiene información detallada sobre partidos de la Liga de Campeones de la UEFA, proporcionando una excelente base para análisis predictivo y estadístico de fútbol de élite europea.

=== Características del Dataset

Competición:: UEFA Champions League
Formato:: Archivo comprimido (ZIP)
Tipo de datos:: Estadísticas de partidos de fútbol profesional
Alcance:: Partidos de la competición más prestigiosa de clubes europeos

=== Datos Disponibles (estructura típica esperada)

[source,python]
----
# Estructura estimada basada en competiciones de Champions League
columnas_esperadas = [
    'match_id', 'fecha', 'equipo_local', 'equipo_visitante', 
    'goles_local', 'goles_visitante', 'resultado_final',
    'fase_competicion', 'temporada', 'estadio',
    'posesion_local', 'posesion_visitante',
    'tiros_local', 'tiros_visitante', 'tiros_arco_local', 'tiros_arco_visitante',
    'corners_local', 'corners_visitante', 'faltas_local', 'faltas_visitante',
    'tarjetas_amarillas_local', 'tarjetas_amarillas_visitante',
    'tarjetas_rojas_local', 'tarjetas_rojas_visitante',
    'arbitro', 'asistencia'
]
----

=== Ventajas para el Análisis

* *Nivel competitivo:* Equipos de máxima calidad europea
* *Contexto táctico:* Partidos de alta intensidad y planificación
* *Relevancia temporal:* Datos de competiciones recientes
* *Variedad de fases:* Desde fase de grupos hasta final


Requisitos Técnicos
====================


Bibliotecas Requeridas
-----------------------

[source,python]
----
# Análisis de datos (visto en Bloque 1 y 2)
import pandas as pd
import numpy as np

# Visualización (visto en Bloque 2)
import matplotlib.pyplot as plt
import seaborn as sns

# Configurar tema de seaborn (estándar del curso)
sns.set_theme(style="whitegrid", palette="viridis")

# Machine Learning básico (Bloque 3)
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Utilidades básicas
import warnings
warnings.filterwarnings('ignore')
----


Archivo Único Requerido
------------------------

Nombre del archivo:: `proyecto_champions_final.ipynb`

=== Estructura del Notebook

----
# Proyecto Final: Análisis de Champions League

## Sección 1: Exploración de Datos (40%)
### 1.1 Carga de Datos
### 1.2 Análisis Básico de Datos  
### 1.3 Limpieza Simple de Datos

## Sección 2: Visualización y Análisis (35%)
### 2.1 Gráficos Descriptivos
### 2.2 Análisis de Patrones
### 2.3 Estadísticas Básicas

## Sección 3: Predicción Simple (25%)
### 3.1 Preparar Datos para Predicción
### 3.2 Crear Modelo Simple
### 3.3 Interpretar Resultados

## Conclusiones Finales
- ¿Qué aprendiste sobre Champions League?
- ¿Cómo te ayudó Python en el análisis?
- ¿Qué más te gustaría investigar?
----


Criterios de Evaluación
========================


Rúbrica Detallada (100 puntos)
-------------------------------

[cols="2,1,2,2,2,2"]
|===
|Componente |Peso |Excelente (90-100%) |Bueno (80-89%) |Suficiente (70-79%) |Insuficiente (<70%)

|*Exploración de Datos* 
|40% 
|Análisis completo, insights claros, código bien documentado
|Análisis correcto, interpretación adecuada, código funcional
|Análisis básico pero correcto, código simple
|Análisis superficial o errores importantes

|*Visualización y Análisis*
|35% 
|Gráficos informativos, análisis profundo, conclusiones sólidas
|Gráficos correctos, análisis apropiado, buenas conclusiones
|Gráficos básicos funcionales, análisis simple
|Gráficos deficientes o análisis incorrecto

|*Predicción Simple*
|25%
|Modelo bien implementado, evaluación correcta, interpretación clara
|Modelo correcto, evaluación adecuada, interpretación básica
|Modelo funcional básico, evaluación simple
|Errores en implementación o evaluación
|===


Criterios Específicos por Sección
----------------------------------

=== Exploración de Datos (40 puntos)

* *Carga y exploración (15 pts):* Código correcto, exploración completa
* *Limpieza de datos (15 pts):* Manejo apropiado de datos faltantes y duplicados
* *Estadísticas descriptivas (10 pts):* Cálculos correctos, interpretación básica

=== Visualización y Análisis (35 puntos)

* *Gráficos (20 pts):* 5-7 visualizaciones claras y apropiadas
* *Análisis (10 pts):* Interpretación correcta de los gráficos
* *Conclusiones (5 pts):* Al menos 3 conclusiones válidas sobre Champions League

=== Predicción Simple (25 puntos)

* *Preparación de datos (10 pts):* División correcta train/test, variables apropiadas
* *Implementación del modelo (10 pts):* Código correcto, uso apropiado de RandomForest
* *Evaluación e interpretación (5 pts):* Cálculo de precisión, interpretación en español


Hitos y Entregables
====================


Semana 14: Exploración y Visualización
---------------------------------------

Fecha límite:: Viernes de la semana 14

Entregables::
* Sección 1 completa (Exploración de Datos)
* Sección 2 completa (Visualización y Análisis)
* Notebook parcial con las primeras dos secciones

Revisión:: Feedback sobre calidad de análisis y visualizaciones


Semana 15: Predicción y Entrega Final
--------------------------------------

Fecha límite:: Último día de clases

Entregables::
* Sección 3 completa (Predicción Simple)
* Conclusiones finales
* Notebook completo y bien documentado

Evaluación:: Calificación final basada en rúbrica completa


Preguntas de Investigación Sugeridas
=====================================

Los estudiantes pueden enfocar su análisis en estas preguntas:

Análisis Básico
---------------

. ¿Qué equipos marcan más goles en Champions League?
. ¿Es ventajoso jugar como local en esta competición?
. ¿En qué temporada hubo más goles?
. ¿Cuál es el resultado más común?

Análisis de Patrones
--------------------

. ¿Hay diferencias entre las fases del torneo?
. ¿Qué países tienen equipos más exitosos?
. ¿Cómo ha cambiado el estilo de juego a través de los años?
. ¿Existen patrones en los resultados por temporada?


Recursos y Soporte
===================


Documentación Técnica
----------------------

* https://pandas.pydata.org/docs/[Pandas Documentation]
* https://matplotlib.org/stable/contents.html[Matplotlib Guide]
* https://seaborn.pydata.org/tutorial.html[Seaborn Tutorial]
* https://scikit-learn.org/stable/user_guide.html[Scikit-learn User Guide]


Sesiones de Consulta
---------------------

Presencial::
* Martes y jueves: 2:00-3:00 PM

Virtual::
* Miércoles: 6:00-7:00 PM

Por cita:: Disponible bajo solicitud


Recursos Adicionales
---------------------

* Datasets complementarios disponibles en Moodle
* Templates de código en el repositorio del curso
* Ejemplos de análisis básicos (notebooks de referencia)
* Canal de Slack para dudas técnicas


Criterios de Originalidad
==========================


Se Fomenta
----------

* Análisis creativos dentro del nivel del curso
* Preguntas interesantes sobre el fútbol
* Visualizaciones claras y bien diseñadas
* Interpretaciones personales de los datos


Se Penaliza
-----------

* Copia directa de código sin comprensión
* Proyectos idénticos entre estudiantes
* Uso de técnicas no vistas en clase sin explicación
* Datos externos sin autorización previa


Política de Integridad Académica
---------------------------------

* Todo código debe ser comprendido por el estudiante
* Se permite consultar documentación oficial
* Se fomenta la discusión de conceptos entre estudiantes
* Se prohíbe compartir código completo de soluciones


Notas Finales
=============

Este proyecto integrador representa la culminación del aprendizaje en el curso, donde los estudiantes demuestran su capacidad para aplicar Python de manera efectiva en el análisis básico de datos deportivos. El enfoque está en la comprensión y aplicación correcta de los conceptos fundamentales aprendidos durante las 15 semanas del curso.

¡Buena suerte con tu análisis de la Champions League!