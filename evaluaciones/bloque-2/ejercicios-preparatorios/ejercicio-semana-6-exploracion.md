# Ejercicio Semana 6: Introducción y Exploración de Datos Deportivos

## Información del Ejercicio

**Bloque:** 2 - Fundamentos de Data Science  
**Peso:** 12% de la calificación del bloque (60% ÷ 5 ejercicios)  
**Tiempo estimado:** 2-2.5 horas  
**Entrega:** Final de Semana 6

## Objetivos

Al completar este ejercicio, serás capaz de:

- Cargar y explorar datasets deportivos reales
- Realizar análisis exploratorio de datos (EDA) básico
- Identificar patrones y anomalías en datos de fútbol
- Aplicar técnicas de limpieza de datos básicas
- Generar primeros insights sobre rendimiento deportivo

## Configuración Inicial

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Configurar estilo
sns.set_theme(style="whitegrid", palette="viridis")
plt.rcParams['figure.figsize'] = (10, 6)

# Cargar datos
df_equipos = pd.read_csv('equipos-europa-2023-24.csv')
df_jugadores = pd.read_csv('jugadores-estrellas-2024.csv')

print("¡Datos cargados y listos para explorar!")
```

## Ejercicio 1: Exploración Inicial de Datos (20 puntos)

### Parte A: Primeras Impresiones del Dataset

```python
# Usar el dataset de equipos europeos

# Tu código aquí:
# 1. Mostrar las primeras 5 filas del dataset
# 2. Mostrar información general con .info()
# 3. Mostrar estadísticas descriptivas con .describe()
# 4. Verificar el shape del dataset (filas y columnas)
# 5. Mostrar los nombres de todas las columnas
# 6. Verificar tipos de datos de cada columna
# 7. Identificar si hay valores faltantes
```

### Parte B: Análisis de Distribuciones

```python
# Continuando con el dataset de equipos

# Tu código aquí:
# 1. Mostrar todas las ligas únicas en el dataset
# 2. Contar cuántos equipos hay por liga
# 3. Calcular estadísticas básicas por liga (promedio de puntos, goles)
# 4. Identificar el equipo con más puntos y el que tiene menos
# 5. Encontrar el equipo más goleador y el más defensivo
# 6. Calcular la diferencia de goles promedio por liga
# 7. Mostrar el rango de presupuestos (mínimo y máximo)
```

### Respuesta Parte A

*Completa la exploración inicial del dataset de equipos.*

### Respuesta Parte B

*Completa el análisis de distribuciones y estadísticas básicas.*

## Ejercicio 2: Análisis Exploratorio de Jugadores (20 puntos)

### Tareas de Exploración

```python
# Usar el dataset de jugadores estrella

# Tu código aquí:
# 1. Explorar la distribución de edades de los jugadores
# 2. Analizar la distribución de posiciones
# 3. Calcular estadísticas por posición (promedio de goles, asistencias)
# 4. Identificar jugadores con mejor ratio goles/partido
# 5. Encontrar correlaciones entre edad, goles y valor de mercado
# 6. Comparar salarios promedio por liga
# 7. Identificar outliers en valor de mercado y salarios
# 8. Analizar qué ligas tienen jugadores más caros
```

### Visualizaciones Básicas

```python
# Crear visualizaciones exploratorias

# Tu código aquí:
# 1. Histograma de distribución de edades
# 2. Gráfico de barras de jugadores por posición
# 3. Boxplot de goles por posición
# 4. Scatterplot edad vs valor de mercado
# 5. Barplot de salario promedio por liga
# 6. Heatmap de correlaciones entre variables numéricas
```

### Respuesta

*Completa el análisis exploratorio completo de jugadores.*

## Ejercicio 3: Limpieza y Preparación de Datos (20 puntos)

### Detección de Problemas

```python
# Simular algunos problemas comunes en datos reales
# (En un caso real, estos problemas ya estarían en los datos)

# Crear una copia del dataset para practicar limpieza
df_jugadores_sucio = df_jugadores.copy()

# Simular problemas típicos:
# 1. Introducir algunos valores faltantes
df_jugadores_sucio.loc[5, 'Goles'] = np.nan
df_jugadores_sucio.loc[12, 'Asistencias'] = np.nan

# 2. Inconsistencias en nombres de posiciones
df_jugadores_sucio.loc[2, 'Posicion'] = 'DELANTERO'  # Mayúsculas
df_jugadores_sucio.loc[8, 'Posicion'] = 'defensa'    # Minúsculas

# 3. Valores atípicos simulados
df_jugadores_sucio.loc[1, 'Edad'] = 55  # Edad imposible

# Tu código aquí:
# 1. Identificar todos los valores faltantes
# 2. Detectar inconsistencias en nombres de posiciones
# 3. Encontrar valores atípicos usando estadísticas (IQR, z-score)
# 4. Crear estrategias para manejar cada problema
# 5. Implementar la limpieza paso a paso
# 6. Verificar que la limpieza fue exitosa
# 7. Comparar dataset original vs limpio
```

### Respuesta

*Completa la detección y limpieza de problemas en los datos.*

## Ejercicio 4: Análisis Comparativo por Liga (20 puntos)

### Análisis Multidimensional

```python
# Combinar análisis de equipos y jugadores

# Tu código aquí:
# 1. Calcular métricas promedio por liga usando ambos datasets
# 2. Determinar qué liga es más competitiva (menor diferencia entre equipos)
# 3. Analizar correlación entre presupuesto de equipos y valor de jugadores
# 4. Identificar patrones de edad por liga
# 5. Comparar estilos de juego (ofensivo vs defensivo) por liga
# 6. Crear un ranking de ligas basado en múltiples criterios
```

### Análisis de Tendencias

```python
# Buscar patrones interesantes

# Tu código aquí:
# 1. ¿Los equipos con mayor presupuesto siempre tienen mejores resultados?
# 2. ¿Hay relación entre la edad promedio del equipo y el rendimiento?
# 3. ¿Qué posición marca más goles en promedio?
# 4. ¿Los jugadores más caros son siempre los más efectivos?
# 5. Crear un "índice de eficiencia" combinando múltiples métricas
# 6. Identificar el mejor jugador por posición según criterios múltiples
```

### Respuesta

*Completa el análisis comparativo y de tendencias.*

## Ejercicio 5: Dashboard Exploratorio (20 puntos)

### Creación de Dashboard Integrado

```python
# Crear un dashboard completo con múltiples análisis

# Tu código aquí:
# Usar plt.subplots() para crear un dashboard con 6 paneles:

# Panel 1: Distribución de equipos por puntos (histogram)
# Panel 2: Top 10 jugadores por valor de mercado (barplot horizontal)
# Panel 3: Correlación edad vs rendimiento por posición (scatterplot)
# Panel 4: Comparación de ligas por múltiples métricas (radar chart o barplot agrupado)
# Panel 5: Distribución de presupuestos por liga (boxplot)
# Panel 6: Tendencia: presupuesto vs puntos obtenidos (scatterplot con línea de tendencia)

# Requisitos:
# - Títulos descriptivos en español
# - Colores consistentes y profesionales
# - Leyendas apropiadas
# - Anotaciones explicativas
# - Layout organizado y atractivo
```

### Insights y Conclusiones

```python
# Generar insights basados en tu análisis

# Tu código aquí:
# 1. Resumir los 3 hallazgos más importantes
# 2. Identificar patrones sorprendentes
# 3. Proponer hipótesis para investigación futura
# 4. Recomendar acciones basadas en datos
# 5. Evaluar limitaciones del análisis
# 6. Sugerir datos adicionales que serían útiles
```

### Respuesta

*Completa el dashboard y proporciona insights profesionales.*

## Ejercicio Bonus: Análisis de Eficiencia Económica (10 puntos extra)

### Análisis Avanzado

**Ejercicio opcional para puntos adicionales:**

```python
# Análisis sofisticado de relación costo-beneficio

# Tu código aquí:
# 1. Crear métrica "Puntos por Euro" para equipos
# 2. Calcular "Goles por Euro de Salario" para jugadores
# 3. Identificar equipos y jugadores más eficientes económicamente
# 4. Crear modelo simple de predicción de rendimiento basado en presupuesto
# 5. Analizar si el dinero garantiza éxito en el fútbol
# 6. Proponer estrategias de inversión basadas en datos

# Usar técnicas como:
# - Análisis de regresión simple
# - Clustering básico de equipos/jugadores
# - Normalización de métricas
# - Análisis de outliers interesantes
```

### Respuesta Bonus

*Ejercicio opcional: Crea análisis económico avanzado del fútbol.*

## Criterios de Evaluación

### Exploración de Datos (35%)

- [ ] Uso correcto de métodos exploratorios de pandas (15%)
- [ ] Identificación apropiada de patrones y anomalías (10%)
- [ ] Análisis estadístico básico correcto (10%)

### Limpieza de Datos (25%)

- [ ] Detección efectiva de problemas en datos (10%)
- [ ] Aplicación de técnicas de limpieza apropiadas (15%)

### Análisis e Interpretación (40%)

- [ ] Insights relevantes y bien fundamentados (20%)
- [ ] Visualizaciones efectivas y profesionales (10%)
- [ ] Conclusiones lógicas basadas en evidencia (10%)

## Instrucciones de Entrega

1. **Completa todos los ejercicios** en este notebook
2. **Incluye interpretaciones** para cada análisis realizado
3. **Asegúrate de que todo el código ejecute** sin errores
4. **Guarda como:** `ejercicio-semana-6-[tu-apellido].ipynb`
5. **Entrega antes del final de Semana 6**

## Recursos de Apoyo

- Notebook de la Semana 6: `introduccion-exploracion.ipynb`
- Datasets: `equipos-europa-2023-24.csv`, `jugadores-estrellas-2024.csv`
- Documentación pandas: <https://pandas.pydata.org/docs/user_guide/10min.html>
- Guía de EDA: <https://pandas.pydata.org/docs/user_guide/basics.html>

---

**¡Descubre los secretos ocultos en los datos del fútbol mundial!** ⚽🔍
