# Proyecto Integrador Final
## Sistema de Análisis Predictivo para Fútbol

**Modalidad:** Individual  
**Ponderación:** 30% de la calificación final  
**Duración:** 4 semanas  
**Entrega:** Jupyter Notebook (20%) + Presentación (10%)

---

## Descripción General

Este proyecto integrador constituye la evaluación final del curso, donde los estudiantes demostrarán su dominio completo de Python para análisis de datos deportivos. Cada estudiante desarrollará un sistema de análisis predictivo que combine todos los conocimientos adquiridos en los tres bloques.

---

## Contexto del Proyecto

Una empresa de análisis deportivo te ha contratado como Data Scientist Junior para desarrollar un prototipo de sistema predictivo para equipos de fútbol profesional. El sistema debe poder:

1. **Predecir resultados** de partidos próximos
2. **Evaluar rendimiento** de jugadores y equipos
3. **Identificar patrones** estacionales y tácticos
4. **Generar recomendaciones** basadas en datos

---

## Objetivos de Aprendizaje

Al completar este proyecto, el estudiante será capaz de:
- Integrar todos los conocimientos de programación Python del curso
- Aplicar técnicas de machine learning básico a datos deportivos
- Desarrollar un pipeline completo de análisis de datos
- Crear visualizaciones interactivas avanzadas
- Presentar resultados técnicos a audiencias diversas
- Demostrar pensamiento crítico y resolución de problemas

---

## Estructura del Proyecto

### Fase 1: Análisis Exploratorio Avanzado (25%)
**Duración:** Semana 1

#### Objetivos:
- Dominio completo de manipulación de datos
- Análisis estadístico profundo
- Identificación de patrones complejos

#### Entregables:
1. **Notebook de EDA:** `01_analisis_exploratorio.ipynb`
2. **Dataset limpio:** `datos_limpios.csv`
3. **Reporte de calidad:** `reporte_calidad_datos.md`

#### Tareas específicas:

**1.1 Carga y Validación de Datos Champions League**
```python
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings('ignore')

def cargar_datos_champions():
    """
    Función para cargar y validar datos de Champions League
    """
    # Cargar dataset de Champions League desde Kaggle
    url_dataset = "https://www.kaggle.com/datasets/julihocc/champs"
    
    # Validaciones específicas para Champions League:
    # - Verificar fases de competición (Grupos, 1/8, 1/4, 1/2, Final)
    # - Validar equipos participantes por temporada
    # - Confirmar integridad de resultados
    # Tu implementación aquí
    pass
```

**1.2 Análisis Estadístico Profundo**
- Distribuciones multivariadas
- Análisis de correlaciones complejas  
- Detección de outliers avanzada
- Tests de normalidad y homogeneidad

**1.3 Ingeniería de Features para Champions League**
- Crear variables derivadas específicas:
  - `diferencia_ranking_uefa`: Diferencia entre rankings de equipos
  - `experiencia_champions`: Número de participaciones previas
  - `racha_actual`: Victorias/derrotas consecutivas en la competición
  - `rendimiento_fase`: Estadísticas por fase de competición
- Métricas de rendimiento compuestas:
  - `indice_dominio_local`: Combinación de posesión, tiros y córners
  - `eficiencia_ofensiva`: Goles por tiro a puerta
  - `solidez_defensiva`: Goles concedidos vs tiros recibidos
- Variables de contexto temporal:
  - `dias_descanso`: Tiempo entre partidos
  - `momento_temporada`: Posición en calendario UEFA
- Indicadores históricos:
  - `historial_enfrentamientos`: Record directo entre equipos
  - `rendimiento_estadio`: Estadísticas como local/visitante

### Fase 2: Modelado Predictivo (35%)
**Duración:** Semana 2-3

#### Objetivos:
- Implementar algoritmos de machine learning
- Validar modelos correctamente
- Interpretar resultados predictivos

#### Entregables:
1. **Notebook de modelado:** `02_modelos_predictivos.ipynb`
2. **Modelos guardados:** `modelos/` (archivos .pkl)
3. **Métricas de evaluación:** `evaluacion_modelos.json`

#### Tareas específicas:

**2.1 Preparación para Machine Learning - Champions League**
```python
def preparar_datos_ml_champions(df):
    """
    Preparar datos específicos de Champions League para ML
    """
    # Codificación específica para Champions:
    # - One-hot encoding para fases de competición
    # - Label encoding para equipos (mantener jerarquía histórica)
    # - Encoding cíclico para fechas (seasonality effects)
    
    # Escalado de variables numéricas
    # División train/test estratificada por temporada
    # Manejo de desbalance: Champions vs eliminación
    
    # Variables objetivo específicas:
    # - clasificacion_resultado: Victoria/Empate/Derrota
    # - avanza_fase: Clasificación a siguiente ronda
    # - goles_prediccion: Número de goles esperados
    
    return X_train, X_test, y_train, y_test
```

**2.2 Implementación de Modelos para Champions League**
- **Regresión logística** para predicción de clasificación a siguiente fase
- **Random Forest** para identificar factores clave en victorias
- **Gradient Boosting** para predicción precisa de goles
- **Ensemble methods** para robustez en diferentes fases del torneo
- **Modelos específicos por fase:**
  - Modelo para fase de grupos (6 partidos por equipo)
  - Modelo para eliminatorias directas (ida y vuelta)
  - Modelo especializado para final (partido único)

**2.3 Evaluación y Validación Champions League**
- Cross-validation estratificada por temporadas
- Métricas específicas del fútbol:
  - Precisión en predicción de resultados exactos
  - Recall para identificar favoritos y sorpresas
  - F1-score balanceado para clasificación de equipos
  - ROC-AUC para probabilidad de avance de fase
- Matrices de confusión por tipo de partido:
  - Fase de grupos vs eliminatorias
  - Partidos de ida vs vuelta
  - Local vs visitante
- Análisis de errores contextual:
  - Factores no capturados por el modelo
  - Eventos inesperados (lesiones, expulsiones)
  - Sesgos por temporada o equipos específicos

### Fase 3: Dashboard Interactivo (25%)
**Duración:** Semana 3-4

#### Objetivos:
- Crear interfaz visual interactiva
- Implementar filtros y controles dinámicos
- Integrar predicciones en tiempo real

#### Entregables:
1. **Dashboard principal:** `03_dashboard_interactivo.ipynb`
2. **Módulos auxiliares:** `utils/dashboard_functions.py`
3. **Manual de usuario:** `manual_dashboard.md`

#### Tareas específicas:

**3.1 Componentes del Dashboard Champions League**
```python
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import ipywidgets as widgets
from IPython.display import display

def crear_dashboard_champions():
    """
    Dashboard interactivo específico para Champions League
    """
    # Panel de control con filtros Champions:
    # - Selector de temporada (2018-2024)
    # - Filtro por fase (Grupos, 1/8, 1/4, 1/2, Final)
    # - Selector de equipos participantes
    # - Filtro por país de origen
    
    # Visualizaciones específicas:
    # - Mapa interactivo de Europa con equipos
    # - Timeline de fases del torneo
    # - Árbol eliminatorio interactivo
    # - Comparador de rendimiento por fases
    
    # Predicciones en tiempo real:
    # - Simulador de eliminatorias
    # - Calculadora de probabilidades de avance
    # - Predictor de campeón
    pass
```

**3.2 Funcionalidades Específicas Champions League:**
- **Filtros interactivos Champions:**
  - Selector de temporada y fase del torneo
  - Filtro por equipos, países y confederaciones
  - Selector de tipo de análisis (histórico vs predictivo)
- **Simulador de Eliminatorias:** 
  - Entrada de equipos → predicción de resultados completos
  - Simulador de cuadro completo desde octavos hasta final
- **Comparador de Equipos Élite:** 
  - Visualización lado a lado de gigantes europeos
  - Análisis histórico de enfrentamientos directos
- **Timeline Champions:** 
  - Evolución de equipos a través de temporadas
  - Progresión de rendimiento por fases del torneo
- **Mapa Táctico Europeo:** 
  - Distribución geográfica de equipos participantes
  - Análisis de rendimiento por liga de origen
- **Predictor de Campeón:**
  - Probabilidades dinámicas basadas en rendimiento actual
  - Simulador Monte Carlo para múltiples escenarios

### Fase 4: Presentación y Documentación (15%)
**Duración:** Semana 4

#### Objetivos:
- Comunicar resultados efectivamente
- Demostrar dominio técnico
- Proponer mejoras futuras

#### Entregables:
1. **Presentación:** `presentacion_final.pdf` (máximo 15 diapositivas)
2. **Video demo:** `demo_dashboard.mp4` (máximo 5 minutos)
3. **Documentación técnica:** `documentacion_tecnica.md`
4. **README del proyecto:** `README.md`

---

## Dataset Proporcionado

### Dataset Principal: Champions League Matches
**Fuente:** [Kaggle - Champions League Matches](https://www.kaggle.com/datasets/julihocc/champs)

Este dataset contiene información detallada sobre partidos de la Liga de Campeones de la UEFA, proporcionando una excelente base para análisis predictivo y estadístico de fútbol de élite europea.

#### Características del Dataset:
- **Competición:** UEFA Champions League
- **Formato:** Archivo comprimido (ZIP)
- **Tipo de datos:** Estadísticas de partidos de fútbol profesional
- **Alcance:** Partidos de la competición más prestigiosa de clubes europeos

#### Datos Disponibles (estructura típica esperada):
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

#### Ventajas para el Análisis:
- **Nivel competitivo:** Equipos de máxima calidad europea
- **Contexto táctico:** Partidos de alta intensidad y planificación
- **Relevancia temporal:** Datos de competiciones recientes
- **Variedad de fases:** Desde fase de grupos hasta final

---

## Requisitos Técnicos

### Bibliotecas Obligatorias:
```python
# Análisis de datos
import pandas as pd
import numpy as np

# Visualización
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

# Machine Learning
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix

# Interactividad
import ipywidgets as widgets
from IPython.display import display

# Utilidades
import warnings
import json
import pickle
from datetime import datetime
```

### Estructura de Archivos Champions League:
```
proyecto_champions/
├── notebooks/
│   ├── 01_analisis_exploratorio_champions.ipynb
│   ├── 02_modelos_predictivos_champions.ipynb
│   └── 03_dashboard_champions.ipynb
├── data/
│   ├── raw/
│   │   └── champions_league_matches.csv    # Dataset de Kaggle
│   ├── processed/
│   │   ├── datos_limpios_champions.csv
│   │   ├── features_ingenieria.csv
│   │   └── estadisticas_por_fase.csv
│   └── external/
│       ├── rankings_uefa.csv              # Rankings históricos
│       └── info_equipos_europa.csv        # Datos adicionales
├── models/
│   ├── modelo_clasificacion_fase.pkl      # Predicción avance fase
│   ├── modelo_resultados_champions.pkl    # Predicción resultados
│   ├── modelo_goles_champions.pkl         # Predicción goles
│   └── metricas_evaluacion_champions.json
├── utils/
│   ├── champions_data_processing.py       # Procesamiento específico
│   ├── champions_visualization.py         # Visualizaciones temáticas
│   ├── eliminatorias_simulator.py        # Simulador de cuadros
│   └── model_utils_champions.py
├── docs/
│   ├── README.md
│   ├── manual_dashboard_champions.md
│   └── documentacion_tecnica_champions.md
└── presentation/
    ├── presentacion_final_champions.pdf
    └── demo_dashboard_champions.mp4
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

### Criterios Específicos por Fase:

#### Análisis Exploratorio (25 puntos):
- **Calidad de EDA (10 pts):** Exhaustividad, insights, visualizaciones
- **Limpieza de datos (8 pts):** Manejo de faltantes, outliers, inconsistencias
- **Ingeniería de features (7 pts):** Creatividad, relevancia, implementación

#### Modelado Predictivo (35 puntos):
- **Implementación técnica (15 pts):** Código correcto, buenas prácticas
- **Evaluación de modelos (10 pts):** Métricas apropiadas, validación cruzada
- **Interpretación (10 pts):** Análisis de resultados, importancia de variables

#### Dashboard Interactivo (25 puntos):
- **Funcionalidad (12 pts):** Filtros, predicciones, comparaciones
- **Diseño UX (8 pts):** Intuitividad, estética, navegación
- **Integración técnica (5 pts):** Conexión con modelos, rendimiento

#### Presentación (15 puntos):
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

### Predicción y Rendimiento:
1. ¿Qué factores determinan el resultado de un partido?
2. ¿Cómo predecir el rendimiento futuro de un jugador?
3. ¿Cuáles son los indicadores tempranos de declive en rendimiento?

### Análisis Táctico:
1. ¿Cómo influye la táctica en los resultados?
2. ¿Qué patrones de juego son más efectivos?
3. ¿Cómo adaptar la estrategia según el rival?

### Análisis de Mercado:
1. ¿Qué determina el valor de mercado de un jugador?
2. ¿Cuándo es el mejor momento para fichar/vender?
3. ¿Qué jugadores están sub/sobrevalorados?

### Análisis Temporal:
1. ¿Cómo varía el rendimiento durante la temporada?
2. ¿Existen patrones estacionales en el fútbol?
3. ¿Cómo predecir rachas de buenos/malos resultados?

---

## Recursos y Soporte

### Documentación Técnica:
- [Guía completa de Scikit-learn](https://scikit-learn.org/stable/)
- [Plotly para dashboards interactivos](https://plotly.com/python/)
- [Mejores prácticas de ML](https://developers.google.com/machine-learning/guides/rules-of-ml)

### Sesiones de Consulta:
- **Martes y jueves:** 2:00-3:00 PM (Presencial)
- **Miércoles:** 6:00-7:00 PM (Virtual)
- **Por cita:** Disponible bajo solicitud

### Recursos Adicionales:
- Datasets complementarios disponibles en Moodle
- Templates de código en el repositorio del curso
- Ejemplos de proyectos exitosos (años anteriores)
- Canal de Slack para dudas técnicas

---

## Criterios de Originalidad

### Se Fomenta:
- Enfoques creativos e innovadores
- Análisis únicos o poco convencionales
- Implementaciones técnicas avanzadas
- Visualizaciones originales

### Se Penaliza:
- Copia directa de código sin atribución
- Proyectos idénticos entre estudiantes
- Uso de herramientas no autorizadas (AutoML completo)
- Datasets externos sin aprobación previa

### Política de Integridad Académica:
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

### Proyecto Destacado Anterior:
**"PredicTOR: Sistema de Predicción para Liga MX"**
- Precisión del 78% en predicción de resultados
- Dashboard con 15+ visualizaciones interactivas
- Análisis de 50,000+ eventos de juego
- Recomendaciones implementadas por equipo real

### Características que lo Hicieron Sobresalir:
1. **Innovación técnica:** Uso de redes neuronales simples
2. **Relevancia práctica:** Partnerships con clubes locales
3. **Calidad visual:** Interface profesional y intuitiva
4. **Impacto medible:** Mejora documentada en decisiones

---

*Este proyecto integrador representa la culminación del aprendizaje en el curso, donde los estudiantes demuestran su capacidad para aplicar Python de manera profesional en el análisis de datos deportivos.*