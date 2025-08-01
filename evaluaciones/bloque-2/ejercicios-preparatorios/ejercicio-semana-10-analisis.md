# Ejercicio Semana 10: Análisis e Interpretación Integral de Datos Deportivos

## Información del Ejercicio

**Bloque:** 2 - Fundamentos de Data Science  
**Peso:** 12% de la calificación del bloque (60% ÷ 5 ejercicios)  
**Tiempo estimado:** 3-4 horas  
**Entrega:** Final de Semana 10

## Objetivos

Al completar este ejercicio, serás capaz de:

- Integrar todas las técnicas de análisis aprendidas en el Bloque 2
- Realizar análisis multidimensional completo de datos deportivos
- Generar insights profundos y recomendaciones basadas en evidencia
- Comunicar hallazgos de manera profesional y convincente
- Desarrollar pensamiento crítico para análisis de datos deportivos
- Crear reportes ejecutivos con conclusiones accionables

## Configuración Inicial

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from scipy import stats
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import warnings
warnings.filterwarnings('ignore')

# Configurar estilos
sns.set_theme(style="whitegrid", palette="viridis")
plt.rcParams['figure.figsize'] = (14, 10)

# Cargar todos los datasets disponibles
df_equipos = pd.read_csv('equipos-europa-2023-24.csv')
df_jugadores = pd.read_csv('jugadores-estrellas-2024.csv')

print("¡Sistema completo de análisis deportivo activado!")
```

## Ejercicio 1: Análisis Multidimensional Integrado (25 puntos)

### Análisis de Correlaciones y Patrones Complejos

```python
# Análisis profundo de relaciones entre variables

# Tu código aquí:
# 1. Crear matriz de correlación completa entre todas las variables numéricas
# 2. Identificar correlaciones sorprendentes o contraintuitivas
# 3. Aplicar análisis de componentes principales (PCA) para reducir dimensionalidad
# 4. Interpretar los componentes principales en contexto deportivo
# 5. Crear clusters de equipos/jugadores usando múltiples variables
# 6. Analizar patrones dentro de cada cluster identificado
# 7. Validar hallazgos usando diferentes métodos estadísticos
# 8. Generar hipótesis sobre relaciones causales vs correlacionales
```

### Análisis de Eficiencia Multifactorial

```python
# Desarrollo de métricas de eficiencia complejas

def calcular_eficiencia_integral(df_equipos):
    """
    Calcula índice de eficiencia considerando múltiples factores
    """
    # Tu código aquí:
    # 1. Crear métrica de eficiencia deportiva (puntos vs recursos)
    # 2. Desarrollar índice de consistencia (variabilidad de rendimiento)
    # 3. Calcular eficiencia económica (resultados vs presupuesto)
    # 4. Generar score de sostenibilidad (rendimiento a largo plazo)
    # 5. Combinar métricas en índice integral ponderado
    # 6. Validar índice con resultados conocidos
    # 7. Crear ranking de eficiencia multidimensional
    # 8. Identificar outliers y casos especiales
    pass

# Aplicar análisis de eficiencia
# indices_eficiencia = calcular_eficiencia_integral(df_equipos)

# Análisis comparativo por liga
# Tu código aquí:
# 1. Comparar eficiencias promedio entre ligas
# 2. Identificar modelos de negocio más exitosos
# 3. Analizar correlación entre diferentes tipos de eficiencia
# 4. Detectar equipos que superan o no alcanzan expectativas
# 5. Proponer estrategias de mejora basadas en benchmarks
```

### Respuesta

*Completa el análisis multidimensional integrado.*

## Ejercicio 2: Análisis Predictivo Básico (25 puntos)

### Predicción de Rendimiento Futuro

```python
# Usar datos históricos para predicciones simples

# Simular datos de múltiples temporadas
temporadas = ['2021-22', '2022-23', '2023-24']
equipos_historicos = []

# Crear datos históricos simulados
np.random.seed(42)
for temporada in temporadas:
    for _, equipo in df_equipos.iterrows():
        equipos_historicos.append({
            'Temporada': temporada,
            'Equipo': equipo['Equipo'],
            'Liga': equipo['Liga'],
            'Puntos': equipo['Puntos'] + np.random.normal(0, 8),
            'Goles_Favor': equipo['Goles_Favor'] + np.random.normal(0, 10),
            'Presupuesto': equipo['Presupuesto'] + np.random.normal(0, 50)
        })

df_historico = pd.DataFrame(equipos_historicos)

# Tu código aquí:
# 1. Analizar tendencias de rendimiento por equipo a lo largo del tiempo
# 2. Identificar equipos en ascenso, descenso o estables
# 3. Crear modelo simple de predicción basado en tendencias lineales
# 4. Calcular intervalos de confianza para predicciones
# 5. Validar predicciones con datos conocidos (temporada actual)
# 6. Identificar factores que más influyen en cambios de rendimiento
# 7. Generar predicciones para próxima temporada (2024-25)
# 8. Cuantificar incertidumbre en las predicciones
```

### Análisis de Escenarios

```python
# Análisis de diferentes escenarios posibles

def analizar_escenarios(equipo_data, factores_cambio):
    """
    Analiza diferentes escenarios para un equipo
    
    Parámetros:
    equipo_data: Datos actuales del equipo
    factores_cambio: Diccionario con posibles cambios
    """
    # Tu código aquí:
    # 1. Escenario conservador: Sin cambios significativos
    # 2. Escenario optimista: Mejora en factores clave
    # 3. Escenario pesimista: Deterioro en métricas importantes
    # 4. Escenario de inversión: Aumento de presupuesto
    # 5. Calcular impacto probable de cada escenario
    # 6. Generar distribución de resultados posibles
    # 7. Identificar factores de mayor impacto
    # 8. Crear recomendaciones estratégicas
    pass

# Aplicar análisis de escenarios a equipos clave
equipos_analizar = ['Barcelona', 'Real Madrid', 'Manchester City']

# for equipo in equipos_analizar:
#     datos_equipo = df_equipos[df_equipos['Equipo'] == equipo]
#     escenarios = analizar_escenarios(datos_equipo, factores_cambio)
```

### Respuesta

*Completa el análisis predictivo y de escenarios.*

## Ejercicio 3: Análisis de Mercado y Valoraciones (25 puntos)

### Análisis del Mercado de Jugadores

```python
# Análisis profundo del mercado de transferencias

# Tu código aquí:
# 1. Identificar jugadores sobrevalorados y subvalorados
# 2. Analizar relación entre rendimiento y valor de mercado
# 3. Crear modelo de valoración basado en métricas objetivas
# 4. Comparar valoraciones entre ligas y posiciones
# 5. Identificar oportunidades de mercado (gangas potenciales)
# 6. Analizar inflación en valores según edad y posición
# 7. Predecir evolución de valores basada en rendimiento
# 8. Generar alertas de inversión para equipos

def detectar_oportunidades_mercado(df_jugadores, umbral_descuento=0.3):
    """
    Detecta jugadores potencialmente subvalorados
    
    Parámetros:
    df_jugadores: DataFrame con datos de jugadores
    umbral_descuento: Umbral para considerar una oportunidad
    """
    # Tu código aquí:
    # 1. Calcular valor teórico basado en rendimiento
    # 2. Comparar con valor de mercado actual
    # 3. Identificar discrepancias significativas
    # 4. Considerar factores adicionales (edad, liga, potencial)
    # 5. Generar score de oportunidad
    # 6. Crear lista priorizada de recomendaciones
    pass

# oportunidades = detectar_oportunidades_mercado(df_jugadores)
```

### Análisis de ROI en Fichajes

```python
# Análisis de retorno de inversión en fichajes

# Simular datos de fichajes y rendimiento posterior
fichajes_simulados = {
    'Jugador': ['Haaland', 'Bellingham', 'Gvardiol', 'Rice', 'Osimhen'],
    'Equipo_Destino': ['Manchester City', 'Real Madrid', 'Manchester City', 'Arsenal', 'PSG'],
    'Costo_Millones': [75, 103, 90, 116, 120],
    'Rendimiento_Esperado': [85, 78, 72, 75, 80],  # Score 0-100
    'Rendimiento_Real': [92, 82, 68, 77, 74],      # Score real observado
    'Impacto_Equipo': [15, 12, 8, 10, 9]           # Mejora en puntos del equipo
}

df_fichajes = pd.DataFrame(fichajes_simulados)

# Tu código aquí:
# 1. Calcular ROI de cada fichaje
# 2. Comparar expectativas vs realidad
# 3. Identificar factores de éxito en fichajes
# 4. Analizar impacto en rendimiento del equipo
# 5. Crear modelo de evaluación pre-fichaje
# 6. Generar recomendaciones para futuros fichajes
# 7. Analizar patrones por liga, posición y rango de precio
# 8. Desarrollar sistema de alertas tempranas sobre rendimiento
```

### Respuesta

*Completa el análisis de mercado y valoraciones.*

## Ejercicio 4: Reporte Ejecutivo Integral (25 puntos)

### Síntesis y Comunicación de Hallazgos

```python
def generar_reporte_ejecutivo(analisis_completo):
    """
    Genera reporte ejecutivo con hallazgos principales
    
    Estructura:
    1. Executive Summary (2-3 párrafos)
    2. Hallazgos Clave (5-7 insights principales)
    3. Análisis por Liga
    4. Recomendaciones Estratégicas
    5. Riesgos y Oportunidades
    6. Conclusiones y Próximos Pasos
    """
    # Tu código aquí:
    # 1. Identificar los 3 insights más importantes
    # 2. Cuantificar impacto económico/deportivo de hallazgos
    # 3. Priorizar recomendaciones por impacto y factibilidad
    # 4. Crear timeline para implementación
    # 5. Identificar métricas de seguimiento
    # 6. Documentar limitaciones del análisis
    # 7. Proponer análisis adicionales necesarios
    # 8. Formatear para audiencia ejecutiva
    pass

# Crear secciones del reporte

# Executive Summary
executive_summary = """
Tu código aquí:
Escribir resumen ejecutivo de 2-3 párrafos que incluya:
- Objetivo del análisis
- Metodología empleada
- Hallazgos más importantes
- Valor del análisis para la organización
"""

# Hallazgos Clave
hallazgos_clave = [
    # Tu código aquí:
    # 1. "La Liga X muestra mayor eficiencia económica con Y% menos presupuesto"
    # 2. "Jugadores de posición Z están subvalorados en promedio 30%"
    # 3. "Equipos con estrategia W tienen 40% más probabilidad de éxito"
    # 4. "Factor X explica 65% de la variabilidad en rendimiento"
    # 5. "Tendencia Y sugiere cambio estructural en el mercado"
]

# Recomendaciones Estratégicas
recomendaciones = {
    'Corto_Plazo': [
        # Acciones para próximos 6 meses
    ],
    'Mediano_Plazo': [
        # Estrategias para 1-2 años
    ],
    'Largo_Plazo': [
        # Visión estratégica 3-5 años
    ]
}
```

### Dashboard Ejecutivo Final

```python
# Crear dashboard final con métricas clave

def crear_dashboard_ejecutivo():
    """
    Dashboard de una página con métricas más importantes
    """
    # Tu código aquí:
    # 1. KPI principales en la parte superior
    # 2. Gráfico de eficiencia por liga
    # 3. Top 5 oportunidades de mercado
    # 4. Alertas y riesgos identificados
    # 5. Tendencias temporales clave
    # 6. Comparaciones competitivas
    # 7. Navegación intuitiva
    # 8. Exportación automática a PDF/PowerPoint
    
    # Usar plotly para interactividad
    fig = make_subplots(
        rows=3, cols=2,
        subplot_titles=[
            'Eficiencia por Liga', 'Oportunidades de Mercado',
            'Tendencias Temporales', 'Análisis de Riesgo',
            'Comparación Competitiva', 'Métricas de Rendimiento'
        ]
    )
    
    # Agregar cada visualización
    # ...
    
    # Configurar layout profesional
    fig.update_layout(
        title="Dashboard Ejecutivo - Análisis Integral de Fútbol",
        showlegend=True,
        height=800
    )
    
    return fig

# dashboard_ejecutivo = crear_dashboard_ejecutivo()
```

### Validación y Control de Calidad

```python
# Sistema de validación de análisis

def validar_analisis(resultados_analisis):
    """
    Valida la calidad y consistencia del análisis realizado
    """
    # Tu código aquí:
    # 1. Verificar consistencia estadística de resultados
    # 2. Validar que conclusiones están respaldadas por datos
    # 3. Revisar que no hay sesgos evidentes
    # 4. Confirmar que el análisis responde preguntas originales
    # 5. Evaluar completitud del análisis
    # 6. Verificar calidad de visualizaciones
    # 7. Revisar claridad de comunicación
    # 8. Generar score de calidad general
    
    checklist_calidad = {
        'datos_validados': False,
        'metodos_apropiados': False,
        'conclusiones_respaldadas': False,
        'comunicacion_clara': False,
        'insights_accionables': False,
        'limitaciones_identificadas': False
    }
    
    # Evaluar cada criterio
    # ...
    
    return checklist_calidad

# validacion = validar_analisis(mi_analisis)
```

### Respuesta

*Completa el reporte ejecutivo integral y validación.*

## Ejercicio Bonus: Análisis de Impacto Social y Mediático (Extra)

### Análisis Integral de Valor

**Ejercicio opcional para puntos adicionales:**

```python
# Análisis que va más allá de métricas deportivas

# Tu código aquí:
# 1. Analizar correlación entre rendimiento deportivo e impacto mediático
# 2. Evaluar valor de marca de equipos/jugadores
# 3. Considerar factores sociales y culturales en valoraciones
# 4. Analizar sostenibilidad financiera a largo plazo
# 5. Evaluar impacto de decisiones en fanbase global
# 6. Crear métricas de valor integral (deportivo + comercial + social)
# 7. Proponer estrategias de optimización holística
# 8. Generar proyecciones de valor de marca futuro

# Métricas innovadoras a considerar:
# - Engagement en redes sociales
# - Valor de derechos televisivos
# - Impacto en patrocinadores
# - Desarrollo de base de fans
# - Sostenibilidad económica
# - Responsabilidad social
```

### Respuesta Bonus

*Ejercicio opcional: Desarrolla análisis de impacto integral.*

## Criterios de Evaluación

### Integración de Técnicas (30%)

- [ ] Uso efectivo de múltiples técnicas de análisis (15%)
- [ ] Combinación apropiada de estadística descriptiva e inferencial (15%)

### Calidad de Insights (35%)

- [ ] Profundidad y originalidad de hallazgos (20%)
- [ ] Relevancia práctica para contexto deportivo (15%)

### Comunicación y Presentación (35%)

- [ ] Claridad en comunicación de resultados (15%)
- [ ] Calidad de reporte ejecutivo (10%)
- [ ] Efectividad de visualizaciones integradas (10%)

## Instrucciones de Entrega

1. **Completa análisis integral** usando todas las técnicas del Bloque 2
2. **Genera reporte ejecutivo** con hallazgos principales
3. **Incluye validación** de la calidad del análisis
4. **Documenta metodología** y limitaciones
5. **Guarda como:** `ejercicio-semana-10-[tu-apellido].ipynb`
6. **Entrega antes del final de Semana 10**

## Recursos de Apoyo

- Notebook de la Semana 10: `analisis-interpretacion.ipynb`
- Todos los notebooks previos del Bloque 2
- Templates de reportes ejecutivos
- Guías de mejores prácticas en análisis deportivo

---

**¡Culmina tu formación en Data Science deportivo con un análisis magistral!** ⚽🏆
