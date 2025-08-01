# Ejercicio Semana 8: Estadística Descriptiva en Análisis Deportivo

## Información del Ejercicio

**Bloque:** 2 - Fundamentos de Data Science  
**Peso:** 12% de la calificación del bloque (60% ÷ 5 ejercicios)  
**Tiempo estimado:** 2.5-3 horas  
**Entrega:** Final de Semana 8

## Objetivos

Al completar este ejercicio, serás capaz de:

- Calcular e interpretar medidas de tendencia central en contexto deportivo
- Aplicar medidas de dispersión para analizar variabilidad en rendimiento
- Identificar y analizar outliers en datos futbolísticos
- Realizar análisis de distribuciones y normalidad
- Comparar rendimientos usando estadística descriptiva
- Crear reportes estadísticos profesionales

## Configuración Inicial

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

# Configurar estilo
sns.set_theme(style="whitegrid", palette="viridis")
plt.rcParams['figure.figsize'] = (12, 8)

# Cargar datos
df_equipos = pd.read_csv('equipos-europa-2023-24.csv')
df_jugadores = pd.read_csv('jugadores-estrellas-2024.csv')

print("¡Herramientas estadísticas listas para el análisis deportivo!")
```

## Ejercicio 1: Medidas de Tendencia Central (20 puntos)

### Análisis de Rendimiento Ofensivo

```python
# Extraer goles por equipo para análisis
goles_equipos = df_equipos['Goles_Favor'].values
puntos_equipos = df_equipos['Puntos'].values

# Tu código aquí:
# 1. Calcular media, mediana y moda de goles por equipo
# 2. Calcular media, mediana y moda de puntos por equipo
# 3. Interpretar qué medida es más representativa para cada variable
# 4. Comparar medias por liga usando groupby
# 5. Calcular media ponderada de goles (por número de partidos)
# 6. Identificar cuándo usar cada medida de tendencia central
# 7. Crear función para calcular todas las medidas automáticamente
```

### Análisis de Jugadores por Posición

```python
# Análisis específico por posición de jugadores
goles_jugadores = df_jugadores['Goles'].values
valores_mercado = df_jugadores['Valor_Mercado'].values

# Tu código aquí:
# 1. Calcular estadísticas centrales de goles por posición
# 2. Analizar valores de mercado por posición
# 3. Comparar medias de diferentes métricas por liga
# 4. Identificar posiciones con mayor variabilidad en rendimiento
# 5. Calcular percentiles (25, 50, 75) para cada métrica
# 6. Crear tabla resumen con todas las medidas centrales
# 7. Interpretar diferencias entre posiciones
```

### Respuesta

*Completa el análisis de medidas de tendencia central.*

## Ejercicio 2: Medidas de Dispersión y Variabilidad (20 puntos)

### Análisis de Consistencia en el Rendimiento

```python
# Análisis de variabilidad en el rendimiento de equipos

# Tu código aquí:
# 1. Calcular rango, varianza y desviación estándar de goles por liga
# 2. Calcular coeficiente de variación para normalizar comparaciones
# 3. Identificar equipos más y menos consistentes en su rendimiento
# 4. Analizar dispersión de presupuestos por liga
# 5. Comparar variabilidad entre goles a favor y en contra
# 6. Calcular rango intercuartílico (IQR) para detectar outliers
# 7. Crear ranking de consistencia por múltiples métricas
```

### Análisis de Estabilidad de Jugadores

```python
# Simular datos de rendimiento temporal para análisis de consistencia
np.random.seed(42)

# Crear datos de goles por partido para varios jugadores
jugadores_rendimiento = {
    'Messi': np.random.normal(0.8, 0.3, 25),  # Media alta, baja variabilidad
    'Ronaldo': np.random.normal(0.7, 0.4, 25),  # Media alta, media variabilidad  
    'Haaland': np.random.normal(0.9, 0.5, 25),  # Media muy alta, alta variabilidad
    'Benzema': np.random.normal(0.6, 0.2, 25)   # Media media, muy baja variabilidad
}

# Tu código aquí:
# 1. Calcular todas las medidas de dispersión para cada jugador
# 2. Determinar qué jugador es más consistente
# 3. Identificar jugador con mayor potencial pero menos consistente
# 4. Calcular score de "fiabilidad" combinando media y desviación
# 5. Crear visualizaciones de distribución de rendimiento
# 6. Analizar qué tipo de jugador prefiere cada estrategia de equipo
# 7. Generar reporte de recomendaciones basado en estadísticas
```

### Respuesta

*Completa el análisis de variabilidad y consistencia.*

## Ejercicio 3: Análisis de Distribuciones y Normalidad (20 puntos)

### Estudio de Distribuciones en Datos Deportivos

```python
# Análisis de normalidad en diferentes variables

# Tu código aquí:
# 1. Crear histogramas de diferentes variables (goles, puntos, valores)
# 2. Aplicar test de Shapiro-Wilk para normalidad
# 3. Generar Q-Q plots para evaluación visual de normalidad
# 4. Identificar variables que siguen distribución normal
# 5. Analizar simetría y curtosis de las distribuciones
# 6. Comparar distribuciones entre diferentes ligas
# 7. Aplicar transformaciones para normalizar datos sesgados
```

### Análisis de Distribuciones por Categorías

```python
# Comparar distribuciones entre grupos

# Tu código aquí:
# 1. Comparar distribución de goles entre posiciones
# 2. Analizar si valores de mercado siguen distribución específica
# 3. Evaluar normalidad de salarios por liga
# 4. Aplicar test de Kolmogorov-Smirnov para comparar distribuciones
# 5. Identificar distribuciones que requieren métodos no paramétricos
# 6. Crear overlays de distribuciones para comparación visual
# 7. Generar conclusiones sobre patrones de distribución deportivos
```

### Respuesta

*Completa el análisis de distribuciones y normalidad.*

## Ejercicio 4: Detección y Análisis de Outliers (20 puntos)

### Identificación de Valores Atípicos

```python
# Métodos estadísticos para detectar outliers

def detectar_outliers_iqr(data, columna):
    """Detecta outliers usando método IQR"""
    Q1 = data[columna].quantile(0.25)
    Q3 = data[columna].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return data[(data[columna] < lower_bound) | (data[columna] > upper_bound)]

def detectar_outliers_zscore(data, columna, threshold=3):
    """Detecta outliers usando Z-score"""
    z_scores = np.abs(stats.zscore(data[columna]))
    return data[z_scores > threshold]

# Tu código aquí:
# 1. Aplicar método IQR para detectar outliers en goles y puntos
# 2. Usar Z-score para identificar outliers en valores de mercado
# 3. Comparar resultados de diferentes métodos de detección
# 4. Analizar si los outliers son errores o casos especiales legítimos
# 5. Crear visualizaciones (boxplots, scatterplots) para mostrar outliers
# 6. Determinar impacto de outliers en estadísticas descriptivas
# 7. Decidir estrategia de tratamiento para cada tipo de outlier
```

### Análisis Contextual de Outliers

```python
# Entender el significado deportivo de los outliers

# Tu código aquí:
# 1. Investigar el contexto de equipos/jugadores outliers
# 2. Categorizar outliers: excepcionales vs erróneos
# 3. Analizar correlaciones de outliers con otras variables
# 4. Evaluar si outliers siguen patrones específicos (liga, posición)
# 5. Crear perfil de características de outliers positivos/negativos
# 6. Generar insights sobre factores que crean rendimientos atípicos
# 7. Recomendar uso de outliers en análisis futuros
```

### Respuesta

*Completa la detección y análisis contextual de outliers.*

## Ejercicio 5: Reporte Estadístico Integral (20 puntos)

### Dashboard Estadístico Completo

```python
def generar_reporte_estadistico(df, variables_numericas, variable_categoria=None):
    """
    Genera reporte estadístico completo para análisis deportivo
    
    Parámetros:
    df (DataFrame): Dataset a analizar
    variables_numericas (list): Lista de variables numéricas
    variable_categoria (str): Variable para segmentación
    
    Retorna:
    dict: Reporte estadístico completo
    """
    # Tu código aquí:
    # 1. Calcular todas las medidas de tendencia central
    # 2. Incluir todas las medidas de dispersión
    # 3. Evaluar normalidad de distribuciones
    # 4. Detectar y reportar outliers
    # 5. Generar correlaciones entre variables
    # 6. Crear visualizaciones automáticas
    # 7. Producir interpretaciones en lenguaje natural
    # 8. Estructura: Executive Summary + Análisis Detallado
    pass

# Aplicar a diferentes conjuntos de datos
# reporte_equipos = generar_reporte_estadistico(
#     df_equipos, 
#     ['Puntos', 'Goles_Favor', 'Goles_Contra', 'Presupuesto'],
#     'Liga'
# )
```

### Análisis Comparativo Entre Ligas

```python
# Comparación estadística comprehensiva entre ligas

# Tu código aquí:
# 1. Crear tabla comparativa de estadísticas por liga
# 2. Realizar tests estadísticos para diferencias significativas
# 3. Calcular effect size para diferencias encontradas
# 4. Generar ranking de ligas por diferentes métricas
# 5. Identificar características distintivas de cada liga
# 6. Crear visualización multi-dimensional de comparaciones
# 7. Generar conclusiones sobre competitividad relativa
# 8. Proponer hipótesis para diferencias observadas
```

### Predicciones Basadas en Estadística Descriptiva

```python
# Usar estadística descriptiva para predicciones básicas

# Tu código aquí:
# 1. Establecer rangos esperados para rendimiento futuro
# 2. Identificar equipos/jugadores sobre/bajo su nivel histórico
# 3. Calcular probabilidades basadas en distribuciones históricas
# 4. Crear alertas para rendimientos anómalos
# 5. Generar expectativas realistas para próximas temporadas
# 6. Establecer benchmarks para evaluación de rendimiento
# 7. Crear sistema de scoring basado en percentiles históricos
```

### Respuesta

*Completa el reporte estadístico integral y análisis predictivo.*

## Ejercicio Bonus: Estadística Inferencial Básica (10 puntos extra)

### Tests de Hipótesis Aplicados al Fútbol

**Ejercicio opcional para puntos adicionales:**

```python
# Aplicar tests estadísticos básicos

# Tu código aquí:
# 1. Test t para comparar medias entre dos ligas
# 2. ANOVA para comparar múltiples ligas simultáneamente
# 3. Test de correlación de Pearson/Spearman
# 4. Chi-cuadrado para asociaciones categóricas
# 5. Test de Mann-Whitney para datos no paramétricos
# 6. Calcular intervalos de confianza para medias
# 7. Interpretar p-values en contexto deportivo
# 8. Generar conclusiones estadísticamente válidas

# Hipótesis a probar:
# - ¿La Premier League es significativamente más competitiva?
# - ¿Los presupuestos predicen el rendimiento?
# - ¿Hay diferencias reales entre posiciones en efectividad?
# - ¿Los jugadores jóvenes son más variables en rendimiento?
```

### Respuesta Bonus

*Ejercicio opcional: Aplica estadística inferencial al análisis deportivo.*

## Criterios de Evaluación

### Dominio Estadístico (45%)

- [ ] Cálculo correcto de medidas centrales y dispersión (15%)
- [ ] Análisis apropiado de distribuciones y normalidad (15%)
- [ ] Detección e interpretación correcta de outliers (15%)

### Aplicación Práctica (35%)

- [ ] Interpretación correcta en contexto deportivo (20%)
- [ ] Insights relevantes y bien fundamentados (15%)

### Presentación y Comunicación (20%)

- [ ] Reporte estadístico claro y profesional (10%)
- [ ] Visualizaciones efectivas de conceptos estadísticos (10%)

## Instrucciones de Entrega

1. **Completa todos los ejercicios** con análisis estadístico riguroso
2. **Incluye interpretaciones** para cada resultado estadístico
3. **Valida tus cálculos** usando múltiples métodos cuando sea posible
4. **Guarda como:** `ejercicio-semana-8-[tu-apellido].ipynb`
5. **Entrega antes del final de Semana 8**

## Recursos de Apoyo

- Notebook de la Semana 8: `estadistica-descriptiva.ipynb`
- Documentación SciPy stats: <https://docs.scipy.org/doc/scipy/reference/stats.html>
- Pandas describe: <https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html>
- Seaborn distributions: <https://seaborn.pydata.org/tutorial/distributions.html>

---

**¡Descubre los patrones ocultos en los números del fútbol mundial!** ⚽📊
