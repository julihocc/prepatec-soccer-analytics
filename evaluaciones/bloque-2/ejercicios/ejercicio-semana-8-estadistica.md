# Ejercicio Semana 8: Estadística Descriptiva Deportiva

## Información General

**Bloque:** 2 - Fundamentos de Data Science  
**Semana:** 8  
**Tiempo estimado:** 60 minutos  
**Puntos totales:** 100 puntos  
**Fecha límite:** Final de la Semana 8  
**Archivo entrega:** `[matricula]-ejercicio-semana-8.ipynb`

## Objetivos de Aprendizaje

Al completar este ejercicio, el estudiante será capaz de:
- Calcular e interpretar medidas de tendencia central en análisis deportivo
- Aplicar medidas de dispersión para evaluar variabilidad en rendimiento
- Identificar y analizar valores atípicos en estadísticas futbolísticas
- Realizar análisis de distribuciones para caracterizar rendimiento
- Comparar equipos y jugadores usando estadística descriptiva avanzada

## Prerrequisitos

- Ejercicios de las Semanas 6-7 completados exitosamente
- Conocimiento sólido de pandas y tipos de datos
- Comprensión básica de conceptos estadísticos
- Familiaridad con visualizaciones en seaborn

## Contexto del Ejercicio

Eres el **estadístico jefe** del departamento de análisis del Arsenal FC. El cuerpo técnico necesita un análisis estadístico profundo para:

- Evaluar la consistencia del rendimiento del equipo
- Comparar estadísticamente con la competencia
- Identificar fortalezas y debilidades usando métrica objetivas
- Generar reportes estadísticos para la junta directiva

---

# Ejercicio Integrador: Análisis Estadístico Arsenal FC

## Parte 1: Medidas de Tendencia Central (25 puntos)

### Objetivo
Calcular y comparar medidas de tendencia central para evaluar el rendimiento del Arsenal vs competencia.

### Instrucciones Detalladas

**Paso 1:** Configura el entorno estadístico:

```python
# Configuración del laboratorio estadístico Arsenal FC
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

# Configuración visual para Arsenal
sns.set_theme(style="whitegrid", palette="viridis")
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 11

print("=== LABORATORIO ESTADÍSTICO ARSENAL FC ===")
print("Sistema de análisis estadístico deportivo iniciado")
print("¡Herramientas de análisis listas!")

# Cargar datos de equipos europeos
df_equipos = pd.read_csv('equipos-europa-2023-24.csv')
print(f"Analizando {len(df_equipos)} equipos de élite europea")
```

**Paso 2:** Calcula medidas de tendencia central:

```python
# Análisis de tendencia central en rendimiento ofensivo

# TU CÓDIGO AQUÍ:
# 1. Extraer datos de goles a favor de todos los equipos
# 2. Calcular media, mediana y moda de goles por liga
# 3. Identificar la posición del Arsenal en cada métrica
# 4. Comparar Arsenal vs promedio de Premier League
# 5. Calcular percentiles (25, 50, 75, 90) para goles y puntos
# 6. Determinar en qué percentil está el Arsenal
# 7. Crear ranking de equipos por media de múltiples métricas

goles_por_liga = df_equipos.groupby('Liga')['Goles_Favor'].agg(['mean', 'median', 'std']).round(2)

print("=== ANÁLISIS DE TENDENCIA CENTRAL ARSENAL ===")
print("\n1. POSICIÓN OFENSIVA DEL ARSENAL:")
# Implementar análisis específico del Arsenal

print("\n2. COMPARACIÓN POR LIGAS:")
# Mostrar estadísticas por liga

print("\n3. PERCENTILES DE RENDIMIENTO:")
# Calcular y mostrar percentiles
```

### Criterios de Evaluación
- **Cálculos estadísticos correctos** (15 puntos)
- **Interpretación en contexto Arsenal** (10 puntos)

---

## Parte 2: Medidas de Dispersión y Variabilidad (25 puntos)

### Objetivo
Analizar la consistencia y variabilidad del rendimiento utilizando medidas de dispersión.

### Instrucciones Detalladas

**Paso 3:** Calcula medidas de dispersión:

```python
# Análisis de consistencia y variabilidad en rendimiento

# TU CÓDIGO AQUÍ:
# 1. Calcular desviación estándar de goles, puntos y presupuesto por liga
# 2. Calcular coeficiente de variación para comparar ligas
# 3. Identificar liga más consistente (menor variabilidad)
# 4. Analizar dispersión en relación presupuesto-rendimiento
# 5. Calcular rango intercuartílico (IQR) para detectar outliers
# 6. Determinar qué liga tiene mayor competitividad (variabilidad en puntos)

# Análisis de variabilidad por liga
variabilidad_ligas = df_equipos.groupby('Liga').agg({
    'Puntos': ['std', 'var'],
    'Goles_Favor': ['std', 'var'],
    'Presupuesto': ['std', 'var']
}).round(2)

print("=== ANÁLISIS DE VARIABILIDAD Y CONSISTENCIA ===")
print("\n1. CONSISTENCIA POR LIGA:")
# Mostrar análisis de variabilidad

print("\n2. COMPETITIVIDAD (DISPERSIÓN DE PUNTOS):")
# Identificar liga más competitiva

print("\n3. EFICIENCIA PRESUPUESTARIA:")
# Analizar relación presupuesto-variabilidad
```

**Paso 4:** Identifica y analiza valores atípicos:

```python
# Detección y análisis de outliers

# TU CÓDIGO AQUÍ:
# 1. Usar método IQR para detectar outliers en goles y puntos
# 2. Identificar equipos outliers (positivos y negativos)
# 3. Analizar si Arsenal es outlier en alguna métrica
# 4. Crear visualización de boxplots para mostrar outliers
# 5. Calcular z-scores para identificar valores extremos
# 6. Interpretar qué significan estos outliers en contexto deportivo

def detectar_outliers_iqr(serie, factor=1.5):
    """Detecta outliers usando método IQR"""
    Q1 = serie.quantile(0.25)
    Q3 = serie.quantile(0.75)
    IQR = Q3 - Q1
    limite_inferior = Q1 - factor * IQR
    limite_superior = Q3 + factor * IQR
    return serie[(serie < limite_inferior) | (serie > limite_superior)]

print("=== DETECCIÓN DE VALORES ATÍPICOS ===")
# Aplicar análisis de outliers
```

### Criterios de Evaluación
- **Análisis de dispersión correcto** (15 puntos)
- **Detección e interpretación de outliers** (10 puntos)

---

## Parte 3: Análisis de Distribuciones (25 puntos)

### Objetivo
Analizar las distribuciones de variables clave para entender patrones de rendimiento.

### Instrucciones Detalladas

**Paso 5:** Analiza distribuciones de variables:

```python
# Análisis de distribuciones en métricas deportivas

# TU CÓDIGO AQUÍ:
# 1. Crear histogramas de goles, puntos y presupuesto
# 2. Calcular medidas de forma: asimetría (skewness) y curtosis
# 3. Probar normalidad usando test de Shapiro-Wilk
# 4. Comparar distribuciones entre ligas
# 5. Identificar si alguna variable sigue distribución normal
# 6. Crear Q-Q plots para verificar normalidad visualmente

# Análisis de forma de distribuciones
from scipy.stats import skew, kurtosis, shapiro

metricas_forma = {}
for columna in ['Puntos', 'Goles_Favor', 'Presupuesto']:
    datos = df_equipos[columna]
    metricas_forma[columna] = {
        'asimetria': skew(datos),
        'curtosis': kurtosis(datos),
        'shapiro_p': shapiro(datos)[1]
    }

print("=== ANÁLISIS DE DISTRIBUCIONES ===")
print("\n1. FORMA DE DISTRIBUCIONES:")
# Mostrar métricas de forma

print("\n2. PRUEBAS DE NORMALIDAD:")
# Interpretar resultados de normalidad

print("\n3. COMPARACIÓN ENTRE LIGAS:")
# Analizar diferencias distribucionales
```

**Paso 6:** Crea visualizaciones de distribuciones:

```python
# Dashboard de distribuciones múltiples

# TU CÓDIGO AQUÍ:
# 1. Crear subplot con 6 gráficos:
#    - Histograma de puntos por liga
#    - Boxplot de goles por liga
#    - Distribución de presupuestos (log scale)
#    - Q-Q plot de puntos vs normal
#    - Kernel density de goles por liga
#    - Violin plot de eficiencia (puntos/presupuesto)
# 2. Añadir líneas de referencia (media, mediana)
# 3. Destacar posición del Arsenal en cada gráfico
# 4. Incluir estadísticas relevantes en cada plot

fig, axes = plt.subplots(2, 3, figsize=(15, 10))
# Implementar visualizaciones

plt.suptitle("Análisis de Distribuciones: Fútbol Europeo 2023-24", fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()

print("Dashboard de distribuciones generado para análisis Arsenal")
```

### Criterios de Evaluación
- **Análisis distribucional completo** (15 puntos)
- **Visualizaciones estadísticas efectivas** (10 puntos)

---

## Parte 4: Reporte Estadístico Ejecutivo (25 puntos)

### Objetivo
Generar un reporte estadístico profesional con conclusiones para la dirección del Arsenal.

### Instrucciones Detalladas

**Paso 7:** Genera análisis comparativo completo:

```python
# Análisis estadístico comparativo Arsenal vs competencia

# TU CÓDIGO AQUÍ:
# 1. Crear perfil estadístico completo del Arsenal
# 2. Comparar Arsenal vs promedio de Premier League
# 3. Posicionar Arsenal en rankings europeos
# 4. Identificar fortalezas estadísticas del Arsenal
# 5. Detectar áreas de mejora basadas en datos
# 6. Calcular correlaciones entre métricas del Arsenal

def crear_perfil_estadistico(equipo_nombre, dataframe):
    """Crea perfil estadístico completo de un equipo"""
    equipo_data = dataframe[dataframe['Equipo'] == equipo_nombre]
    if len(equipo_data) == 0:
        return None
    
    # Tu implementación aquí
    perfil = {}
    return perfil

print("=== REPORTE ESTADÍSTICO ARSENAL FC ===")
print("\n1. PERFIL ESTADÍSTICO ARSENAL:")
# Generar perfil completo

print("\n2. POSICIÓN COMPETITIVA:")
# Comparar con competencia

print("\n3. ANÁLISIS DE FORTALEZAS:")
# Identificar ventajas estadísticas

print("\n4. ÁREAS DE MEJORA:")
# Detectar debilidades
```

**Paso 8:** Crea dashboard ejecutivo final:

```python
# Dashboard ejecutivo para presentación a la junta directiva

# TU CÓDIGO AQUÍ:
# 1. Crear visualización tipo "spider chart" con métricas clave del Arsenal
# 2. Gráfico de barras: Arsenal vs Top 5 equipos europeos
# 3. Scatter plot: Eficiencia presupuestaria (Arsenal destacado)
# 4. Trend chart: Progresión histórica (simular datos)
# 5. Heatmap de correlaciones entre métricas del Arsenal
# 6. Incluir estadísticas clave y percentiles

print("=== DASHBOARD EJECUTIVO ARSENAL FC ===")

# Métricas clave para la junta directiva
metricas_clave = {
    'Rendimiento Ofensivo': 'percentil',
    'Eficiencia Defensiva': 'percentil', 
    'Consistencia': 'ranking',
    'Eficiencia Presupuestaria': 'percentil',
    'Competitividad Liga': 'posición'
}

print("\n🎯 MÉTRICAS CLAVE ARSENAL FC:")
for metrica, tipo in metricas_clave.items():
    # Calcular y mostrar cada métrica
    pass

print("\n📊 RECOMENDACIONES ESTRATÉGICAS:")
print("1. [Basada en análisis estadístico]")
print("2. [Basada en análisis estadístico]") 
print("3. [Basada en análisis estadístico]")

# Crear visualización final
plt.figure(figsize=(14, 10))
# Implementar dashboard ejecutivo
plt.suptitle("Arsenal FC: Dashboard Estadístico Ejecutivo 2023-24", fontsize=16, fontweight='bold')
plt.show()
```

### Criterios de Evaluación
- **Reporte estadístico profesional** (15 puntos)
- **Dashboard ejecutivo efectivo** (10 puntos)

## Criterios de Evaluación General

### Correctitud Técnica (40 puntos)
- Cálculos estadísticos precisos y verificables
- Uso correcto de métodos estadísticos
- Implementación adecuada de pruebas de hipótesis
- Detección correcta de outliers y normalidad

### Aplicación Práctica (30 puntos)
- Interpretación relevante para contexto Arsenal
- Insights útiles para toma de decisiones
- Comparaciones significativas con competencia
- Recomendaciones basadas en evidencia estadística

### Claridad y Documentación (30 puntos)
- Explicaciones claras de resultados estadísticos
- Visualizaciones profesionales y comprensibles
- Reporte ejecutivo bien estructurado
- Variables y análisis con nombres descriptivos

## Instrucciones de Entrega

1. **Completa todos los análisis** con rigor estadístico
2. **Incluye interpretaciones** para cada resultado estadístico
3. **Verifica cálculos** con métodos alternativos cuando sea posible
4. **Guarda como:** `[matricula]-ejercicio-semana-8.ipynb`
5. **Entrega antes del final de Semana 8**

## Recursos de Apoyo

- Notebook de la Semana 8: `estadistica-descriptiva.ipynb`
- Dataset: `equipos-europa-2023-24.csv`
- Documentación scipy.stats: Pruebas estadísticas
- Guía de interpretación estadística en deportes

---

**¡Domina la estadística descriptiva y convierte al Arsenal en una potencia basada en datos!** ⚽📈

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
