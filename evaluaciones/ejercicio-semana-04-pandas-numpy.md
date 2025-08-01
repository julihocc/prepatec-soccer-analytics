# Ejercicio Semana 4: Pandas y NumPy - Introducción

## 📋 Información General

**Bloque:** 1 - Prerrequisitos de Programación  
**Semana:** 4  
**Tiempo estimado:** 60 minutos  
**Puntos totales:** 100 puntos  
**Fecha límite:** Final de la Semana 4

## 🎯 Objetivos de Aprendizaje

Al completar este ejercicio, el estudiante será capaz de:

- Manipular datos deportivos usando pandas DataFrames
- Realizar cálculos estadísticos con NumPy
- Filtrar y agrupar datos de equipos y jugadores
- Crear análisis básicos de rendimiento deportivo

## 📚 Conocimientos Previos Requeridos

- Funciones y programación modular
- Manipulación básica de pandas DataFrames
- Operaciones con arrays de NumPy
- Indexación y filtrado de datos

## 🚀 Ejercicio: Análisis de Datos de La Liga

### Contexto

Como analista de datos deportivos, has recibido datos de La Liga española y necesitas realizar un análisis completo usando pandas y NumPy. Los datos incluyen información de equipos, jugadores y partidos de la temporada 2023-24.

### Parte 1: Preparación y Exploración de Datos (25 puntos)

**Instrucciones:**
Crea y explora los datasets básicos:

```python
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Configurar pandas para mejor visualización
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

print("🏈 SISTEMA DE ANÁLISIS DE LA LIGA ESPAÑOLA")
print("=" * 60)

# 1. Crear dataset de equipos
equipos_data = {
    'equipo': ['Barcelona', 'Real Madrid', 'Atletico Madrid', 'Sevilla', 'Real Sociedad', 
               'Villarreal', 'Athletic Bilbao', 'Valencia', 'Real Betis', 'Osasuna'],
    'ciudad': ['Barcelona', 'Madrid', 'Madrid', 'Sevilla', 'San Sebastian',
               'Villarreal', 'Bilbao', 'Valencia', 'Sevilla', 'Pamplona'],
    'fundacion': [1899, 1902, 1903, 1890, 1909, 1923, 1898, 1919, 1907, 1920],
    'estadio_capacidad': [99354, 81044, 68456, 43883, 39500, 23500, 53289, 49430, 60721, 23516],
    'presupuesto_millones': [1350, 1200, 350, 200, 120, 180, 150, 90, 110, 45]
}

df_equipos = pd.DataFrame(equipos_data)

# Tu código aquí
print("📊 INFORMACIÓN BÁSICA DEL DATASET DE EQUIPOS:")
print(f"Número de equipos: {len(df_equipos)}")
print(f"Columnas disponibles: {list(df_equipos.columns)}")
print("\nPrimeras 5 filas:")
print(df_equipos.head())

print("\n📈 ESTADÍSTICAS DESCRIPTIVAS:")
# Tu código para mostrar estadísticas de columnas numéricas
print(df_equipos.describe())

# 2. Crear dataset de jugadores
np.random.seed(42)  # Para resultados reproducibles

jugadores_data = {
    'nombre': ['Lewandowski', 'Benzema', 'Griezmann', 'En-Nesyri', 'Oyarzabal',
               'Moreno', 'Williams', 'Cavani', 'Fekir', 'Budimir'],
    'equipo': ['Barcelona', 'Real Madrid', 'Atletico Madrid', 'Sevilla', 'Real Sociedad',
               'Villarreal', 'Athletic Bilbao', 'Valencia', 'Real Betis', 'Osasuna'],
    'posicion': ['Delantero', 'Delantero', 'Delantero', 'Delantero', 'Delantero',
                'Delantero', 'Delantero', 'Delantero', 'Centrocampista', 'Delantero'],
    'edad': np.random.randint(22, 35, 10),
    'goles': np.random.randint(8, 25, 10),
    'asistencias': np.random.randint(2, 12, 10),
    'partidos_jugados': np.random.randint(20, 30, 10),
    'minutos_jugados': np.random.randint(1800, 2700, 10)
}

df_jugadores = pd.DataFrame(jugadores_data)

# Tu código aquí
print("\n👤 INFORMACIÓN DEL DATASET DE JUGADORES:")
print(f"Número de jugadores: {len(df_jugadores)}")
print(f"Equipos representados: {df_jugadores['equipo'].nunique()}")
print(f"Posiciones: {df_jugadores['posicion'].unique()}")

# Mostrar información de cada jugador
print("\n🎯 DATOS DE JUGADORES:")
# Tu código para mostrar nombre, equipo, goles y asistencias de cada jugador

# 3. Calcular métricas adicionales usando NumPy
print("\n📊 MÉTRICAS CALCULADAS CON NUMPY:")

# Tu código aquí - calcula usando NumPy:
# - Promedio de goles por partido para cada jugador
df_jugadores['goles_por_partido'] = # Tu código

# - Promedio de minutos por partido
df_jugadores['minutos_por_partido'] = # Tu código  

# - Contribución total (goles + asistencias)
df_jugadores['contribucion_total'] = # Tu código

# Mostrar las nuevas columnas
print("Nuevas métricas calculadas:")
columnas_mostrar = ['nombre', 'goles_por_partido', 'minutos_por_partido', 'contribucion_total']
print(df_jugadores[columnas_mostrar].round(2))
```

### Parte 2: Análisis con Filtros y Agrupaciones (30 puntos)

**Instrucciones:**
Realiza análisis usando filtros y agrupaciones de pandas:

```python
print("\n" + "="*60)
print("🔍 ANÁLISIS CON FILTROS Y AGRUPACIONES")
print("="*60)

# 1. Filtrar datos
print("\n🎯 ANÁLISIS DE DELANTEROS TOP:")

# Tu código aquí
# Filtrar jugadores con más de 15 goles
delanteros_top = # Tu código

print(f"Delanteros con más de 15 goles: {len(delanteros_top)}")
if len(delanteros_top) > 0:
    print(delanteros_top[['nombre', 'equipo', 'goles', 'asistencias']].sort_values('goles', ascending=False))
else:
    print("No hay delanteros con más de 15 goles en el dataset actual.")

# 2. Filtrar equipos por presupuesto
print("\n💰 EQUIPOS CON ALTO PRESUPUESTO:")

# Tu código aquí
# Filtrar equipos con presupuesto mayor a 200 millones
equipos_ricos = # Tu código

print(f"Equipos con presupuesto > 200M: {len(equipos_ricos)}")
print(equipos_ricos[['equipo', 'presupuesto_millones', 'estadio_capacidad']].sort_values('presupuesto_millones', ascending=False))

# 3. Agrupaciones y estadísticas
print("\n📈 ESTADÍSTICAS POR EQUIPO:")

# Tu código aquí  
# Agrupar jugadores por equipo y calcular estadísticas
stats_por_equipo = df_jugadores.groupby('equipo').agg({
    'goles': # Tu código para suma, promedio, máximo
    'asistencias': # Tu código
    'partidos_jugados': # Tu código  
    'contribucion_total': # Tu código
}).round(2)

print("Estadísticas agrupadas por equipo:")
print(stats_por_equipo)

# 4. Ranking de equipos por diferentes criterios
print("\n🏆 RANKINGS DE EQUIPOS:")

# Tu código aquí
# Crear ranking por total de goles
ranking_goles = stats_por_equipo.sort_values(('goles', 'sum'), ascending=False)
print("\n🥅 Top 5 equipos por total de goles:")
print(ranking_goles[('goles', 'sum')].head())

# Crear ranking por promedio de contribución total
ranking_contribucion = stats_por_equipo.sort_values(('contribucion_total', 'mean'), ascending=False)
print("\n⭐ Top 5 equipos por promedio de contribución:")
print(ranking_contribucion[('contribucion_total', 'mean')].head())

# 5. Análisis de correlaciones con NumPy
print("\n🔢 ANÁLISIS DE CORRELACIONES:")

# Tu código aquí
# Calcular correlación entre diferentes métricas usando NumPy
correlacion_goles_asistencias = # Tu código usando np.corrcoef()
correlacion_edad_goles = # Tu código
correlacion_minutos_contribucion = # Tu código

print(f"Correlación goles-asistencias: {correlacion_goles_asistencias[0,1]:.3f}")
print(f"Correlación edad-goles: {correlacion_edad_goles[0,1]:.3f}")  
print(f"Correlación minutos-contribución: {correlacion_minutos_contribucion[0,1]:.3f}")
```

### Parte 3: Manipulación Avanzada de DataFrames (25 puntos)

**Instrucciones:**
Realiza operaciones avanzadas de manipulación de datos:

```python
print("\n" + "="*60)
print("🛠️ MANIPULACIÓN AVANZADA DE DATAFRAMES")
print("="*60)

# 1. Unir datasets (merge/join)
print("\n🔗 UNIÓN DE DATASETS:")

# Tu código aquí
# Unir información de jugadores con información de equipos
df_completo = # Tu código usando merge()

print("Dataset completo creado!")
print(f"Columnas disponibles: {list(df_completo.columns)}")

# Mostrar información combinada de algunos jugadores
print("\n👤 INFORMACIÓN COMBINADA DE JUGADORES:")
columnas_interes = ['nombre', 'equipo', 'goles', 'ciudad', 'estadio_capacidad', 'presupuesto_millones']
print(df_completo[columnas_interes].head())

# 2. Crear nuevas métricas combinadas
print("\n🧮 MÉTRICAS COMBINADAS:")

# Tu código aquí
# Calcular eficiencia por presupuesto (goles por millón de presupuesto)
df_completo['eficiencia_presupuesto'] = # Tu código

# Calcular factor de localía (goles por capacidad del estadio)
df_completo['factor_localia'] = # Tu código

# Clasificar jugadores por rendimiento
def clasificar_rendimiento(contribucion):
    """Clasifica jugadores según su contribución total"""
    if contribucion >= 20:
        return "Elite"
    elif contribucion >= 15:
        return "Muy Bueno"
    elif contribucion >= 10:
        return "Bueno"
    else:
        return "Regular"

df_completo['clasificacion'] = # Tu código aplicando la función

print("Nuevas métricas calculadas:")
print(df_completo[['nombre', 'eficiencia_presupuesto', 'factor_localia', 'clasificacion']].round(4))

# 3. Análisis por categorías
print("\n📊 ANÁLISIS POR CATEGORÍAS:")

# Tu código aquí
# Agrupar por clasificación de rendimiento
analisis_clasificacion = df_completo.groupby('clasificacion').agg({
    'nombre': 'count',  # contar jugadores
    'goles': ['mean', 'sum'],
    'asistencias': ['mean', 'sum'],
    'edad': 'mean',
    'presupuesto_millones': 'mean'
}).round(2)

print("Estadísticas por clasificación de rendimiento:")
print(analisis_clasificacion)

# 4. Crear un resumen ejecutivo
print("\n📋 RESUMEN EJECUTIVO:")

# Tu código aquí
# Calcular métricas generales usando pandas y NumPy
total_jugadores = len(df_completo)
promedio_goles = df_completo['goles'].mean()
promedio_asistencias = df_completo['asistencias'].mean()
jugador_mas_efectivo = df_completo.loc[df_completo['contribucion_total'].idxmax()]
equipo_mas_goles = df_completo.groupby('equipo')['goles'].sum().idxmax()

# Estadísticas con NumPy
edad_mediana = np.median(df_completo['edad'])
desviacion_goles = np.std(df_completo['goles'])

print(f"📈 MÉTRICAS GENERALES:")
print(f"Total de jugadores analizados: {total_jugadores}")
print(f"Promedio de goles por jugador: {promedio_goles:.2f}")
print(f"Promedio de asistencias por jugador: {promedio_asistencias:.2f}")
print(f"Mediana de edad: {edad_mediana:.0f} años")
print(f"Desviación estándar de goles: {desviacion_goles:.2f}")

print(f"\n🏆 DESTACADOS:")
print(f"Jugador más efectivo: {jugador_mas_efectivo['nombre']} ({jugador_mas_efectivo['contribucion_total']} contribuciones)")
print(f"Equipo con más goles: {equipo_mas_goles}")

# 5. Crear tabla pivot
print("\n📊 TABLA PIVOT - GOLES POR EQUIPO Y CLASIFICACIÓN:")

# Tu código aquí
tabla_pivot = # Tu código usando pd.pivot_table()

print(tabla_pivot.fillna(0))
```

### Parte 4: Análisis Estadístico Final (20 puntos)

**Instrucciones:**
Realiza un análisis estadístico comprehensivo:

```python
print("\n" + "="*60)
print("📊 ANÁLISIS ESTADÍSTICO FINAL")
print("="*60)

# 1. Estadísticas descriptivas avanzadas
print("\n📈 ESTADÍSTICAS DESCRIPTIVAS AVANZADAS:")

# Tu código aquí usando NumPy
# Calcular cuartiles, percentiles y otras métricas

metricas_goles = {
    'Media': # Tu código
    'Mediana': # Tu código  
    'Moda': # Tu código (usar scipy.stats.mode o el valor más frecuente)
    'Q1 (Percentil 25)': # Tu código
    'Q3 (Percentil 75)': # Tu código
    'Percentil 90': # Tu código
    'Rango': # Tu código (max - min)
    'Varianza': # Tu código
    'Desviación estándar': # Tu código
}

print("📊 Estadísticas de GOLES:")
for metrica, valor in metricas_goles.items():
    print(f"{metrica:20}: {valor:.2f}")

# 2. Análisis de outliers
print("\n🔍 ANÁLISIS DE OUTLIERS:")

# Tu código aquí
# Identificar outliers usando el método IQR
Q1_goles = np.percentile(df_completo['goles'], 25)
Q3_goles = np.percentile(df_completo['goles'], 75)
IQR_goles = Q3_goles - Q1_goles
limite_inferior = Q1_goles - 1.5 * IQR_goles
limite_superior = Q3_goles + 1.5 * IQR_goles

outliers = df_completo[(df_completo['goles'] < limite_inferior) | 
                      (df_completo['goles'] > limite_superior)]

print(f"Límite inferior para goles: {limite_inferior:.2f}")
print(f"Límite superior para goles: {limite_superior:.2f}")
print(f"Jugadores outliers encontrados: {len(outliers)}")

if len(outliers) > 0:
    print("Jugadores outliers:")
    print(outliers[['nombre', 'equipo', 'goles', 'asistencias']])

# 3. Comparación entre grupos
print("\n⚖️ COMPARACIÓN ENTRE GRUPOS:")

# Tu código aquí
# Comparar jugadores de equipos ricos vs equipos con menos presupuesto
equipos_ricos_lista = equipos_ricos['equipo'].tolist()

jugadores_equipos_ricos = df_completo[df_completo['equipo'].isin(equipos_ricos_lista)]
jugadores_equipos_pobres = df_completo[~df_completo['equipo'].isin(equipos_ricos_lista)]

print("Comparación equipos ricos vs equipos con menor presupuesto:")
print(f"\n💰 EQUIPOS RICOS (n={len(jugadores_equipos_ricos)}):")
print(f"Promedio goles: {jugadores_equipos_ricos['goles'].mean():.2f}")
print(f"Promedio asistencias: {jugadores_equipos_ricos['asistencias'].mean():.2f}")
print(f"Promedio contribución: {jugadores_equipos_ricos['contribucion_total'].mean():.2f}")

print(f"\n💸 EQUIPOS MENOR PRESUPUESTO (n={len(jugadores_equipos_pobres)}):")
print(f"Promedio goles: {jugadores_equipos_pobres['goles'].mean():.2f}")
print(f"Promedio asistencias: {jugadores_equipos_pobres['asistencias'].mean():.2f}")
print(f"Promedio contribución: {jugadores_equipos_pobres['contribucion_total'].mean():.2f}")

# 4. Crear reporte final
print("\n" + "="*60)
print("📋 REPORTE FINAL DE ANÁLISIS")
print("="*60)

# Tu código aquí
# Reporte ejecutivo con los hallazgos más importantes

print(f"\n🎯 HALLAZGOS PRINCIPALES:")

# Top 3 jugadores por contribución total
top_3_jugadores = df_completo.nlargest(3, 'contribucion_total')
print(f"\n🏆 TOP 3 JUGADORES POR CONTRIBUCIÓN:")
for i, (_, jugador) in enumerate(top_3_jugadores.iterrows(), 1):
    print(f"{i}. {jugador['nombre']} ({jugador['equipo']}): {jugador['contribucion_total']} contribuciones")

# Equipo más eficiente por presupuesto
eficiencia_por_equipo = df_completo.groupby('equipo')['eficiencia_presupuesto'].mean().sort_values(ascending=False)
print(f"\n💡 EQUIPO MÁS EFICIENTE POR PRESUPUESTO:")
print(f"{eficiencia_por_equipo.index[0]}: {eficiencia_por_equipo.iloc[0]:.4f} goles/millón")

# Distribución por clasificación
distribucion_clasificacion = df_completo['clasificacion'].value_counts()
print(f"\n📊 DISTRIBUCIÓN DE JUGADORES POR CLASIFICACIÓN:")
for clasificacion, cantidad in distribucion_clasificacion.items():
    porcentaje = (cantidad / total_jugadores) * 100
    print(f"{clasificacion}: {cantidad} jugadores ({porcentaje:.1f}%)")

print(f"\n🔍 CONCLUSIONES:")
print(f"- El análisis incluyó {total_jugadores} jugadores de {df_completo['equipo'].nunique()} equipos")
print(f"- La correlación goles-asistencias es {correlacion_goles_asistencias[0,1]:.3f}")
print(f"- {len(outliers)} jugadores fueron identificados como outliers en goles")
print(f"- Los equipos con mayor presupuesto tienen un promedio de {jugadores_equipos_ricos['contribucion_total'].mean():.1f} contribuciones")

print(f"\n{'='*60}")
print("✅ ANÁLISIS COMPLETADO EXITOSAMENTE")
print(f"{'='*60}")
```

## 📤 Instrucciones de Entrega

1. **Formato:** Archivo `.py` o notebook `.ipynb`
2. **Nombre del archivo:** `apellido_nombre_ejercicio_semana04.py`
3. **Contenido mínimo:**
   - Todo el código ejecutado sin errores
   - Comentarios explicando cada análisis
   - Salida completa de todos los análisis
   - DataFrames mostrados correctamente

4. **Documentación adicional:**
   - Lista de 3 insights más importantes encontrados en los datos
   - Explicación de qué análisis fue más útil y por qué
   - Reflexión sobre las diferencias entre pandas y NumPy

## 🏆 Criterios de Evaluación

### Correctitud Técnica (40 puntos)

- **Excelente (36-40):** Código ejecuta sin errores, uso correcto de pandas y NumPy
- **Competente (28-35):** Errores menores, uso mayormente correcto de las librerías
- **En desarrollo (20-27):** Algunos errores, uso básico de pandas/NumPy
- **Insuficiente (0-19):** Múltiples errores, uso incorrecto de las librerías

### Aplicación Práctica (30 puntos)

- **Excelente (27-30):** Análisis completos, insights relevantes, uso avanzado de funciones
- **Competente (21-26):** Análisis apropiados, algunos insights útiles
- **En desarrollo (15-20):** Análisis básicos, insights limitados
- **Insuficiente (0-14):** Análisis incompletos o incorrectos

### Claridad y Documentación (30 puntos)

- **Excelente (27-30):** Código muy bien comentado, resultados bien presentados
- **Competente (21-26):** Buena documentación, presentación clara
- **En desarrollo (15-20):** Documentación básica, presentación simple
- **Insuficiente (0-14):** Poca documentación, presentación confusa

## 💡 Consejos para el Éxito

1. **Explora primero:** Usa `.head()`, `.info()`, `.describe()` antes de analizar
2. **Verifica tipos:** Asegúrate de que las columnas tengan el tipo correcto
3. **Maneja valores faltantes:** Revisa si hay NaN con `.isna().sum()`
4. **Usa métodos encadenados:** Combina operaciones de pandas eficientemente
5. **Interpreta resultados:** No solo calcules, explica qué significan los números

## 🔗 Recursos Adicionales

- [Documentación de pandas](https://pandas.pydata.org/docs/)
- [Documentación de NumPy](https://numpy.org/doc/)
- [Tutorial de pandas](https://pandas.pydata.org/docs/user_guide/10min.html)
- [Guía de NumPy](https://numpy.org/doc/stable/user/quickstart.html)

---

*¿Preguntas? Contacta a tu instructor durante las horas de oficina o en el foro del curso.*
