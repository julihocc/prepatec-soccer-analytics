# Información General

**Tema:** Pandas y NumPy para Análisis Deportivo  
**Semana:** 4  
**Bloque:** 1 - Prerrequisitos de Programación  
**Tiempo estimado:** 60 minutos  
**Puntos totales:** 100 puntos  
**Fecha límite:** Final de la Semana 4  
**Archivo entrega:** `[matricula]-ejercicio-semana-4.ipynb`

## Objetivos de Aprendizaje

Al finalizar este ejercicio, el estudiante será capaz de:

1. **Manipular DataFrames** de Pandas para análisis de datos deportivos
2. **Realizar operaciones estadísticas** con NumPy de manera eficiente
3. **Filtrar y agrupar datos** para obtener insights específicos
4. **Combinar datasets** usando merge y join para análisis integrales
5. **Generar estadísticas avanzadas** para toma de decisiones deportivas

## Prerrequisitos

- Ejercicios de las Semanas 1, 2 y 3 completados exitosamente
- Conocimiento sólido de funciones y estructuras de control
- Comprensión de listas y diccionarios
- Instalación de pandas y numpy en el entorno de trabajo

## Contexto del Ejercicio

Eres el **analista de datos senior** del Atlético de Madrid. La dirección deportiva necesita un análisis profundo de:

- Rendimiento individual y colectivo de jugadores
- Comparación con equipos rivales de La Liga
- Patrones de goles y asistencias por temporada
- Identificación de oportunidades de fichajes

---

# Ejercicio Integrador: Centro de Análisis de Datos Atlético Madrid

## Parte 1: Construcción y Análisis de DataFrame Principal (25 puntos)

### Objetivo
Crear y manipular un DataFrame completo con datos de la plantilla del Atlético Madrid.

### Instrucciones Detalladas

```python
import pandas as pd
import numpy as np

# Datos de la plantilla 2023-24 del Atlético Madrid
datos_plantilla = {
    'nombre': ['Jan Oblak', 'Koke', 'Antoine Griezmann', 'José Giménez', 'Marcos Llorente',
               'Álvaro Morata', 'João Félix', 'Stefan Savić', 'Yannick Carrasco', 'Diego Simeone Jr'],
    'posicion': ['Portero', 'Centrocampista', 'Delantero', 'Defensa', 'Centrocampista',
                'Delantero', 'Delantero', 'Defensa', 'Extremo', 'Centrocampista'],
    'edad': [31, 32, 33, 29, 29, 31, 24, 33, 30, 23],
    'partidos_jugados': [35, 38, 36, 32, 35, 34, 28, 31, 33, 15],
    'goles': [0, 3, 16, 2, 5, 13, 8, 1, 7, 1],
    'asistencias': [0, 5, 6, 1, 3, 2, 3, 0, 4, 2],
    'minutos_totales': [3150, 3230, 3060, 2720, 2975, 2890, 2240, 2635, 2805, 945],
    'tarjetas_amarillas': [2, 8, 4, 7, 6, 5, 3, 6, 4, 1],
    'tarjetas_rojas': [0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
    'salario_mensual': [900000, 250000, 800000, 180000, 220000, 350000, 600000, 160000, 280000, 45000]
}

# TU CÓDIGO AQUÍ:

# 1. Crear el DataFrame 'df_atletico'
df_atletico = pd.DataFrame(datos_plantilla)

# 2. Exploración inicial del DataFrame:
#    - Mostrar información general (.info())
#    - Mostrar estadísticas descriptivas (.describe())
#    - Verificar si hay valores nulos (.isnull())

# 3. Crear nuevas columnas calculadas:
#    - 'goles_por_partido': goles / partidos_jugados
#    - 'asistencias_por_partido': asistencias / partidos_jugados
#    - 'contribucion_total': goles + asistencias
#    - 'minutos_por_partido': minutos_totales / partidos_jugados
#    - 'efectividad': (goles + asistencias) / (minutos_totales / 90)

# 4. Análisis por posición:
#    - Agrupar por posición y calcular promedio de goles
#    - Encontrar la posición más disciplinada (menos tarjetas)
#    - Calcular el salario promedio por posición

# 5. Ranking de jugadores:
#    - Top 3 goleadores del equipo
#    - Top 3 asistentes del equipo
#    - Top 3 con mejor efectividad (min. 1000 minutos)
```

### Criterios de Evaluación
- **DataFrame creado correctamente** (8 puntos)
- **Columnas calculadas precisas** (10 puntos)
- **Análisis por posición completo** (7 puntos)

---

## Parte 2: Análisis Estadístico con NumPy (25 puntos)

### Objetivo
Utilizar NumPy para realizar cálculos estadísticos avanzados y detectar patrones de rendimiento.

### Instrucciones Detalladas

```python
# TU CÓDIGO AQUÍ usando NumPy:

# 1. Convertir columnas numéricas a arrays de NumPy:
goles_array = np.array(df_atletico['goles'])
asistencias_array = np.array(df_atletico['asistencias'])
minutos_array = np.array(df_atletico['minutos_totales'])
salarios_array = np.array(df_atletico['salario_mensual'])

# 2. Estadísticas descriptivas avanzadas:
#    - Media, mediana, desviación estándar de goles
#    - Percentiles 25, 50, 75 de asistencias
#    - Coeficiente de variación de salarios (std/mean)
#    - Correlación entre goles y asistencias usando np.corrcoef()

# 3. Análisis de distribución:
#    - Crear histograma de goles (usar np.histogram())
#    - Identificar outliers en salarios (valores > mean + 2*std)
#    - Calcular el rango intercuartílico de minutos jugados

# 4. Operaciones vectorizadas:
#    - Crear array 'rendimiento_normalizado' = (goles + asistencias) / max(goles + asistencias)
#    - Calcular índice de eficiencia = minutos_totales / (goles + asistencias + 1)
#    - Determinar qué jugadores están por encima de la media en goles Y asistencias

# 5. Simulación estadística:
#    - Simular 1000 partidos donde cada jugador tiene probabilidad 
#      (goles_por_partido/3) de marcar en cada partido
#    - Calcular goles esperados en 10 partidos para cada jugador
#    - Comparar con goles reales y encontrar diferencias

# 6. Matriz de análisis:
#    - Crear matriz 2D con filas=jugadores, columnas=[goles, asistencias, minutos]
#    - Calcular la suma de cada fila (contribución total)
#    - Encontrar el jugador con máxima contribución usando np.argmax()
```

### Criterios de Evaluación
- **Estadísticas descriptivas correctas** (10 puntos)
- **Operaciones vectorizadas apropiadas** (10 puntos)
- **Análisis de correlación y simulación** (5 puntos)

---

## Parte 3: Comparación con Equipos Rivales (25 puntos)

### Objetivo
Comparar el rendimiento del Atlético Madrid con otros equipos de La Liga usando DataFrames múltiples.

### Instrucciones Detalladas

```python
# Datos de equipos rivales para comparación
datos_real_madrid = {
    'equipo': 'Real Madrid',
    'goles_favor': 87,
    'goles_contra': 34,
    'partidos_jugados': 38,
    'victorias': 26,
    'empates': 8,
    'derrotas': 4,
    'puntos': 86
}

datos_barcelona = {
    'equipo': 'Barcelona', 
    'goles_favor': 76,
    'goles_contra': 37,
    'partidos_jugados': 38,
    'victorias': 22,
    'empates': 10,
    'derrotas': 6,
    'puntos': 76
}

datos_atletico_equipo = {
    'equipo': 'Atlético Madrid',
    'goles_favor': 68,
    'goles_contra': 33,
    'partidos_jugados': 38,
    'victorias': 20,
    'empates': 8,
    'derrotas': 10,
    'puntos': 68
}

# TU CÓDIGO AQUÍ:

# 1. Crear DataFrame de comparación:
df_liga = pd.DataFrame([datos_real_madrid, datos_barcelona, datos_atletico_equipo])

# 2. Calcular métricas derivadas para cada equipo:
#    - 'goles_promedio_favor': goles_favor / partidos_jugados
#    - 'goles_promedio_contra': goles_contra / partidos_jugados  
#    - 'diferencia_goles': goles_favor - goles_contra
#    - 'porcentaje_victorias': (victorias / partidos_jugados) * 100
#    - 'puntos_por_partido': puntos / partidos_jugados

# 3. Análisis comparativo:
#    - Ranking de equipos por diferencia de goles
#    - Equipo más goleador y más sólido defensivamente
#    - Calcular qué tan cerca está el Atlético del líder en cada métrica

# 4. Análisis de eficiencia:
#    - Ratio goles/victorias para cada equipo
#    - Efectividad defensiva (goles_contra/derrotas)
#    - Índice de consistencia (puntos/(victorias*3 + empates))

# 5. Proyección de rendimiento:
#    - Si el Atlético mantuviera su promedio de goles, ¿cuántos goles en 50 partidos?
#    - ¿Cuántos puntos necesitaría el Atlético para igualar al líder?
#    - Simular cómo cambiaría la tabla si el Atlético mejorara su defensa en 20%

# 6. Visualización con pandas:
#    - Crear un DataFrame summary con las métricas más importantes
#    - Ordenar equipos por puntos totales
#    - Mostrar el top performer en cada categoría
```

### Criterios de Evaluación
- **Comparación estadística completa** (15 puntos)
- **Cálculos de eficiencia correctos** (5 puntos)
- **Proyecciones realistas** (5 puntos)

---

## Parte 4: Análisis Avanzado de Mercado de Fichajes (25 puntos)

### Objetivo
Combinar múltiples DataFrames para analizar oportunidades en el mercado de fichajes.

### Instrucciones Detalladas

```python
# Base de datos de posibles fichajes
mercado_fichajes = {
    'nombre': ['Erling Haaland', 'Pedri', 'Jude Bellingham', 'Gianluigi Donnarumma', 
               'Rafael Leão', 'Declan Rice', 'Victor Osimhen', 'Bukayo Saka'],
    'equipo_actual': ['Manchester City', 'Barcelona', 'Real Madrid', 'PSG',
                     'AC Milan', 'Arsenal', 'Napoli', 'Arsenal'],
    'posicion': ['Delantero', 'Centrocampista', 'Centrocampista', 'Portero',
                'Extremo', 'Centrocampista', 'Delantero', 'Extremo'],
    'edad': [24, 21, 20, 25, 24, 25, 25, 23],
    'goles_temporada': [36, 4, 14, 0, 14, 7, 31, 14],
    'asistencias_temporada': [13, 6, 13, 0, 6, 4, 5, 11],
    'valor_mercado_millones': [180, 100, 120, 60, 90, 80, 150, 80],
    'salario_anual_millones': [25, 8, 12, 12, 7, 9, 18, 6]
}

# TU CÓDIGO AQUÍ:

# 1. Crear DataFrame de mercado y análisis inicial:
df_mercado = pd.DataFrame(mercado_fichajes)

# 2. Análisis de valor por posición:
#    - Promedio de valor de mercado por posición
#    - Ratio valor/edad para identificar mejores inversiones
#    - Comparar productividad (goles+asistencias) vs valor de mercado

# 3. Compatibilidad con el Atlético:
#    - Filtrar jugadores que mejoren posiciones débiles del Atlético
#    - Calcular el salario total del Atlético si se fichan 2 jugadores
#    - Identificar el mejor fichaje por euro invertido

# 4. Análisis financiero:
#    - Crear columna 'costo_total_5_años' = valor_mercado + (salario_anual * 5)
#    - Ranking de eficiencia: (goles + asistencias) / costo_total_5_años
#    - Presupuesto máximo: 200M euros para fichajes, ¿qué combinación es óptima?

# 5. Merge con datos del Atlético:
#    - Combinar jugadores del mercado con plantilla actual
#    - Crear DataFrame unificado con todos los jugadores disponibles
#    - Análisis de qué posiciones necesitan refuerzo urgente

# 6. Recomendaciones estratégicas:
#    - Top 3 fichajes recomendados para el Atlético
#    - Justificación basada en datos para cada recomendación
#    - Impacto proyectado en el rendimiento del equipo

# 7. Simulación de plantilla mejorada:
#    - Añadir los 2 mejores fichajes al DataFrame del Atlético
#    - Recalcular estadísticas del equipo con los nuevos jugadores
#    - Comparar la nueva plantilla con Real Madrid y Barcelona
```

### Criterios de Evaluación
- **Análisis de mercado comprehensivo** (15 puntos)
- **Merge y manipulación de datos** (5 puntos)
- **Recomendaciones justificadas** (5 puntos)

---

# Criterios de Evaluación Total

## Distribución de Puntos (100 total)

### 1. Correctitud Técnica (40 puntos)
- **Sintaxis pandas/numpy correcta:** Sin errores de ejecución
- **Manipulación de DataFrames:** Operaciones precisas y eficientes  
- **Cálculos estadísticos:** Resultados matemáticamente correctos
- **Uso de funciones apropiadas:** Selección correcta de métodos

### 2. Aplicación Práctica (30 puntos)
- **Análisis deportivo relevante:** Insights útiles para decisiones
- **Comparaciones significativas:** Benchmarking efectivo con rivales
- **Recomendaciones estratégicas:** Propuestas respaldadas por datos
- **Integración de conceptos:** Combinación efectiva de técnicas

### 3. Claridad y Documentación (30 puntos)
- **Código bien comentado:** Explicaciones claras del análisis
- **Variables descriptivas:** Nombres en español y apropiados
- **Presentación profesional:** Outputs formateados y legibles
- **Interpretación correcta:** Análisis acertado de resultados

---

# Instrucciones de Entrega

## Lista de Verificación

Antes de entregar, asegúrate de:

1. **✅ Completar las 4 partes** del análisis con pandas y numpy
2. **✅ Ejecutar todo el código** sin errores
3. **✅ Incluir interpretaciones** de todos los resultados estadísticos
4. **✅ Usar nombres descriptivos** en español para variables
5. **✅ Mostrar DataFrames** claramente formateados

## Formato de Entrega

- **Nombre del archivo:** `[matricula]-ejercicio-semana-4.ipynb`
- **Formato:** Jupyter Notebook ejecutado completamente  
- **Fecha límite:** Final de la Semana 4
- **Método:** Subir a la plataforma del curso

## Recursos de Apoyo

- **Notebook principal:** `bloque-1/semana-4/pandas-numpy-introduccion.ipynb`
- **Documentación Pandas:** [User Guide](https://pandas.pydata.org/docs/user_guide/)
- **Documentación NumPy:** [User Guide](https://numpy.org/doc/stable/user/index.html)
- **Rúbrica detallada:** `evaluaciones/bloque-1/rubrica-unificada-bloque1.md`

---

**¡Domina el análisis de datos deportivos con pandas y numpy como un analista profesional!**
