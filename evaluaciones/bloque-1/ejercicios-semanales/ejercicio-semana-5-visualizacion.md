# Ejercicio Semana 5: Visualización Básica con Matplotlib y Seaborn

## Información del Ejercicio

**Bloque:** 1 - Prerrequisitos de Programación  
**Peso:** 12% de la calificación del bloque (60% ÷ 5 ejercicios)  
**Tiempo estimado:** 2-2.5 horas  
**Entrega:** Final de Semana 5

## Objetivos

Al completar este ejercicio, serás capaz de:

- Crear gráficos básicos con matplotlib para datos deportivos
- Utilizar seaborn para visualizaciones estadísticas avanzadas
- Personalizar gráficos con títulos, etiquetas y colores apropiados
- Interpretar y comunicar resultados a través de visualizaciones

## Configuración Inicial

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Configurar tema de seaborn
sns.set_theme(style="whitegrid", palette="viridis")

# Configurar matplotlib
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.size'] = 12

print("¡Herramientas de visualización listas!")
```

## Ejercicio 1: Gráficos Básicos con Matplotlib (20 puntos)

### Parte A: Gráficos de Línea y Barras

```python
# Datos de goles por jornada de dos equipos
jornadas = list(range(1, 21))  # 20 jornadas
goles_barcelona = [2, 3, 1, 4, 0, 2, 1, 3, 2, 1, 4, 2, 0, 3, 1, 2, 3, 1, 2, 4]
goles_real_madrid = [1, 2, 3, 2, 1, 3, 0, 2, 4, 1, 2, 1, 3, 2, 2, 1, 4, 0, 3, 2]

# Tu código aquí:
# 1. Crear gráfico de línea comparando ambos equipos
# 2. Agregar título: "Evolución de Goles por Jornada"
# 3. Etiquetar ejes apropiadamente
# 4. Agregar leyenda
# 5. Personalizar colores (azul para Barcelona, blanco para Real Madrid)
# 6. Crear gráfico de barras agrupadas para las primeras 10 jornadas
# 7. Agregar línea de tendencia simple
```

### Parte B: Histogramas y Gráficos de Dispersión

```python
# Datos de jugadores
np.random.seed(42)
edades = np.random.normal(26, 4, 50)
goles_temporada = np.random.poisson(12, 50) + np.random.normal(0, 2, 50)
valor_mercado = goles_temporada * 3 + np.random.normal(0, 5, 50) + edades * 0.5

# Tu código aquí:
# 1. Crear histograma de distribución de edades
# 2. Crear histograma de goles por temporada
# 3. Crear gráfico de dispersión: edad vs goles
# 4. Crear gráfico de dispersión: goles vs valor de mercado
# 5. Personalizar todos los gráficos con títulos y etiquetas
# 6. Usar subplots para mostrar múltiples gráficos
```

### Respuesta Parte A

*Completa los gráficos de línea y barras con matplotlib.*

### Respuesta Parte B

*Completa los histogramas y gráficos de dispersión.*

## Ejercicio 2: Visualizaciones Avanzadas con Seaborn (20 puntos)

### Parte A: Gráficos Estadísticos

```python
# Crear DataFrame de jugadores
datos_jugadores = {
    'Nombre': [f'Jugador_{i}' for i in range(1, 31)],
    'Posicion': np.random.choice(['Portero', 'Defensa', 'Centrocampista', 'Delantero'], 30),
    'Liga': np.random.choice(['La Liga', 'Premier League', 'Serie A', 'Bundesliga'], 30),
    'Edad': np.random.randint(18, 35, 30),
    'Goles': np.random.poisson(8, 30),
    'Asistencias': np.random.poisson(5, 30),
    'Partidos': np.random.randint(15, 30, 30),
    'Salario': np.random.normal(2000000, 800000, 30)  # En euros
}

df_jugadores = pd.DataFrame(datos_jugadores)

# Tu código aquí:
# 1. Crear boxplot de goles por posición
# 2. Crear violinplot de salarios por liga
# 3. Crear heatmap de correlación entre variables numéricas
# 4. Crear pairplot para explorar relaciones entre variables
# 5. Personalizar todos los gráficos con títulos en español
```

### Parte B: Gráficos de Distribución y Comparación

```python
# Continuando con el DataFrame anterior

# Tu código aquí:
# 1. Crear countplot de jugadores por liga
# 2. Crear barplot promedio de goles por posición
# 3. Crear stripplot de edad vs goles, coloreado por posición
# 4. Crear FacetGrid para analizar goles por liga y posición
# 5. Crear jointplot de goles vs asistencias
# 6. Personalizar paletas de colores para cada gráfico
```

### Respuesta Parte A

*Completa los gráficos estadísticos con seaborn.*

### Respuesta Parte B

*Completa los gráficos de distribución y comparación.*

## Ejercicio 3: Análisis de Equipos y Rendimiento (20 puntos)

### Tareas de Visualización

```python
# Datos de equipos en múltiples temporadas
equipos_data = {
    'Equipo': ['Barcelona', 'Real Madrid', 'Atletico Madrid', 'Valencia', 'Sevilla'] * 3,
    'Temporada': ['2021-22'] * 5 + ['2022-23'] * 5 + ['2023-24'] * 5,
    'Puntos': [73, 86, 71, 48, 68, 88, 85, 78, 52, 70, 82, 85, 76, 49, 68],
    'Goles_Favor': [68, 80, 65, 48, 53, 70, 75, 70, 45, 58, 75, 85, 72, 40, 56],
    'Goles_Contra': [38, 31, 43, 53, 30, 26, 28, 33, 48, 32, 35, 36, 28, 55, 38],
    'Presupuesto': [800, 750, 400, 200, 180, 850, 800, 450, 180, 200, 900, 850, 500, 150, 220]
}

df_equipos = pd.DataFrame(equipos_data)

# Tu código aquí:
# 1. Crear gráfico de barras: evolución de puntos por equipo y temporada
# 2. Crear lineplot: evolución de puntos a lo largo de las temporadas
# 3. Crear scatterplot: presupuesto vs puntos, con tamaño por goles a favor
# 4. Crear heatmap: equipos vs temporadas mostrando diferencia de goles
# 5. Crear boxplot: distribución de puntos por temporada
# 6. Crear gráfico de barras horizontales: promedio de goles por equipo
# 7. Personalizar todos con colores representativos de cada equipo
```

### Respuesta

*Completa el análisis visual completo de equipos.*

## Ejercicio 4: Dashboard Básico de Estadísticas (20 puntos)

### Creación de Dashboard

```python
# Crear un dashboard con múltiples gráficos en una sola figura

# Datos simulados de una liga completa
np.random.seed(123)
equipos = ['Equipo_' + str(i) for i in range(1, 21)]
datos_liga = {
    'Equipo': equipos,
    'Puntos': np.random.randint(25, 85, 20),
    'Goles_Favor': np.random.randint(30, 90, 20),
    'Goles_Contra': np.random.randint(25, 70, 20),
    'Partidos_Casa': np.random.randint(8, 15, 20),
    'Partidos_Visitante': np.random.randint(8, 15, 20)
}

for equipo in equipos:
    datos_liga[equipo + '_Victorias'] = np.random.randint(5, 25, 1)[0]

df_liga = pd.DataFrame(datos_liga)

# Tu código aquí:
# Crear figura con subplots (2x3 = 6 gráficos):
# 1. Top 10 equipos por puntos (barplot)
# 2. Distribución de goles a favor (histogram)
# 3. Relación goles favor vs contra (scatterplot)
# 4. Promedio de puntos por rango de goles favor (barplot)
# 5. Boxplot de distribución de puntos
# 6. Pie chart de equipos por rango de puntos (alto, medio, bajo)

# Requisitos:
# - Usar plt.subplots() con figsize=(15, 10)
# - Títulos descriptivos en español para cada gráfico
# - Colores consistentes y atractivos
# - Leyendas donde sea apropiado
# - Título general del dashboard
```

### Respuesta

*Completa el dashboard con 6 visualizaciones integradas.*

## Ejercicio 5: Análisis Temporal y Tendencias (20 puntos)

### Visualización de Series Temporales

```python
# Datos de rendimiento temporal de un equipo
fechas = pd.date_range('2024-01-01', '2024-12-31', freq='W')
rendimiento_semanal = {
    'Fecha': fechas,
    'Goles_Favor': np.random.poisson(2, len(fechas)) + np.sin(np.arange(len(fechas)) * 2 * np.pi / 52) + 2,
    'Goles_Contra': np.random.poisson(1, len(fechas)) + np.cos(np.arange(len(fechas)) * 2 * np.pi / 52) + 1,
    'Puntos_Acumulados': np.cumsum(np.random.choice([0, 1, 3], len(fechas), p=[0.2, 0.3, 0.5])),
    'Asistencia_Promedio': np.random.normal(45000, 10000, len(fechas))
}

df_temporal = pd.DataFrame(rendimiento_semanal)

# Tu código aquí:
# 1. Crear gráfico de línea doble: goles favor vs contra a lo largo del año
# 2. Crear gráfico de área: puntos acumulados durante la temporada
# 3. Crear gráfico de barras mensuales: promedio de asistencia por mes
# 4. Crear heatmap calendario: goles favor por semana del año
# 5. Crear gráfico de tendencia con línea de regresión
# 6. Crear análisis de estacionalidad (trimestres)
# 7. Personalizar con anotaciones en fechas importantes
```

### Respuesta

*Completa el análisis temporal completo.*

## Ejercicio Bonus: Visualización Interactiva Básica (10 puntos extra)

### Gráficos Avanzados

**Ejercicio opcional para puntos adicionales:**

```python
# Crear visualizaciones más sofisticadas

# Tu código aquí:
# 1. Crear gráfico de radar para comparar jugadores
# 2. Crear mapa de calor animado (simular con múltiples frames)
# 3. Crear gráfico de cascada para análisis de puntos
# 4. Crear gráfico de Sankey para transferencias (simulado)
# 5. Personalizar con estilos avanzados y anotaciones

# Usar técnicas como:
# - plt.annotate() para anotaciones
# - matplotlib.patches para formas personalizadas
# - Colormaps personalizados
# - Múltiples ejes Y
# - Gráficos polares
```

### Respuesta Bonus

*Ejercicio opcional: Crea visualizaciones avanzadas y creativas.*

## Criterios de Evaluación

### Técnica de Visualización (40%)

- [ ] Uso correcto de matplotlib y seaborn (20%)
- [ ] Personalización apropiada de gráficos (20%)

### Comunicación Visual (35%)

- [ ] Títulos y etiquetas claros en español (15%)
- [ ] Elección apropiada de tipo de gráfico (10%)
- [ ] Paletas de colores efectivas (10%)

### Análisis e Interpretación (25%)

- [ ] Interpretación correcta de los gráficos (15%)
- [ ] Insights relevantes del análisis visual (10%)

## Instrucciones de Entrega

1. **Completa todos los ejercicios** en este notebook
2. **Ejecuta todas las celdas** de visualización
3. **Incluye interpretaciones** de cada gráfico creado
4. **Guarda como:** `ejercicio-semana-5-[tu-apellido].ipynb`
5. **Entrega antes del final de Semana 5**

## Recursos de Apoyo

- Notebook de la Semana 5: `visualizacion-basica.ipynb`
- Documentación Matplotlib: <https://matplotlib.org/>
- Documentación Seaborn: <https://seaborn.pydata.org/>
- Galería de gráficos: <https://python-graph-gallery.com/>

---

**¡Transforma datos en historias visuales que comuniquen insights deportivos!** ⚽📈
