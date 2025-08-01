# Ejercicio Semana 7: Tipos de Datos en Análisis Deportivo

## Información General

**Bloque:** 2 - Fundamentos de Data Science  
**Semana:** 7  
**Tiempo estimado:** 60 minutos  
**Puntos totales:** 100 puntos  
**Fecha límite:** Final de la Semana 7  
**Archivo entrega:** `[matricula]-ejercicio-semana-7.ipynb`

## Objetivos de Aprendizaje

Al completar este ejercicio, el estudiante será capaz de:
- Identificar y manejar diferentes tipos de datos en análisis futbolístico
- Convertir tipos de datos apropiadamente usando pandas
- Trabajar eficientemente con datos categóricos, numéricos y temporales
- Optimizar el uso de memoria mediante tipos de datos correctos
- Crear categorías significativas para análisis deportivo avanzado

## Prerrequisitos

- Ejercicio de la Semana 6 completado exitosamente
- Conocimiento básico de pandas y exploratory data analysis
- Comprensión de tipos de datos básicos en Python
- Familiaridad con operaciones de DataFrame

## Contexto del Ejercicio

Eres el **analista de datos principal** del Manchester United. El departamento de analytics necesita un sistema robusto para:

- Optimizar la gestión de datos de jugadores y partidos
- Asegurar la calidad y consistencia de tipos de datos
- Crear categorías útiles para análisis de rendimiento
- Preparar datos para modelos predictivos avanzados

---

# Ejercicio Integrador: Sistema de Calidad de Datos Manchester United

## Parte 1: Identificación y Conversión de Tipos (25 puntos)

### Objetivo
Analizar y corregir tipos de datos en el sistema de información deportiva del Manchester United.

### Instrucciones Detalladas

**Paso 1:** Configura el entorno y carga datos problemáticos:

```python
# Configuración del sistema de análisis Manchester United
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta

# Configuración visual estándar
sns.set_theme(style="whitegrid", palette="viridis")
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.size'] = 11

print("=== SISTEMA DE CALIDAD DE DATOS MAN UNITED ===")
print("Módulo de optimización de tipos de datos iniciado")
print("¡Herramientas de análisis listas!")
```

**Paso 2:** Analiza y corrige tipos de datos problemáticos:

```python
# Dataset con tipos incorrectos (simula datos reales mal formateados)
datos_partidos_mufc = {
    'Fecha': ['2024-01-15', '2024-01-22', '2024-01-29', '2024-02-05', '2024-02-12'],
    'Jornada': ['1', '2', '3', '4', '5'],  # String pero debe ser int
    'Rival': ['Liverpool', 'Arsenal', 'Chelsea', 'Man City', 'Tottenham'],
    'Ubicacion': ['Old Trafford', 'Emirates', 'Old Trafford', 'Etihad', 'Old Trafford'],
    'Goles_MUFC': ['2', '1', '3', '0', '2'],  # String pero debe ser int
    'Goles_Rival': [1, 2, 1, 1, 0],  # Ya int correcto
    'Temperatura': ['15.5', '18.2', '12.8', '20.1', '16.7'],  # String pero debe ser float
    'Asistencia': [74310, 60260, 74310, 55017, 74310],  # Ya int correcto
    'Arbitro': ['Oliver', 'Taylor', 'Atkinson', 'Dean', 'Friend'],
    'Competicion': ['Premier', 'Premier', 'Premier', 'Premier', 'Premier']
}

df_mufc = pd.DataFrame(datos_partidos_mufc)

# TU CÓDIGO AQUÍ:
# 1. Mostrar tipos de datos actuales con .dtypes
# 2. Mostrar uso de memoria inicial con .memory_usage(deep=True)
# 3. Identificar columnas con tipos incorrectos
# 4. Convertir 'Fecha' a datetime usando pd.to_datetime()
# 5. Convertir 'Jornada' y 'Goles_MUFC' a enteros
# 6. Convertir 'Temperatura' a float
# 7. Convertir columnas de texto a 'category' para optimizar memoria
# 8. Verificar los tipos después de conversión
# 9. Comparar uso de memoria antes y después

print("=== ANÁLISIS DE TIPOS DE DATOS MUFC ===")
print("Estado inicial del dataset:")
# Mostrar análisis aquí
```

### Criterios de Evaluación
- **Identificación correcta de tipos problemáticos** (10 puntos)
- **Conversiones exitosas y verificadas** (15 puntos)

---

## Parte 2: Gestión de Datos Categóricos (25 puntos)

### Objetivo
Crear y gestionar categorías eficientes para análisis de rendimiento de jugadores.

### Instrucciones Detalladas

**Paso 3:** Crea dataset de jugadores con categorías:

```python
# Información de jugadores del Manchester United
jugadores_mufc = {
    'Nombre': ['Rashford', 'Fernandes', 'Casemiro', 'Varane', 'Shaw', 'Garnacho', 'Eriksen', 'Maguire'],
    'Edad': [26, 29, 31, 30, 28, 19, 31, 30],
    'Altura_cm': [180, 179, 185, 191, 185, 180, 182, 194],
    'Peso_kg': [70, 69, 84, 81, 85, 73, 76, 100],
    'Posicion': ['Delantero', 'Centrocampista', 'Centrocampista', 'Defensa', 'Defensa', 'Extremo', 'Centrocampista', 'Defensa'],
    'Pie_Habil': ['Derecho', 'Derecho', 'Derecho', 'Derecho', 'Izquierdo', 'Derecho', 'Derecho', 'Derecho'],
    'Partidos_Jugados': [45, 48, 38, 29, 35, 42, 40, 25],
    'Goles_Temporada': [17, 8, 1, 2, 1, 9, 3, 1],
    'Salario_Semanal': [300000, 240000, 350000, 340000, 150000, 50000, 150000, 190000],
    'Estado_Contrato': ['Renovado', 'Vigente', 'Vigente', 'Vigente', 'Renovado', 'Joven', 'Vigente', 'Vigente']
}

df_jugadores_mufc = pd.DataFrame(jugadores_mufc)

# TU CÓDIGO AQUÍ:
# 1. Convertir 'Posicion' y 'Pie_Habil' a tipo category
# 2. Crear categoría 'Grupo_Edad': 'Joven' (<23), 'Medio' (23-29), 'Veterano' (30+)
# 3. Crear categoría 'Nivel_Salario': 'Bajo' (<100k), 'Medio' (100k-250k), 'Alto' (250k+)
# 4. Crear categoría 'Efectividad_Gol': Basada en goles/partidos
# 5. Crear categoría 'Tipo_Fisico': Basada en altura y peso
# 6. Verificar todas las categorías creadas
# 7. Mostrar distribución de jugadores por cada categoría

print("=== CATEGORIZACIÓN DE JUGADORES MUFC ===")
```

**Paso 4:** Analiza las categorías creadas:

```python
# Análisis de distribuciones categóricas

# TU CÓDIGO AQUÍ:
# 1. Mostrar conteo de jugadores por posición
# 2. Calcular estadísticas por grupo de edad
# 3. Analizar rendimiento por nivel de salario
# 4. Crear tabla cruzada posición vs grupo de edad
# 5. Identificar patrones en las categorías
# 6. Calcular correlaciones entre categorías numéricas

print("=== ANÁLISIS CATEGÓRICO DETALLADO ===")
```

### Criterios de Evaluación
- **Creación correcta de categorías** (15 puntos)
- **Análisis categórico completo** (10 puntos)

---

## Parte 3: Manipulación de Datos Temporales (25 puntos)

### Objetivo
Gestionar y analizar datos temporales para seguimiento de rendimiento estacional.

### Instrucciones Detalladas

**Paso 5:** Crea y analiza series temporales:

```python
# Crear datos de rendimiento temporal del Manchester United
fechas_temporada = pd.date_range('2023-08-01', '2024-05-30', freq='W')
np.random.seed(42)  # Para reproducibilidad

datos_temporales = {
    'Fecha': fechas_temporada[:20],  # 20 partidos de muestra
    'Puntos_Obtenidos': np.random.choice([0, 1, 3], 20, p=[0.15, 0.25, 0.60]),
    'Goles_Favor': np.random.poisson(1.8, 20),
    'Goles_Contra': np.random.poisson(1.2, 20),
    'Posesion_Promedio': np.random.normal(58, 8, 20),
    'Pases_Completados': np.random.normal(520, 80, 20)
}

df_temporal_mufc = pd.DataFrame(datos_temporales)

# TU CÓDIGO AQUÍ:
# 1. Verificar que 'Fecha' es tipo datetime
# 2. Extraer componentes temporales: mes, día de la semana, quarter
# 3. Crear columnas: 'Mes', 'Dia_Semana', 'Trimestre'
# 4. Calcular estadísticas por mes y trimestre
# 5. Identificar tendencias temporales en el rendimiento
# 6. Crear categoría 'Epoca_Temporada': 'Inicio', 'Medio', 'Final'
# 7. Analizar diferencias de rendimiento por época de temporada

print("=== ANÁLISIS TEMPORAL RENDIMIENTO MUFC ===")
```

**Paso 6:** Visualiza patrones temporales:

```python
# Crear visualizaciones de tendencias temporales

# TU CÓDIGO AQUÍ:
# 1. Gráfico de línea: Puntos acumulados a lo largo de la temporada
# 2. Gráfico de barras: Rendimiento promedio por mes
# 3. Boxplot: Distribución de goles por trimestre
# 4. Heatmap: Rendimiento por día de la semana y mes
# 5. Identificar patrones estacionales
# 6. Detectar mejores y peores períodos de rendimiento

plt.figure(figsize=(12, 8))
# Implementar visualizaciones

print("=== VISUALIZACIÓN DE PATRONES TEMPORALES ===")
```

### Criterios de Evaluación
- **Manipulación temporal correcta** (15 puntos)
- **Análisis de patrones temporales** (10 puntos)

---

## Parte 4: Optimización y Validación Final (25 puntos)

### Objetivo
Crear un sistema integral de validación y optimización de tipos de datos.

### Instrucciones Detalladas

**Paso 7:** Desarrolla sistema de validación:

```python
# Sistema de validación automática de tipos de datos

# TU CÓDIGO AQUÍ:
# 1. Crear función que valide tipos esperados para cada columna
# 2. Función que detecte valores atípicos por tipo de dato
# 3. Función que optimice uso de memoria automáticamente
# 4. Sistema de alertas para tipos incorrectos
# 5. Reporte de calidad de datos con recomendaciones
# 6. Función que documente cambios realizados

def validar_tipos_mufc(dataframe, tipos_esperados):
    """
    Valida tipos de datos en DataFrames del Manchester United
    
    Parámetros:
    dataframe: DataFrame a validar
    tipos_esperados: Dict con tipos esperados por columna
    
    Retorna:
    Dict con resultado de validación y recomendaciones
    """
    # Tu implementación aquí
    pass

def optimizar_memoria_mufc(dataframe):
    """
    Optimiza uso de memoria del DataFrame
    """
    # Tu implementación aquí
    pass

# Probar funciones con datasets creados
print("=== SISTEMA DE VALIDACIÓN MUFC ===")
```

**Paso 8:** Genera reporte final de optimización:

```python
# Reporte ejecutivo de optimización de datos

# TU CÓDIGO AQUÍ:
# 1. Comparar uso de memoria antes y después de optimizaciones
# 2. Calcular porcentaje de mejora en eficiencia
# 3. Documentar todos los cambios realizados
# 4. Crear dashboard de calidad de datos
# 5. Proponer mejoras adicionales
# 6. Generar recomendaciones para futuros datasets

print("=== REPORTE FINAL DE OPTIMIZACIÓN MUFC ===")
print("\n1. MEJORAS EN USO DE MEMORIA:")
# Tu análisis aquí

print("\n2. CALIDAD DE DATOS ALCANZADA:")
# Tu análisis aquí

print("\n3. CATEGORÍAS ÚTILES CREADAS:")
# Tu análisis aquí

print("\n4. RECOMENDACIONES FUTURAS:")
# Tu análisis aquí

# Crear visualización final de eficiencia
plt.figure(figsize=(10, 6))
# Gráfico comparativo de optimización

plt.title("Optimización de Datos: Antes vs Después", fontsize=14, fontweight='bold')
plt.show()
```

### Criterios de Evaluación
- **Sistema de validación funcional** (15 puntos)
- **Reporte ejecutivo completo** (10 puntos)

## Criterios de Evaluación General

### Correctitud Técnica (40 puntos)
- Conversiones de tipos correctas y verificadas
- Uso apropiado de métodos de pandas
- Funciones de validación implementadas correctamente
- Cálculos de optimización precisos

### Aplicación Práctica (30 puntos)
- Categorías relevantes para análisis deportivo
- Análisis temporal útil para toma de decisiones
- Sistema de validación aplicable al contexto real
- Optimizaciones que impacten el rendimiento

### Claridad y Documentación (30 puntos)
- Código bien documentado en español
- Explicaciones claras de optimizaciones realizadas
- Presentación profesional de resultados
- Variables con nombres descriptivos del contexto MUFC

## Instrucciones de Entrega

1. **Completa todas las partes** siguiendo la secuencia lógica
2. **Incluye explicaciones** para cada optimización realizada
3. **Verifica funcionamiento** de todas las funciones creadas
4. **Guarda como:** `[matricula]-ejercicio-semana-7.ipynb`
5. **Entrega antes del final de Semana 7**

## Recursos de Apoyo

- Notebook de la Semana 7: `tipos-datos-futbol.ipynb`
- Documentación pandas: Métodos `.astype()`, `.category()`, `pd.to_datetime()`
- Guía de optimización de memoria en pandas

---

**¡Optimiza los datos del Manchester United y lleva el análisis deportivo al siguiente nivel!** ⚽🔧
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
