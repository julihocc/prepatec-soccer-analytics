# Caso Práctico Colaborativo - Bloque 2
## Scouting y Análisis Táctico con Datos

**Modalidad:** Colaborativa (equipos de 3-4 estudiantes)  
**Ponderación:** 15% del 2do Parcial  
**Duración:** 2 semanas  
**Entrega:** Notebook de Jupyter + Dashboard interactivo + presentación

---

## Contexto del Problema

Una academia de fútbol profesional ha contratado a tu equipo como analistas de datos para crear un sistema de scouting (búsqueda de talentos) basado en estadísticas. Necesitan identificar patrones en el rendimiento de jugadores jóvenes para optimizar sus decisiones de reclutamiento.

**Situación:** La academia tiene datos históricos de múltiples torneos juveniles, pero necesita convertir esta información en insights accionables para sus scouts y entrenadores.

---

## Objetivos de Aprendizaje

Al completar este caso práctico, los estudiantes serán capaces de:
- Aplicar técnicas de exploración de datos en contextos deportivos
- Crear visualizaciones informativas con seaborn y matplotlib
- Realizar análisis estadístico descriptivo avanzado
- Identificar patrones y tendencias en datos deportivos
- Comunicar hallazgos técnicos a audiencias no técnicas

---

## Datasets Proporcionados

### Dataset Principal: `jugadores_liga_juvenil.csv`
```csv
jugador_id,nombre,edad,equipo,posicion,torneo,goles,asistencias,partidos_jugados,minutos_jugados,tiros_al_arco,precision_pases,recuperaciones,tarjetas_amarillas,tarjetas_rojas,valor_mercado_estimado
1,Alejandro Martínez,17,Atlas Sub-20,Delantero,Liga MX Sub-20,12,5,18,1425,45,78.5,23,2,0,150000
2,Sofia Hernández,16,Chivas Femenil,Mediocampo,Liga MX Femenil Sub-18,3,18,20,1650,15,89.2,78,3,0,200000
...
```

### Dataset de Partidos: `partidos_detalle.csv`
```csv
partido_id,fecha,equipo_local,equipo_visitante,goles_local,goles_visitante,competicion,asistencia
101,2023-09-15,Atlas Sub-20,América Sub-20,2,1,Liga MX Sub-20,5600
102,2023-09-16,Chivas Femenil,Tigres Femenil,0,2,Liga MX Femenil Sub-18,3200
...
```

### Dataset de Eventos: `eventos_partidos.csv`
```csv
evento_id,partido_id,minuto,jugador_id,tipo_evento,equipo,posicion_campo_x,posicion_campo_y
1,101,15,1,Gol,Atlas Sub-20,85.2,42.1
2,101,23,5,Tarjeta Amarilla,América Sub-20,45.8,28.3
...
```

---

## Tareas Requeridas

### Parte 1: Exploración y Limpieza de Datos (30 puntos)

#### 1.1 Configuración y Carga de Datos (5 puntos)
```python
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# Configuración de seaborn para gráficos profesionales
sns.set_theme(style="whitegrid", palette="Set2")
plt.rcParams['figure.figsize'] = (12, 8)
```

#### 1.2 Análisis Exploratorio de Datos (15 puntos)

**a) Análisis de distribuciones:**
- Distribución de edades por posición
- Distribución de goles por equipo y competición
- Análisis de valores atípicos (outliers) en rendimiento

**b) Análisis de tipos de datos:**
- Identificar y clasificar variables categóricas vs numéricas
- Detectar y manejar valores faltantes
- Validar consistencia entre datasets

**Código requerido:**
```python
def analizar_dataset(df, nombre_dataset):
    """
    Función para análisis exploratorio estandarizado
    """
    print(f"=== ANÁLISIS DE {nombre_dataset.upper()} ===")
    print(f"Dimensiones: {df.shape}")
    print(f"Columnas: {list(df.columns)}")
    print(f"Valores faltantes por columna:")
    print(df.isnull().sum())
    print(f"Estadísticas descriptivas:")
    print(df.describe())
    return df.info()
```

#### 1.3 Limpieza de Datos (10 puntos)
- Manejar valores faltantes de manera apropiada
- Normalizar nombres de equipos y posiciones
- Crear variables derivadas (ej: goles_por_partido, eficiencia_tiros)
- Validar rangos lógicos (edades, minutos jugados, etc.)

### Parte 2: Análisis Estadístico Avanzado (40 puntos)

#### 2.1 Estadística Descriptiva por Categorías (15 puntos)

**a) Análisis por posición:**
```python
def analizar_por_posicion(df):
    """
    Análisis comparativo de rendimiento por posición
    """
    stats_posicion = df.groupby('posicion').agg({
        'goles': ['mean', 'median', 'std'],
        'asistencias': ['mean', 'median'],
        'precision_pases': 'mean',
        'edad': 'mean',
        'valor_mercado_estimado': 'mean'
    }).round(2)
    
    return stats_posicion
```

**b) Análisis temporal:**
- Evolución del rendimiento por mes/torneo
- Identificar tendencias estacionales
- Comparar rendimiento en diferentes competiciones

#### 2.2 Análisis de Correlaciones (10 puntos)
- Matriz de correlación entre métricas de rendimiento
- Identificar qué factores predicen mejor el valor de mercado
- Analizar relación entre estadísticas defensivas y ofensivas

#### 2.3 Identificación de Patrones (15 puntos)

**a) Perfiles de jugadores:**
- Crear clusters básicos de tipos de jugadores
- Identificar jugadores "subestimados" vs "sobrevalorados"
- Detectar talentos emergentes

**b) Análisis táctico:**
- Mapas de calor de eventos por posición en el campo
- Análisis de efectividad por zona del campo
- Patrones de juego por equipo

### Parte 3: Visualización de Datos (20 puntos)

#### 3.1 Visualizaciones Exploratorias (10 puntos)

**Gráficos requeridos:**
```python
# 1. Dashboard de rendimiento por posición
fig, axes = plt.subplots(2, 2, figsize=(15, 10))

# Gráfico 1: Distribución de goles por posición
sns.boxplot(data=df_jugadores, x='posicion', y='goles', ax=axes[0,0])
axes[0,0].set_title('Distribución de Goles por Posición')
axes[0,0].tick_params(axis='x', rotation=45)

# Gráfico 2: Relación edad vs valor de mercado
sns.scatterplot(data=df_jugadores, x='edad', y='valor_mercado_estimado', 
                hue='posicion', ax=axes[0,1])
axes[0,1].set_title('Edad vs Valor de Mercado')

# Gráfico 3: Heatmap de correlaciones
correlation_matrix = df_jugadores.select_dtypes(include=[np.number]).corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', 
            center=0, ax=axes[1,0])
axes[1,0].set_title('Matriz de Correlaciones')

# Gráfico 4: Top 10 goleadores
top_goleadores = df_jugadores.nlargest(10, 'goles')
sns.barplot(data=top_goleadores, x='goles', y='nombre', ax=axes[1,1])
axes[1,1].set_title('Top 10 Goleadores')

plt.tight_layout()
plt.show()
```

#### 3.2 Visualizaciones Avanzadas (10 puntos)

**a) Mapa de calor de eventos:**
- Visualizar donde ocurren más goles, faltas, etc.
- Usar datos de posición en el campo

**b) Dashboard interactivo:**
- Filtros por equipo, posición, edad
- Comparación de múltiples jugadores
- Métricas personalizables

### Parte 4: Insights y Recomendaciones (10 puntos)

#### 4.1 Análisis de Scouting
**Preguntas a responder:**
1. ¿Qué perfil de jugador ofrece mejor relación calidad-precio?
2. ¿En qué posiciones hay más talento disponible?
3. ¿Qué equipos desarrollan mejor a sus juveniles?
4. ¿Cuáles son los indicadores tempranos de éxito?

#### 4.2 Recomendaciones Estratégicas
- Lista de 5 jugadores prioritarios para scouting
- Estrategias de reclutamiento por posición
- Benchmarks de rendimiento para evaluación
- Indicadores de alerta temprana

---

## Entregables

### 1. Notebook Principal (`scouting_analysis_equipo[X].ipynb`)
- **Sección 1:** Exploración y limpieza de datos
- **Sección 2:** Análisis estadístico completo
- **Sección 3:** Visualizaciones profesionales
- **Sección 4:** Insights y recomendaciones
- **Sección 5:** Conclusiones y próximos pasos

### 2. Dashboard Interactivo (`dashboard_equipo[X].ipynb`)
- Widgets interactivos para filtros
- Comparación visual de jugadores
- Métricas clave actualizables
- Interfaz intuitiva para scouts

### 3. Presentación Ejecutiva (`presentacion_scouting_equipo[X].pdf`)
- 10-12 diapositivas máximo
- Enfoque en insights accionables
- Visualizaciones claras y profesionales
- Recomendaciones específicas

### 4. Reporte de Scouting (`reporte_scouting_equipo[X].pdf`)
- Formato profesional de scouting
- Top 10 jugadores recomendados
- Análisis de fortalezas y debilidades
- Estrategias de aproximación

---

## Criterios de Evaluación

### Rúbrica Detallada (100 puntos total)

| Criterio | Peso | Excelente (90-100%) | Bueno (80-89%) | Suficiente (70-79%) | Insuficiente (<70%) |
|----------|------|-------------------|----------------|-------------------|-------------------|
| **Exploración de Datos** | 30% | Análisis exhaustivo, manejo correcto de datos faltantes | Análisis completo con pequeñas omisiones | Análisis básico pero correcto | Análisis superficial o incorrecto |
| **Visualizaciones** | 25% | Gráficos profesionales, informativos e innovadores | Visualizaciones claras y bien ejecutadas | Gráficos básicos pero funcionales | Visualizaciones pobres o confusas |
| **Análisis Estadístico** | 25% | Uso correcto de estadística, insights profundos | Análisis correcto con interpretación adecuada | Estadísticas básicas correctas | Errores en análisis o interpretación |
| **Trabajo Colaborativo** | 10% | Participación equitativa evidente | Buena colaboración documentada | Colaboración básica | Falta evidencia de trabajo en equipo |
| **Comunicación** | 10% | Presentación excepcional, narrativa clara | Buena comunicación de resultados | Presentación básica pero clara | Comunicación deficiente |

### Criterios Específicos de Evaluación:

#### Técnicos (60%):
- **Código limpio y funcional:** Sin errores, bien documentado
- **Uso apropiado de librerías:** seaborn, pandas, numpy
- **Análisis estadístico correcto:** Interpretación adecuada
- **Visualizaciones efectivas:** Claras, informativas, profesionales

#### Aplicados (40%):
- **Relevancia deportiva:** Insights útiles para scouting
- **Pensamiento crítico:** Análisis más allá de lo obvio
- **Comunicación efectiva:** Audiencia no técnica
- **Trabajo colaborativo:** Evidencia de coordinación

---

## Cronograma Sugerido

### Semana 1: Exploración y Análisis
| Día | Actividades | Responsabilidad |
|-----|-------------|----------------|
| 1-2 | Formación de equipos, exploración inicial de datos | Equipo completo |
| 3-4 | Limpieza de datos y análisis exploratorio | Dividir por datasets |
| 5-6 | Análisis estadístico descriptivo | Especialización por área |
| 7 | Integración de resultados parciales | Equipo completo |

### Semana 2: Visualización y Presentación
| Día | Actividades | Responsabilidad |
|-----|-------------|----------------|
| 1-2 | Creación de visualizaciones avanzadas | Dividir por tipos de gráficos |
| 3-4 | Desarrollo del dashboard interactivo | Programación colaborativa |
| 5-6 | Preparación de presentación y reportes | División de roles |
| 7 | Presentaciones finales | Equipo completo |

---

## Recursos Técnicos

### Bibliotecas Avanzadas Permitidas:
```python
# Visualización avanzada
import plotly.express as px
import plotly.graph_objects as go

# Widgets interactivos
from ipywidgets import interact, widgets
from IPython.display import display

# Análisis geoespacial básico (para mapas de calor)
import matplotlib.patches as patches
```

### Templates de Código:

#### 1. Dashboard Interactivo:
```python
# Widget para seleccionar posición
@interact
def analizar_posicion(posicion=list(df_jugadores['posicion'].unique())):
    datos_filtrados = df_jugadores[df_jugadores['posicion'] == posicion]
    
    fig, ax = plt.subplots(1, 2, figsize=(15, 6))
    
    # Gráfico 1: Distribución de goles
    ax[0].hist(datos_filtrados['goles'], bins=10, alpha=0.7)
    ax[0].set_title(f'Distribución de Goles - {posicion}')
    
    # Gráfico 2: Scatter plot edad vs valor
    ax[1].scatter(datos_filtrados['edad'], datos_filtrados['valor_mercado_estimado'])
    ax[1].set_title(f'Edad vs Valor - {posicion}')
    
    plt.tight_layout()
    plt.show()
    
    # Estadísticas resumidas
    print(f"Estadísticas de {posicion}:")
    print(datos_filtrados[['goles', 'asistencias', 'edad']].describe())
```

#### 2. Mapa de Calor de Campo:
```python
def crear_mapa_campo_eventos(df_eventos, tipo_evento='Gol'):
    # Filtrar eventos específicos
    eventos_filtrados = df_eventos[df_eventos['tipo_evento'] == tipo_evento]
    
    # Crear figura del campo
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Dibujar campo de fútbol básico
    field = patches.Rectangle((0, 0), 100, 68, linewidth=2, 
                             edgecolor='white', facecolor='green', alpha=0.3)
    ax.add_patch(field)
    
    # Agregar eventos como puntos de calor
    scatter = ax.scatter(eventos_filtrados['posicion_campo_x'], 
                        eventos_filtrados['posicion_campo_y'],
                        c='red', alpha=0.6, s=50)
    
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 68)
    ax.set_title(f'Mapa de Calor: {tipo_evento}s')
    ax.set_xlabel('Posición X (0-100)')
    ax.set_ylabel('Posición Y (0-68)')
    
    plt.show()
```

---

## Preguntas Guía para el Desarrollo

### Exploración de Datos:
1. ¿Qué patrones veo en la distribución de edades por posición?
2. ¿Hay correlación entre el valor de mercado y las estadísticas de rendimiento?
3. ¿Qué posiciones tienen mayor variabilidad en su rendimiento?

### Análisis Estadístico:
1. ¿Cuáles son los benchmarks de rendimiento por posición y edad?
2. ¿Qué jugadores están por encima/debajo de su rendimiento esperado?
3. ¿Hay diferencias significativas entre competiciones?

### Visualización:
1. ¿Cómo puedo mostrar múltiples dimensiones de datos simultáneamente?
2. ¿Qué tipo de gráfico comunica mejor cada insight?
3. ¿Cómo hago que mis visualizaciones sean intuitivas para no-técnicos?

### Aplicación Práctica:
1. ¿Qué información es más valiosa para un scout profesional?
2. ¿Cómo balanceo rendimiento actual vs potencial futuro?
3. ¿Qué indicadores de alerta temprana puedo identificar?

---

## Evaluación por Pares

Como parte de la experiencia colaborativa, cada equipo evaluará a otro equipo usando la siguiente rúbrica:

### Criterios de Evaluación entre Pares (10 puntos bonus):
- **Originalidad del análisis:** ¿Encontraron insights únicos?
- **Calidad técnica:** ¿El código es robusto y eficiente?
- **Presentación:** ¿Comunicaron efectivamente sus hallazgos?
- **Relevancia práctica:** ¿Sus recomendaciones son accionables?

---

*Este caso práctico está diseñado para aplicar todas las técnicas de exploración de datos aprendidas en el Bloque 2, mientras se desarrollan habilidades colaborativas y de comunicación esenciales para analistas de datos profesionales.*