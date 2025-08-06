# Información General

**Tema:** Visualización Básica con Matplotlib y Seaborn  
**Semana:** 5  
**Bloque:** 1 - Prerrequisitos de Programación  
**Tiempo estimado:** 60 minutos  
**Puntos totales:** 100 puntos  
**Fecha límite:** Final de la Semana 5  
**Archivo entrega:** `[matricula]-ejercicio-semana-5.ipynb`

## Objetivos de Aprendizaje

Al finalizar este ejercicio, el estudiante será capaz de:

1. **Crear gráficos básicos** con matplotlib para análisis deportivo
2. **Personalizar visualizaciones** con seaborn para presentaciones profesionales
3. **Interpretar patrones** visuales en datos de rendimiento deportivo
4. **Generar dashboards** básicos para reportes ejecutivos
5. **Combinar múltiples gráficos** en presentaciones coherentes

## Prerrequisitos

- Ejercicios de las Semanas 1-4 completados exitosamente
- Dominio sólido de pandas y numpy
- Conocimiento de DataFrames y manipulación de datos
- Instalación de matplotlib y seaborn

## Contexto del Ejercicio

Eres el **responsable de visualización de datos** del Valencia CF. La junta directiva necesita presentaciones visuales para:

- Evaluar el rendimiento de la temporada actual
- Comparar con temporadas anteriores
- Identificar áreas de mejora visualmente
- Preparar informes para sponsors y medios de comunicación

---

# Ejercicio Integrador: Dashboard Visual Valencia CF

## Parte 1: Gráficos de Rendimiento Individual (25 puntos)

### Objetivo
Crear visualizaciones que muestren el rendimiento individual de los jugadores estrella del Valencia.

### Instrucciones Detalladas

```python
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Configuración visual estándar
sns.set_theme(style="whitegrid", palette="viridis")
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 11

# Datos de los jugadores estrella del Valencia CF
datos_valencia = {
    'jugador': ['Carlos Soler', 'Gonçalo Guedes', 'Rodrigo Moreno', 'Daniel Wass', 
                'José Gayà', 'Maxi Gómez', 'Lee Kang-in', 'Manu Vallejo'],
    'posicion': ['Centrocampista', 'Extremo', 'Delantero', 'Lateral', 
                'Lateral', 'Delantero', 'Centrocampista', 'Delantero'],
    'goles': [13, 11, 16, 2, 1, 9, 4, 3],
    'asistencias': [6, 7, 4, 5, 8, 2, 3, 1],
    'minutos_jugados': [2850, 2640, 2720, 2480, 2950, 1980, 1650, 1200],
    'tarjetas_amarillas': [7, 4, 3, 8, 6, 5, 2, 3],
    'edad': [25, 24, 30, 32, 27, 25, 21, 24],
    'valor_mercado': [35, 30, 25, 8, 15, 20, 18, 5]  # en millones
}

df_valencia = pd.DataFrame(datos_valencia)

# TU CÓDIGO AQUÍ:

# 1. GRÁFICO DE BARRAS - Goles por jugador
#    - Crear gráfico de barras horizontal
#    - Personalizar colores según posición
#    - Añadir título: "Goleadores Valencia CF 2023-24"
#    - Incluir valores sobre las barras
#    - Configurar etiquetas en español

# 2. GRÁFICO DE DISPERSIÓN - Goles vs Asistencias  
#    - Usar scatter plot con seaborn
#    - Colorear puntos según posición
#    - Añadir línea de tendencia
#    - Título: "Relación Goles-Asistencias Valencia CF"
#    - Incluir leyenda clara

# 3. GRÁFICO CIRCULAR - Distribución por posición
#    - Mostrar porcentaje de jugadores por posición
#    - Usar colores distintivos
#    - Incluir etiquetas con porcentajes
#    - Título: "Distribución de Jugadores por Posición"

# 4. BOXPLOT - Análisis de edad por posición
#    - Crear boxplot con seaborn
#    - Mostrar distribución de edades
#    - Personalizar con palette="Set2"
#    - Título: "Distribución de Edades por Posición"

# 5. HEATMAP - Correlación de estadísticas
#    - Matriz de correlación entre variables numéricas
#    - Usar seaborn heatmap con anotaciones
#    - Colormap='coolwarm'
#    - Título: "Correlaciones Estadísticas Valencia CF"
```

### Criterios de Evaluación
- **5 gráficos implementados correctamente** (15 puntos)
- **Personalización visual profesional** (5 puntos)
- **Títulos y etiquetas en español** (5 puntos)

---

## Parte 2: Análisis Temporal de Rendimiento (25 puntos)

### Objetivo
Crear visualizaciones que muestren la evolución del equipo a lo largo de la temporada.

### Instrucciones Detalladas

```python
# Datos de rendimiento por jornada
jornadas = list(range(1, 21))  # Primeras 20 jornadas
goles_por_jornada = [2, 1, 3, 0, 2, 1, 4, 2, 1, 3, 2, 0, 1, 3, 2, 1, 2, 3, 1, 2]
goles_recibidos = [1, 2, 1, 1, 0, 2, 1, 1, 2, 0, 1, 1, 0, 2, 1, 1, 0, 1, 2, 1]
puntos_acumulados = [3, 3, 6, 6, 9, 10, 13, 16, 16, 19, 22, 22, 25, 28, 31, 34, 37, 40, 40, 43]

# Datos comparativos con rivales
equipos_comparison = ['Valencia', 'Sevilla', 'Real Sociedad', 'Villarreal', 'Athletic']
goles_temporada = [38, 42, 35, 45, 33]
goles_contra_temporada = [28, 25, 30, 22, 31]
puntos_totales = [43, 48, 41, 51, 39]

# TU CÓDIGO AQUÍ:

# 1. GRÁFICO DE LÍNEAS - Evolución de goles por jornada
#    - Línea para goles a favor (verde)
#    - Línea para goles en contra (rojo)
#    - Área sombreada entre las líneas
#    - Título: "Evolución Goleadora Valencia CF - 20 Jornadas"
#    - Leyenda y grid personalizado

# 2. GRÁFICO DE ÁREA - Puntos acumulados
#    - Mostrar crecimiento de puntos a lo largo de jornadas
#    - Añadir línea de objetivo (60 puntos al final de temporada)
#    - Color fill azul con transparencia
#    - Título: "Progresión de Puntos Valencia CF"

# 3. SUBPLOTS - Panel de seguimiento
#    - Crear figura con 2x2 subplots
#    - Subplot 1: Goles por jornada (barras)
#    - Subplot 2: Diferencia de goles acumulada 
#    - Subplot 3: Tendencia de puntos (línea con marcadores)
#    - Subplot 4: Promedio móvil de goles (ventana de 5 partidos)

# 4. GRÁFICO DE BARRAS AGRUPADAS - Comparación con rivales
#    - Goles a favor vs goles en contra por equipo
#    - Barras agrupadas por equipo
#    - Colores diferenciados
#    - Título: "Valencia vs Rivales Directos 2023-24"

# 5. GRÁFICO RADAR - Perfil del equipo
#    - Crear gráfico radar con 6 métricas:
#      (Ataque, Defensa, Disciplina, Experiencia, Valor, Efectividad)
#    - Normalizar valores 0-10
#    - Comparar con promedio de La Liga
```

### Criterios de Evaluación
- **Gráficos temporales correctos** (15 puntos)
- **Subplots bien organizados** (5 puntos)
- **Gráfico radar implementado** (5 puntos)

---

## Parte 3: Dashboard Interactivo y Comparativo (25 puntos)

### Objetivo
Crear un dashboard completo que combine múltiples visualizaciones para análisis integral.

### Instrucciones Detalladas

```python
# Datos ampliados para dashboard
datos_completos = {
    'temporada': ['2020-21', '2021-22', '2022-23', '2023-24'],
    'posicion_liga': [13, 9, 12, 10],
    'goles_favor': [47, 48, 38, 43],
    'goles_contra': [53, 53, 48, 35],
    'puntos': [45, 48, 41, 49],
    'valor_plantilla': [180, 220, 185, 210],  # millones
    'presupuesto': [75, 85, 80, 90]  # millones
}

df_historico = pd.DataFrame(datos_completos)

# TU CÓDIGO AQUÍ:

# 1. DASHBOARD PRINCIPAL - Figura con múltiples subplots
#    Crear figura de 3x3 con 9 gráficos diferentes:

# Fila 1:
#    - Subplot (0,0): Evolución histórica posición en liga
#    - Subplot (0,1): Goles favor vs contra por temporada  
#    - Subplot (0,2): Eficiencia goleadora (goles/partido)

# Fila 2:
#    - Subplot (1,0): Relación valor plantilla vs posición
#    - Subplot (1,1): Distribución de goles temporada actual (histograma)
#    - Subplot (1,2): Comparación presupuesto vs rendimiento

# Fila 3:
#    - Subplot (2,0): Top goleadores individuales (barras)
#    - Subplot (2,1): Análisis disciplinario (tarjetas)
#    - Subplot (2,2): Proyección resto de temporada

# 2. CONFIGURACIÓN AVANZADA:
#    - Título general del dashboard
#    - Espaciado apropiado entre subplots
#    - Colores consistentes en todo el dashboard
#    - Tamaño de figura: (20, 15)

# 3. GRÁFICOS ESPECIALIZADOS:

# A) Gráfico de Violin - Distribución de minutos por posición
#    - Mostrar densidad de distribución
#    - Comparar con otras posiciones
#    - Identificar outliers

# B) Heatmap de rendimiento por mes
#    - Crear matriz mes vs métrica
#    - Mostrar patrones estacionales
#    - Usar diverging colormap

# C) Gráfico de Gantt - Calendario de partidos importantes
#    - Visualizar fixture congestionado
#    - Destacar partidos contra equipos top
#    - Mostrar períodos de descanso

# 4. ANÁLISIS PREDICTIVO VISUAL:
#    - Tendencia polinomial de puntos
#    - Proyección final de liga
#    - Zona de confianza estadística
```

### Criterios de Evaluación
- **Dashboard completo con 9 subplots** (15 puntos)
- **Gráficos especializados** (5 puntos)  
- **Análisis predictivo visual** (5 puntos)

---

## Parte 4: Presentación Profesional para Directiva (25 puntos)

### Objetivo
Crear una presentación visual ejecutiva que resuma los hallazgos clave para la directiva.

### Instrucciones Detalladas

```python
# TU CÓDIGO AQUÍ:

# 1. SLIDE 1 - Resumen Ejecutivo (1 figura, 4 subplots)
#    - KPI principal: Posición actual vs objetivo
#    - Progreso de puntos vs temporada pasada
#    - Diferencial goleador mensual
#    - Comparación con presupuesto

# 2. SLIDE 2 - Análisis de Jugadores Clave (1 figura grande)
#    - Bubble chart: Goles vs Asistencias vs Valor de Mercado
#    - Tamaño de burbuja = Minutos jugados
#    - Color = Posición
#    - Añadir anotaciones para jugadores estrella

# 3. SLIDE 3 - Benchmarking Competitivo (2 subplots)
#    - Subplot izquierdo: Ranking en métricas clave vs 5 rivales
#    - Subplot derecho: Radar chart comparativo
#    - Destacar fortalezas y debilidades

# 4. SLIDE 4 - Proyecciones y Recomendaciones (3 subplots)
#    - Proyección de puntos finales (con intervalo confianza)
#    - ROI de inversiones en fichajes
#    - Roadmap visual de objetivos restantes

# 5. CONFIGURACIÓN PROFESIONAL:
#    - Usar colores corporativos del Valencia (naranja/negro/blanco)
#    - Títulos ejecutivos claros y concisos
#    - Incluir logos/branding simulado
#    - Texto explicativo en cada gráfico

# 6. INSIGHTS CLAVE DESTACADOS:
#    - Cajas de texto con hallazgos principales
#    - Métricas en formato de tarjetas
#    - Call-to-action para decisiones estratégicas

# 7. EXPORTACIÓN:
#    - Guardar cada slide como PNG de alta resolución
#    - Crear versión PDF del reporte completo
#    - Optimizar para presentación en pantalla

# 8. INTERACTIVIDAD SIMULADA:
#    - Crear función que actualice gráficos con nuevos datos
#    - Demostrar cómo cambiarían las visualizaciones
#    - Preparar versiones alternativas de escenarios
```

### Criterios de Evaluación
- **4 slides profesionales completos** (15 puntos)
- **Branding y diseño corporativo** (5 puntos)
- **Insights ejecutivos claros** (5 puntos)

---

# Criterios de Evaluación Total

## Distribución de Puntos (100 total)

### 1. Correctitud Técnica (40 puntos)
- **Sintaxis matplotlib/seaborn correcta:** Sin errores de ejecución
- **Tipos de gráficos apropiados:** Selección correcta para cada análisis
- **Configuración visual:** Parámetros y personalización correctos
- **Exportación y formato:** Calidad profesional de outputs

### 2. Aplicación Práctica (30 puntos)
- **Análisis visual relevante:** Gráficos útiles para decisiones deportivas
- **Interpretación correcta:** Insights válidos de las visualizaciones
- **Comparaciones efectivas:** Benchmarking visual significativo
- **Dashboard integrado:** Presentación cohesiva de múltiples métricas

### 3. Claridad y Documentación (30 puntos)
- **Títulos y etiquetas claros:** Información completa en español
- **Leyendas apropiadas:** Explicación clara de todos los elementos
- **Colores y diseño:** Paleta coherente y profesional
- **Narrativa visual:** Historia clara contada a través de gráficos

---

# Instrucciones de Entrega

## Lista de Verificación

Antes de entregar, asegúrate de:

1. ** Completar las 4 partes** del ejercicio de visualización
2. ** Ejecutar todos los gráficos** sin errores
3. ** Usar configuración estándar** con sns.set_theme()
4. ** Incluir títulos y etiquetas** en español
5. ** Mostrar interpretaciones** de cada visualización

## Formato de Entrega

- **Nombre del archivo:** `[matricula]-ejercicio-semana-5.ipynb`
- **Formato:** Jupyter Notebook ejecutado con todas las visualizaciones
- **Fecha límite:** Final de la Semana 5
- **Método:** Subir a la plataforma del curso

## Recursos de Apoyo

- **Notebook principal:** `bloque-1/semana-5/visualizacion-basica.ipynb`
- **Galería Matplotlib:** [Gallery](https://matplotlib.org/stable/gallery/index.html)
- **Tutorial Seaborn:** [User Guide](https://seaborn.pydata.org/tutorial.html)
- **Rúbrica detallada:** `evaluaciones/bloque-1/rubrica-unificada-bloque1.md`

---

**¡Domina la visualización de datos deportivos y comunica insights como un analista profesional!**
