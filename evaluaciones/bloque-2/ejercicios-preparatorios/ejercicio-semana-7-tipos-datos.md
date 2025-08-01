# Ejercicio Semana 7: Dominando Tipos de Datos en Análisis Futbolístico

## Información del Ejercicio

**Bloque:** 2 - Fundamentos de Data Science  
**Peso:** 12% de la calificación del bloque (60% ÷ 5 ejercicios)  
**Tiempo estimado:** 2-2.5 horas  
**Entrega:** Final de Semana 7

## Objetivos

Al completar este ejercicio, serás capaz de:

- Identificar y trabajar con diferentes tipos de datos en contexto futbolístico
- Convertir y manipular tipos de datos apropiadamente
- Aplicar operaciones específicas para datos categóricos, numéricos y temporales
- Optimizar el uso de memoria y rendimiento con tipos correctos
- Crear variables categóricas significativas para análisis deportivo

## Configuración Inicial

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta

# Configurar estilo
sns.set_theme(style="whitegrid", palette="viridis")
plt.rcParams['figure.figsize'] = (10, 6)

print("¡Herramientas para análisis de tipos de datos listas!")
```

## Ejercicio 1: Identificación y Conversión de Tipos (20 puntos)

### Parte A: Análisis de Tipos Actuales

```python
# Crear dataset con tipos mixtos (simular datos reales mal formateados)
datos_partidos = {
    'Fecha': ['2024-01-15', '2024-01-22', '2024-01-29', '2024-02-05', '2024-02-12'],
    'Jornada': ['1', '2', '3', '4', '5'],  # String pero debería ser int
    'Equipo_Local': ['Barcelona', 'Real Madrid', 'Atletico', 'Valencia', 'Sevilla'],
    'Equipo_Visitante': ['Valencia', 'Barcelona', 'Sevilla', 'Real Madrid', 'Atletico'],
    'Goles_Local': ['2', '1', '3', '0', '2'],  # String pero debería ser int
    'Goles_Visitante': [1, 2, 1, 1, 0],  # Ya int
    'Temperatura': ['15.5', '18.2', '12.8', '20.1', '16.7'],  # String pero debería ser float
    'Asistencia': [85000, 88000, 75000, 65000, 42000],  # Ya int
    'Arbitro': ['García', 'López', 'Martínez', 'Rodríguez', 'Fernández'],
    'Liga': ['La Liga', 'La Liga', 'La Liga', 'La Liga', 'La Liga']
}

df_partidos = pd.DataFrame(datos_partidos)

# Tu código aquí:
# 1. Mostrar tipos de datos actuales con .dtypes
# 2. Identificar qué columnas tienen tipos incorrectos
# 3. Convertir 'Fecha' a datetime
# 4. Convertir 'Jornada' y 'Goles_Local' a int
# 5. Convertir 'Temperatura' a float
# 6. Convertir columnas de texto a category cuando sea apropiado
# 7. Verificar los nuevos tipos de datos
# 8. Mostrar el uso de memoria antes y después de conversiones
```

### Parte B: Validación de Conversiones

```python
# Continuando con el dataset anterior

# Tu código aquí:
# 1. Verificar que todas las conversiones fueron exitosas
# 2. Crear función para validar tipos de un DataFrame
# 3. Mostrar estadísticas descriptivas para cada tipo de dato
# 4. Identificar posibles errores en los datos convertidos
# 5. Crear alertas para valores fuera de rango esperado
# 6. Documentar el proceso de conversión
```

### Respuesta Parte A

*Completa la identificación y conversión de tipos de datos.*

### Respuesta Parte B

*Completa la validación del proceso de conversión.*

## Ejercicio 2: Trabajando con Datos Categóricos (20 puntos)

### Creación de Categorías Futbolísticas

```python
# Crear dataset de jugadores con información categórica
jugadores_data = {
    'Nombre': ['Messi', 'Ronaldo', 'Mbappé', 'Haaland', 'Neymar', 'Salah', 'Benzema', 'Lewandowski'],
    'Edad': [36, 39, 25, 23, 32, 31, 36, 35],
    'Altura_cm': [170, 187, 178, 194, 175, 175, 185, 184],
    'Peso_kg': [72, 84, 73, 88, 68, 71, 81, 80],
    'Posicion': ['Delantero', 'Delantero', 'Delantero', 'Delantero', 'Delantero', 'Delantero', 'Delantero', 'Delantero'],
    'Pie_Dominante': ['Izquierdo', 'Derecho', 'Derecho', 'Izquierdo', 'Derecho', 'Izquierdo', 'Derecho', 'Derecho'],
    'Goles_Temporada': [12, 15, 18, 22, 8, 16, 12, 19],
    'Liga': ['MLS', 'Saudi Pro', 'La Liga', 'Premier League', 'Saudi Pro', 'Premier League', 'La Liga', 'La Liga']
}

df_jugadores = pd.DataFrame(jugadores_data)

# Tu código aquí:
# 1. Convertir variables apropiadas a tipo category
# 2. Crear categoría 'Rango_Edad': Joven (<25), Adulto (25-32), Veterano (>32)
# 3. Crear categoría 'Complexion': Bajo (<175cm), Medio (175-185cm), Alto (>185cm)
# 4. Crear categoría 'Rendimiento_Goles': Bajo (<10), Medio (10-15), Alto (>15)
# 5. Ordenar categorías de manera lógica (usar ordered=True)
# 6. Mostrar frecuencias de cada categoría
# 7. Crear tabulación cruzada entre diferentes categorías
```

### Análisis Categórico Avanzado

```python
# Continuando con el dataset de jugadores

# Tu código aquí:
# 1. Calcular estadísticas por categoría de edad
# 2. Analizar relación entre pie dominante y rendimiento
# 3. Comparar distribución de complexión por liga
# 4. Crear heatmap de relaciones entre variables categóricas
# 5. Identificar combinaciones de categorías más exitosas
# 6. Usar .value_counts() para analizar distribuciones
# 7. Aplicar .groupby() con múltiples variables categóricas
```

### Respuesta

*Completa el trabajo con datos categóricos y su análisis.*

## Ejercicio 3: Manipulación de Datos Temporales (20 puntos)

### Análisis de Series de Tiempo Futbolísticas

```python
# Crear dataset temporal de rendimiento semanal
fechas_inicio = pd.date_range('2024-01-01', '2024-06-30', freq='W')
np.random.seed(42)

datos_temporales = {
    'Fecha': fechas_inicio,
    'Equipo': np.random.choice(['Barcelona', 'Real Madrid', 'Atletico'], len(fechas_inicio)),
    'Goles_Favor': np.random.poisson(2, len(fechas_inicio)),
    'Goles_Contra': np.random.poisson(1, len(fechas_inicio)),
    'Posesion_Promedio': np.random.normal(55, 10, len(fechas_inicio)),
    'Distancia_Recorrida': np.random.normal(105, 8, len(fechas_inicio))  # km por partido
}

df_temporal = pd.DataFrame(datos_temporales)

# Tu código aquí:
# 1. Asegurar que 'Fecha' sea tipo datetime
# 2. Establecer 'Fecha' como índice del DataFrame
# 3. Extraer componentes temporales: año, mes, semana, día de la semana
# 4. Crear columna 'Trimestre' basada en la fecha
# 5. Calcular diferencia en días entre partidos consecutivos
# 6. Identificar patrones por día de la semana
# 7. Agrupar datos por mes y calcular promedios
# 8. Crear columna 'Temporada' (ej: 2024-H1, 2024-H2)
```

### Análisis de Tendencias Temporales

```python
# Continuando con el dataset temporal

# Tu código aquí:
# 1. Calcular media móvil de 4 semanas para goles
# 2. Identificar mejor y peor mes de cada equipo
# 3. Analizar tendencias estacionales en el rendimiento
# 4. Calcular correlación entre variables a lo largo del tiempo
# 5. Identificar rachas de buen/mal rendimiento
# 6. Comparar rendimiento entre trimestres
# 7. Crear visualización de evolución temporal por equipo
```

### Respuesta

*Completa el análisis completo de datos temporales.*

## Ejercicio 4: Optimización de Tipos y Memoria (20 puntos)

### Análisis de Eficiencia

```python
# Crear dataset grande para analizar optimización
np.random.seed(123)
n_registros = 10000

datos_grandes = {
    'ID_Jugador': range(1, n_registros + 1),
    'Nombre': [f'Jugador_{i}' for i in range(1, n_registros + 1)],
    'Edad': np.random.randint(16, 40, n_registros),
    'Posicion': np.random.choice(['Portero', 'Defensa', 'Centrocampista', 'Delantero'], n_registros),
    'Liga': np.random.choice(['La Liga', 'Premier League', 'Serie A', 'Bundesliga', 'Ligue 1'], n_registros),
    'Goles': np.random.randint(0, 30, n_registros),
    'Valor_Mercado': np.random.uniform(100000, 100000000, n_registros),
    'Activo': np.random.choice([True, False], n_registros),
    'Rating': np.random.uniform(40.0, 99.0, n_registros)
}

df_grande = pd.DataFrame(datos_grandes)

# Tu código aquí:
# 1. Mostrar uso de memoria inicial con .memory_usage()
# 2. Identificar oportunidades de optimización por columna
# 3. Optimizar tipos enteros (usar int8, int16 según rango)
# 4. Convertir strings repetitivos a category
# 5. Usar tipos float más eficientes cuando sea posible
# 6. Comparar uso de memoria antes y después
# 7. Crear función para optimización automática de DataFrame
# 8. Medir tiempo de operaciones antes y después de optimización
```

### Función de Optimización Automática

```python
def optimizar_dataframe(df):
    """
    Optimiza automáticamente los tipos de datos de un DataFrame
    
    Parámetros:
    df (DataFrame): DataFrame a optimizar
    
    Retorna:
    DataFrame: DataFrame optimizado
    dict: Reporte de optimización
    """
    # Tu código aquí:
    # 1. Crear copia del DataFrame original
    # 2. Iterar por cada columna
    # 3. Aplicar optimizaciones según tipo y valores
    # 4. Generar reporte de mejoras
    # 5. Retornar DataFrame optimizado y reporte
    pass

# Probar la función con el dataset grande
# df_optimizado, reporte = optimizar_dataframe(df_grande)
```

### Respuesta

*Completa la optimización de tipos y memoria del DataFrame.*

## Ejercicio 5: Validación y Control de Calidad (20 puntos)

### Sistema de Validación de Datos

```python
# Crear dataset con problemas típicos para validar
datos_problematicos = {
    'Jugador': ['Messi', 'Ronaldo', '', 'Haaland', 'Neymar'],  # Nombre vacío
    'Edad': [36, 39, -5, 23, 150],  # Edad negativa e imposible
    'Posicion': ['Delantero', 'DELANTERO', 'delantero', 'Medio', ''],  # Inconsistencias
    'Goles': [12, 15, 50, 22, -3],  # Goles negativos y excesivos
    'Salario': [35000000, 200000000, 0, 20000000, ''],  # Valor vacío
    'Fecha_Nacimiento': ['1987-06-24', '1985-02-05', '2025-01-01', '2000-07-21', 'invalid']  # Fecha futura e inválida
}

df_problemas = pd.DataFrame(datos_problematicos)

# Tu código aquí:
# 1. Crear función para validar rangos de edad (16-45 años)
# 2. Crear función para estandarizar nombres de posiciones
# 3. Validar que goles esté en rango lógico (0-50)
# 4. Detectar valores faltantes y decidir estrategia
# 5. Validar fechas de nacimiento lógicas
# 6. Crear reporte completo de problemas encontrados
# 7. Implementar correcciones automáticas cuando sea posible
# 8. Generar dataset limpio con log de cambios
```

### Dashboard de Calidad de Datos

```python
def generar_reporte_calidad(df, nombre_dataset="Dataset"):
    """
    Genera reporte completo de calidad de datos
    
    Parámetros:
    df (DataFrame): DataFrame a analizar
    nombre_dataset (str): Nombre del dataset para el reporte
    
    Retorna:
    dict: Reporte completo de calidad
    """
    # Tu código aquí:
    # 1. Contar valores faltantes por columna
    # 2. Identificar duplicados
    # 3. Detectar outliers estadísticos
    # 4. Validar tipos de datos esperados vs actuales
    # 5. Calcular completitud del dataset
    # 6. Generar score de calidad general
    # 7. Crear visualizaciones de problemas
    # 8. Retornar reporte estructurado
    pass

# Aplicar a diferentes datasets y comparar
# reporte_jugadores = generar_reporte_calidad(df_jugadores, "Jugadores")
# reporte_partidos = generar_reporte_calidad(df_partidos, "Partidos")
```

### Respuesta

*Completa el sistema de validación y control de calidad.*

## Ejercicio Bonus: Ingeniería de Características Categóricas (10 puntos extra)

### Creación de Variables Avanzadas

**Ejercicio opcional para puntos adicionales:**

```python
# Crear características avanzadas para análisis

# Tu código aquí:
# 1. Crear variable 'Experiencia' basada en edad y años profesionales
# 2. Generar 'Índice_Físico' combinando altura, peso y posición
# 3. Crear 'Categoría_Valor' basada en percentiles de valor de mercado
# 4. Desarrollar 'Score_Versatilidad' para jugadores multi-posición
# 5. Implementar 'Rating_Liga' basado en competitividad histórica
# 6. Crear variables dummy para análisis estadístico
# 7. Generar interacciones entre variables categóricas
# 8. Validar utilidad de nuevas variables con correlaciones

# Técnicas avanzadas:
# - One-hot encoding inteligente
# - Label encoding ordenado
# - Target encoding básico
# - Binning automático
# - Feature scaling por categorías
```

### Respuesta Bonus

*Ejercicio opcional: Crea sistema avanzado de ingeniería de características.*

## Criterios de Evaluación

### Dominio de Tipos de Datos (40%)

- [ ] Identificación correcta de tipos apropiados (15%)
- [ ] Conversiones exitosas y validadas (15%)
- [ ] Optimización efectiva de memoria (10%)

### Trabajo con Categorías (30%)

- [ ] Creación lógica de variables categóricas (15%)
- [ ] Análisis apropiado de datos categóricos (15%)

### Análisis Temporal y Validación (30%)

- [ ] Manipulación correcta de fechas y tiempo (15%)
- [ ] Sistema efectivo de validación de calidad (15%)

## Instrucciones de Entrega

1. **Completa todos los ejercicios** en este notebook
2. **Documenta tus decisiones** sobre tipos de datos
3. **Incluye validaciones** para cada conversión
4. **Guarda como:** `ejercicio-semana-7-[tu-apellido].ipynb`
5. **Entrega antes del final de Semana 7**

## Recursos de Apoyo

- Notebook de la Semana 7: `tipos-datos-futbol.ipynb`
- Documentación pandas dtypes: <https://pandas.pydata.org/docs/user_guide/basics.html#dtypes>
- Guía de categorías: <https://pandas.pydata.org/docs/user_guide/categorical.html>
- Trabajando con tiempo: <https://pandas.pydata.org/docs/user_guide/timeseries.html>

---

**¡Domina los tipos de datos para análisis más eficientes y precisos!** ⚽📋
