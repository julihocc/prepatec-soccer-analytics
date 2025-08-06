# Ejercicio Semana 6: Introducción y Exploración de Datos

## Información General

**Bloque:** 2 - Fundamentos de Data Science  
**Semana:** 6  
**Tiempo estimado:** 60 minutos  
**Puntos totales:** 100 puntos  
**Fecha límite:** Final de la Semana 6  
**Archivo entrega:** `[matricula]-ejercicio-semana-6.ipynb`

## Objetivos de Aprendizaje

Al completar este ejercicio, el estudiante será capaz de:
- Cargar y explorar datasets deportivos utilizando pandas
- Realizar análisis exploratorio de datos (EDA) básico sistemático
- Identificar patrones iniciales en rendimiento de equipos europeos
- Aplicar métodos de inspección de datos estructurados
- Generar insights preliminares sobre competitividad futbolística

## Prerrequisitos

- Ejercicios del Bloque 1 (Semanas 1-5) completados exitosamente
- Dominio sólido de pandas y numpy
- Conocimiento de DataFrames y manipulación de datos
- Comprensión de estadísticas descriptivas básicas

## Contexto del Ejercicio

Eres el **analista de datos junior** del departamento de scouting del PSG. La dirección deportiva necesita un análisis inicial de la competencia europea para identificar:

- Patrones de rendimiento en las principales ligas
- Equipos con mejor relación rendimiento-presupuesto
- Oportunidades de mercado y benchmarking competitivo
- Tendencias que puedan influir en estrategias futuras

---

# Ejercicio Integrador: Análisis Exploratorio PSG Scouting

## Parte 1: Configuración y Carga de Datos (25 puntos)

### Objetivo
Configurar el entorno de análisis y realizar la primera exploración del dataset de equipos europeos.

### Instrucciones Detalladas

**Paso 1:** Configura tu entorno de trabajo:

```python
# Configuración del entorno de análisis
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración visual estándar para el PSG
sns.set_theme(style="whitegrid", palette="viridis")
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.size'] = 11

# Mensaje de bienvenida
print("=== CENTRO DE ANÁLISIS PSG ===")
print("Sistema de scouting europeo iniciado")
print("¡Herramientas de análisis listas!")
```

**Paso 2:** Carga y explora el dataset principal:

```python
# Cargar datos de equipos europeos temporada 2023-24
df_equipos = pd.read_csv('equipos-europa-2023-24.csv')

# TU CÓDIGO AQUÍ:
# 1. Mostrar las primeras 5 filas del dataset con .head()
# 2. Mostrar información general del dataset con .info()
# 3. Verificar las dimensiones con .shape
# 4. Mostrar los nombres de las columnas disponibles
# 5. Identificar tipos de datos de cada columna
# 6. Verificar si existen valores nulos con .isnull().sum()
# 7. Mostrar estadísticas descriptivas básicas con .describe()

print("Dataset de equipos europeos cargado exitosamente")
print(f"Analizando {len(df_equipos)} equipos de las principales ligas")
```

### Criterios de Evaluación
- **Configuración correcta del entorno** (8 puntos)
- **Carga exitosa de datos** (7 puntos)
- **Exploración inicial completa** (10 puntos)

---

## Parte 2: Análisis de Distribuciones por Liga (25 puntos)

### Objetivo
Analizar la distribución de equipos y rendimiento por liga para identificar patrones competitivos.

### Instrucciones Detalladas

**Paso 3:** Analiza la composición del dataset:

```python
# Análisis de distribución por liga

# TU CÓDIGO AQUÍ:
# 1. Mostrar todas las ligas únicas en el dataset
# 2. Contar el número de equipos por liga usando .value_counts()
# 3. Crear un DataFrame con estadísticas por liga:
#    - Promedio de puntos por liga
#    - Promedio de goles a favor por liga
#    - Promedio de goles en contra por liga
#    - Promedio de presupuesto por liga
# 4. Identificar la liga más competitiva (menor diferencia entre max y min puntos)
# 5. Encontrar la liga más goleadora (más goles promedio)
# 6. Calcular la eficiencia defensiva promedio por liga (goles_contra/partidos)

# Ejemplo de análisis requerido:
stats_por_liga = df_equipos.groupby('Liga').agg({
    'Puntos': ['mean', 'min', 'max'],
    'Goles_Favor': 'mean',
    'Goles_Contra': 'mean',
    'Presupuesto': 'mean'
}).round(2)

print("=== ANÁLISIS COMPETITIVO POR LIGA ===")
# Mostrar resultados con interpretación
```

**Paso 4:** Identifica equipos destacados:

```python
# Análisis de equipos extremos

# TU CÓDIGO AQUÍ:
# 1. Encontrar el equipo con más puntos en cada liga
# 2. Identificar el equipo más goleador de cada liga
# 3. Encontrar el equipo más defensivo (menos goles en contra) por liga
# 4. Calcular la relación goles_favor/goles_contra por equipo
# 5. Identificar equipos con mejor relación puntos/presupuesto
# 6. Crear ranking de los 5 equipos más eficientes económicamente

print("=== TOP EQUIPOS POR CATEGORÍA ===")
# Mostrar análisis con explicaciones
```

### Criterios de Evaluación
- **Análisis estadístico por liga correcto** (15 puntos)
- **Identificación de equipos destacados** (10 puntos)

---

## Parte 3: Análisis de Rendimiento y Eficiencia (25 puntos)

### Objetivo
Desarrollar métricas de rendimiento avanzadas para evaluación integral de equipos.

### Instrucciones Detalladas

**Paso 5:** Calcula métricas de rendimiento:

```python
# Creación de métricas avanzadas de rendimiento

# TU CÓDIGO AQUÍ:
# 1. Crear columnas calculadas:
#    - 'Diferencia_Goles': Goles_Favor - Goles_Contra
#    - 'Puntos_Por_Partido': Puntos / (Victorias + Empates + Derrotas)
#    - 'Efectividad_Ofensiva': Goles_Favor / (Victorias + Empates + Derrotas)
#    - 'Solidez_Defensiva': Goles_Contra / (Victorias + Empates + Derrotas)
#    - 'Eficiencia_Presupuesto': Puntos / (Presupuesto / 100)  # Puntos por cada 100M

# 2. Crear categorías de rendimiento:
#    - Clasificar equipos en "Elite", "Medio", "Bajo" según puntos
#    - Elite: > 80 puntos, Medio: 60-80 puntos, Bajo: < 60 puntos

# 3. Análisis de correlaciones básicas:
#    - Correlación entre Presupuesto y Puntos
#    - Correlación entre Goles_Favor y Victorias
#    - Correlación entre Diferencia_Goles y Puntos

df_equipos_mejorado = df_equipos.copy()
# Implementar cálculos aquí

print("=== MÉTRICAS DE RENDIMIENTO CALCULADAS ===")
```

**Paso 6:** Análisis comparativo de eficiencia:

```python
# Análisis de eficiencia económica y deportiva

# TU CÓDIGO AQUÍ:
# 1. Identificar equipos "sobrevalorados" (alto presupuesto, bajo rendimiento)
# 2. Encontrar equipos "chollos" (bajo presupuesto, alto rendimiento)
# 3. Calcular el "precio por punto" para cada equipo
# 4. Determinar qué liga ofrece mejor relación calidad-precio
# 5. Analizar si existe correlación directa presupuesto-éxito
# 6. Crear índice combinado de rendimiento (incluye múltiples factores)

# Criterios para análisis:
# - Sobrevalorado: Presupuesto > 600M y Puntos < 70
# - Chollo: Presupuesto < 300M y Puntos > 65
# - Eficiente: Top 5 en relación Puntos/Presupuesto

print("=== ANÁLISIS DE EFICIENCIA ECONÓMICA ===")
```

### Criterios de Evaluación
- **Métricas calculadas correctamente** (15 puntos)
- **Análisis de eficiencia completo** (10 puntos)

---

## Parte 4: Insights y Recomendaciones Estratégicas (25 puntos)

### Objetivo
Generar insights accionables para la dirección deportiva del PSG basados en el análisis exploratorio.

### Instrucciones Detalladas

**Paso 7:** Genera conclusiones estratégicas:

```python
# Síntesis de hallazgos para la dirección deportiva

# TU CÓDIGO AQUÍ:
# 1. Identificar la liga más competitiva para benchmarking
# 2. Determinar patrones de éxito en equipos similares al PSG
# 3. Analizar qué factores distinguen a equipos de elite
# 4. Evaluar oportunidades en mercado de equipos infravalorados
# 5. Proponer estrategia de inversión basada en datos
# 6. Identificar amenazas competitivas emergentes

# Estructura de análisis requerida:
print("=== REPORTE EJECUTIVO PSG SCOUTING ===")
print("\n1. LIGA MÁS COMPETITIVA:")
# Tu análisis aquí

print("\n2. EQUIPOS BENCHMARK (similar nivel al PSG):")
# Tu análisis aquí

print("\n3. FACTORES CLAVE DEL ÉXITO:")
# Tu análisis aquí

print("\n4. OPORTUNIDADES DE MERCADO:")
# Tu análisis aquí

print("\n5. RECOMENDACIONES ESTRATÉGICAS:")
# Tu análisis aquí
```

**Paso 8:** Prepara visualización ejecutiva:

```python
# Dashboard básico para presentación ejecutiva

# TU CÓDIGO AQUÍ:
# Crear un gráfico que combine múltiples insights:
# 1. Scatterplot: Presupuesto vs Puntos (tamaño = Goles_Favor)
# 2. Colorear puntos por Liga
# 3. Destacar al PSG si está en el dataset
# 4. Añadir línea de tendencia
# 5. Incluir anotaciones para equipos destacados
# 6. Títulos y etiquetas en español

plt.figure(figsize=(12, 8))
# Implementar visualización aquí

plt.title("Análisis Competitivo: Rendimiento vs Inversión en Fútbol Europeo", 
          fontsize=16, fontweight='bold')
plt.xlabel('Presupuesto (Millones €)')
plt.ylabel('Puntos Obtenidos')
plt.legend(title='Liga')
plt.grid(True, alpha=0.3)
plt.show()

print("Dashboard ejecutivo generado para la dirección deportiva")
```

### Criterios de Evaluación
- **Insights estratégicos relevantes** (15 puntos)
- **Visualización ejecutiva profesional** (10 puntos)

## Criterios de Evaluación General

### Correctitud Técnica (40 puntos)
- Código ejecuta sin errores
- Uso correcto de pandas y métodos de análisis
- Cálculos estadísticos precisos
- Implementación adecuada de todas las tareas

### Aplicación Práctica (30 puntos)
- Análisis relevante para contexto deportivo
- Insights útiles para toma de decisiones
- Interpretación correcta de resultados
- Aplicación efectiva al contexto PSG

### Claridad y Documentación (30 puntos)
- Código bien comentado en español
- Explicaciones claras de análisis
- Presentación profesional de resultados
- Variables con nombres descriptivos

## Instrucciones de Entrega

1. **Completa todas las partes** en orden secuencial
2. **Incluye interpretaciones** para cada análisis
3. **Verifica que el código ejecute** sin errores
4. **Guarda como:** `[matricula]-ejercicio-semana-6.ipynb`
5. **Entrega antes del final de Semana 6**

## Recursos de Apoyo

- Notebook de la Semana 6: `introduccion-exploracion.ipynb`
- Dataset: `equipos-europa-2023-24.csv` 
- Documentación pandas: Métodos `.head()`, `.info()`, `.describe()`, `.groupby()`

---

**¡Descubre los secretos del éxito en el fútbol europeo y guía al PSG hacia la excelencia!** ⚽�
