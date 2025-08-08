# Proyecto Integrador Final

## Sistema de Análisis Predictivo para Fútbol

**Modalidad:** Individual  
**Ponderación:** 30% de la calificación final  
**Duración:** 2 semanas (Semana 14-15)  
**Entrega:** Jupyter Notebook único con 3 secciones

---

## Descripción General

Este proyecto integrador constituye la evaluación final del curso, donde los estudiantes demostrarán los conocimientos básicos de Python para análisis de datos deportivos adquiridos durante las 15 semanas. Cada estudiante desarrollará un análisis completo de datos de fútbol que combine conceptos fundamentales de programación, análisis de datos y predicciones básicas.

---

## Contexto del Proyecto

Eres un analista junior de fútbol y tu primera tarea es crear un reporte completo sobre la Liga de Campeones usando Python. Tu análisis debe demostrar que puedes:

1. **Explorar y limpiar datos** de partidos de fútbol
2. **Crear visualizaciones** que muestren patrones interesantes
3. **Hacer predicciones básicas** sobre resultados de partidos
4. **Comunicar hallazgos** de forma clara y profesional

---

## Objetivos de Aprendizaje

Al completar este proyecto, el estudiante será capaz de:

- Usar pandas para cargar, limpiar y manipular datos de fútbol
- Aplicar matplotlib y seaborn para crear gráficos informativos
- Calcular estadísticas básicas y encontrar patrones en los datos
- Crear un modelo de predicción simple usando scikit-learn
- Organizar su análisis en un notebook de Jupyter bien estructurado
- Explicar sus hallazgos usando lenguaje claro y apropiado

---

## Estructura del Proyecto

### Sección 1: Exploración de Datos (40%)

**Tiempo estimado:** 3-4 horas

#### Objetivos

- Cargar y explorar el dataset de Champions League
- Limpiar datos básicos (valores faltantes, duplicados)
- Calcular estadísticas descriptivas simples

#### Entregables en el notebook

- Carga de datos con pandas
- Exploración básica (shape, info, describe)
- Limpieza de datos sencilla
- 3-5 gráficos descriptivos con matplotlib/seaborn

#### Tareas específicas

**1.1 Carga de Datos**

```python
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
```

**1.2 Análisis Básico de Datos**

- Ver información general del dataset (`.info()`, `.describe()`)
- Identificar valores faltantes simples
- Contar equipos únicos y temporadas
- Calcular estadísticas básicas de goles

**1.3 Limpieza Simple de Datos**

- Eliminar filas duplicadas si las hay
- Rellenar valores faltantes básicos
- Crear una nueva columna simple como:
  - `total_goles`: suma de goles local + visitante
  - `resultado`: 'Local', 'Visitante', 'Empate'

### Sección 2: Visualización y Análisis (35%)

**Tiempo estimado:** 2-3 horas

#### Objetivos

- Crear gráficos que muestren patrones en los datos
- Responder preguntas básicas sobre el fútbol
- Usar matplotlib y seaborn efectivamente

#### Entregables en el notebook

- 5-7 visualizaciones diferentes (barras, histogramas, boxplots)
- Análisis escrito de cada gráfico
- Al menos 3 conclusiones interesantes sobre Champions League

#### Tareas específicas

**2.1 Gráficos Requeridos (ejemplos)**

```python
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
```

**2.2 Análisis Descriptivo Simple**

- Comparar goles como local vs visitante
- Identificar los equipos más exitosos
- Analizar patrones por temporada
- Describir tendencias básicas observadas

**2.3 Estadísticas Básicas**

- Promedio de goles por partido
- Equipo con mejor record como local
- Temporada con más/menos goles
- Porcentaje de empates, victorias locales y visitantes

### Sección 3: Predicción Simple (25%)

**Tiempo estimado:** 2-3 horas

#### Objetivos

- Crear un modelo básico de predicción
- Usar scikit-learn para clasificación simple
- Evaluar qué tan bien funciona el modelo

#### Entregables en el notebook

- Un modelo de clasificación simple (como decidir si ganará local o visitante)
- Evaluación básica del modelo (precisión)
- Explicación en español de los resultados

#### Tareas específicas

**3.1 Preparar Datos para Predicción**

```python
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Preparar variables simples para el modelo
# Por ejemplo: goles promedio del equipo, si juega como local/visitante
X = datos_champions[['goles_promedio_local', 'goles_promedio_visitante']]
y = datos_champions['resultado']  # 'Local', 'Visitante', 'Empate'

# Dividir datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```

**3.2 Crear Modelo Simple**

- Usar RandomForestClassifier (más fácil que regresión logística para principiantes)
- Entrenar con datos históricos
- Hacer predicciones en datos de prueba
- Calcular precisión del modelo

**3.3 Interpretar Resultados**

- ¿Qué tan bien predice el modelo?
- ¿Qué variables son más importantes?
- ¿Es mejor que adivinar al azar?
- Escribir conclusiones en español sencillo

---

## Dataset Proporcionado

### Dataset Principal: Champions League Matches

**Fuente:** [Kaggle - Champions League Matches](https://www.kaggle.com/datasets/julihocc/champs)

Este dataset contiene información detallada sobre partidos de la Liga de Campeones de la UEFA, proporcionando una excelente base para análisis predictivo y estadístico de fútbol de élite europea.

#### Características del Dataset

- **Competición:** UEFA Champions League
- **Formato:** Archivo comprimido (ZIP)
- **Tipo de datos:** Estadísticas de partidos de fútbol profesional
- **Alcance:** Partidos de la competición más prestigiosa de clubes europeos

#### Datos Disponibles (estructura típica esperada)

```python
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
```

#### Ventajas para el Análisis

- **Nivel competitivo:** Equipos de máxima calidad europea
- **Contexto táctico:** Partidos de alta intensidad y planificación
- **Relevancia temporal:** Datos de competiciones recientes
- **Variedad de fases:** Desde fase de grupos hasta final

---

## Requisitos Técnicos

### Bibliotecas Requeridas

```python
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
```

### Archivo Único Requerido

```
proyecto_champions_final.ipynb
```

**Estructura del Notebook:**

```markdown
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
```

---

## Criterios de Evaluación

### Rúbrica Detallada (100 puntos)

| Componente | Peso | Excelente (90-100%) | Bueno (80-89%) | Suficiente (70-79%) | Insuficiente (<70%) |
|------------|------|-------------------|----------------|-------------------|-------------------|
| **Análisis Exploratorio** | 25% | Análisis exhaustivo, insights profundos | Análisis completo, interpretación correcta | Análisis básico pero correcto | Análisis superficial o errores |
| **Modelado ML** | 35% | Modelos bien implementados, validación rigurosa | Modelos correctos, evaluación adecuada | Modelos básicos funcionales | Errores en implementación o validación |
| **Dashboard** | 25% | Interactividad avanzada, UX excelente | Funcionalidad completa, diseño claro | Funcionalidad básica | Dashboard no funcional |
| **Presentación** | 15% | Comunicación excepcional, dominio total | Presentación clara, buen dominio | Presentación básica | Comunicación deficiente |

### Criterios Específicos por Fase

#### Análisis Exploratorio (25 puntos)

- **Calidad de EDA (10 pts):** Exhaustividad, insights, visualizaciones
- **Limpieza de datos (8 pts):** Manejo de faltantes, outliers, inconsistencias
- **Ingeniería de features (7 pts):** Creatividad, relevancia, implementación

#### Modelado Predictivo (35 puntos)

- **Implementación técnica (15 pts):** Código correcto, buenas prácticas
- **Evaluación de modelos (10 pts):** Métricas apropiadas, validación cruzada
- **Interpretación (10 pts):** Análisis de resultados, importancia de variables

#### Dashboard Interactivo (25 puntos)

- **Funcionalidad (12 pts):** Filtros, predicciones, comparaciones
- **Diseño UX (8 pts):** Intuitividad, estética, navegación
- **Integración técnica (5 pts):** Conexión con modelos, rendimiento

#### Presentación (15 puntos)

- **Claridad comunicativa (8 pts):** Estructura, lenguaje, tiempo
- **Dominio técnico (4 pts):** Respuesta a preguntas, explicaciones
- **Propuestas futuras (3 pts):** Mejoras, extensiones, aplicaciones

---

## Hitos y Entregables

### Semana 1: Análisis Exploratorio

**Fecha límite:** Viernes de la primera semana

- **Entregable:** Notebook de EDA completo
- **Revisión:** Feedback inmediato sobre calidad de análisis
- **Peso:** 25% de la calificación final

### Semana 2-3: Modelado Predictivo

**Fecha límite:** Viernes de la tercera semana

- **Entregable:** Notebook de ML + modelos guardados
- **Revisión:** Evaluación técnica de implementación
- **Peso:** 35% de la calificación final

### Semana 4: Dashboard y Presentación

**Fecha límite:** Último día de clases

- **Entregable:** Dashboard + presentación + documentación
- **Presentación:** 15 minutos por estudiante
- **Peso:** 40% de la calificación final

---

## Preguntas de Investigación Sugeridas

Los estudiantes pueden elegir enfocar su proyecto en una o más de estas preguntas:

### Predicción y Rendimiento

1. ¿Qué factores determinan el resultado de un partido?
2. ¿Cómo predecir el rendimiento futuro de un jugador?
3. ¿Cuáles son los indicadores tempranos de declive en rendimiento?

### Análisis Táctico

1. ¿Cómo influye la táctica en los resultados?
2. ¿Qué patrones de juego son más efectivos?
3. ¿Cómo adaptar la estrategia según el rival?

### Análisis de Mercado

1. ¿Qué determina el valor de mercado de un jugador?
2. ¿Cuándo es el mejor momento para fichar/vender?
3. ¿Qué jugadores están sub/sobrevalorados?

### Análisis Temporal

1. ¿Cómo varía el rendimiento durante la temporada?
2. ¿Existen patrones estacionales en el fútbol?
3. ¿Cómo predecir rachas de buenos/malos resultados?

---

## Recursos y Soporte

### Documentación Técnica

- [Guía completa de Scikit-learn](https://scikit-learn.org/stable/)
- [Plotly para dashboards interactivos](https://plotly.com/python/)
- [Mejores prácticas de ML](https://developers.google.com/machine-learning/guides/rules-of-ml)

### Sesiones de Consulta

- **Martes y jueves:** 2:00-3:00 PM (Presencial)
- **Miércoles:** 6:00-7:00 PM (Virtual)
- **Por cita:** Disponible bajo solicitud

### Recursos Adicionales

- Datasets complementarios disponibles en Moodle
- Templates de código en el repositorio del curso
- Ejemplos de proyectos exitosos (años anteriores)
- Canal de Slack para dudas técnicas

---

## Criterios de Originalidad

### Se Fomenta

- Enfoques creativos e innovadores
- Análisis únicos o poco convencionales
- Implementaciones técnicas avanzadas
- Visualizaciones originales

### Se Penaliza

- Copia directa de código sin atribución
- Proyectos idénticos entre estudiantes
- Uso de herramientas no autorizadas (AutoML completo)
- Datasets externos sin aprobación previa

### Política de Integridad Académica

- Todo código debe ser original o debidamente citado
- Se permite consultar documentación oficial
- Se fomenta la discusión conceptual entre estudiantes
- Se prohíbe compartir código completo

---

## Cronograma Detallado

### Semana 1: Inmersión en Datos

| Día | Actividades | Recursos |
|-----|-------------|----------|
| L | Introducción al proyecto, formación de workspace | Configuración de entorno |
| M | Carga y exploración inicial de datos | Notebooks template |
| X | Análisis estadístico descriptivo | Consulta técnica |
| J | Limpieza de datos y detección de outliers | Tutorial de limpieza |
| V | **Entrega EDA** + Feedback inmediato | Revisión y comentarios |

### Semana 2: Construcción de Modelos

| Día | Actividades | Recursos |
|-----|-------------|----------|
| L | Preparación de datos para ML | Scikit-learn tutorial |
| M | Implementación de modelo baseline | Template de modelado |
| X | Modelos avanzados y tuning | Consulta especializada |
| J | Validación cruzada y métricas | Guía de evaluación |
| V | Interpretación y análisis de errores | Herramientas de interpretación |

### Semana 3: Refinamiento y Dashboard

| Día | Actividades | Recursos |
|-----|-------------|----------|
| L | Optimización final de modelos | Técnicas avanzadas |
| M | Inicio de dashboard interactivo | Plotly workshop |
| X | Desarrollo de funcionalidades | Widgets tutorial |
| J | Integración modelos-dashboard | Consulta técnica |
| V | **Entrega Modelos** + Testing de dashboard | Evaluación intermedia |

### Semana 4: Presentación y Finalización

| Día | Actividades | Recursos |
|-----|-------------|----------|
| L | Finalización de dashboard | Pulido final |
| M | Preparación de presentación | Templates de presentación |
| X | Documentación técnica | Guías de documentación |
| J | Ensayos de presentación | Feedback de compañeros |
| V | **Presentaciones finales** | Evaluación completa |

---

## Ejemplos de Excelencia

### Proyecto Destacado Anterior

**"PredicTOR: Sistema de Predicción para Liga MX"**

- Precisión del 78% en predicción de resultados
- Dashboard con 15+ visualizaciones interactivas
- Análisis de 50,000+ eventos de juego
- Recomendaciones implementadas por equipo real

### Características que lo Hicieron Sobresalir

1. **Innovación técnica:** Uso de redes neuronales simples
2. **Relevancia práctica:** Partnerships con clubes locales
3. **Calidad visual:** Interface profesional y intuitiva
4. **Impacto medible:** Mejora documentada en decisiones

---

*Este proyecto integrador representa la culminación del aprendizaje en el curso, donde los estudiantes demuestran su capacidad para aplicar Python de manera profesional en el análisis de datos deportivos.*
