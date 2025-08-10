---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.17.2
  kernelspec:
    display_name: .venv
    language: python
    name: python3
---

# Semana 7: ¿Todos los datos del fútbol hablan el mismo idioma?

## ¿Alguna vez te has preguntado por qué los analistas deportivos distinguen entre diferentes tipos de información?

**Reflexión inicial**: Cuando miras las estadísticas de tu jugador favorito, ves números como goles (3), texto como posición (delantero), y fechas como edad (23 años). ¿Crees que Python "entiende" que estos datos son fundamentalmente diferentes?

### Pregunta motivadora para la semana:
Si fueras analista del Real Madrid, ¿tratarías igual la información "Manchester City anotó 3 goles" que "el partido fue en enero"?

---

## ESTRUCTURA SEMANAL: 3 Sesiones de Descubrimiento

### SESIÓN 1: ¿Por qué importan los tipos de datos? (50 min)
**Pregunta guía**: ¿Cómo distinguir entre diferentes "idiomas" de información deportiva?
- ¿Qué diferencia un número de una palabra en análisis deportivo?
- ¿Por qué Python necesita "entender" el tipo de cada dato?
- ¿Cómo preparamos datos para análisis específicos?

### SESIÓN 2: ¿Qué revela cada tipo de dato? (50 min)  
**Pregunta guía**: ¿Cómo cada tipo de información cuenta una historia diferente?
- ¿Qué patrones emergen de datos numéricos vs categóricos?
- ¿Cómo las fechas y tiempos transforman nuestro análisis?
- ¿Qué secretos esconden las posiciones geográficas?

### SESIÓN 3: ¿Cómo combinar diferentes tipos sabiamente? (50 min)
**Pregunta guía**: ¿Cuándo y cómo mezclar diferentes tipos de datos?
- ¿Qué análisis requieren múltiples tipos de información?
- ¿Cómo evitar errores al combinar datos diversos?
- ¿Qué nuevos insights emergen de la integración inteligente?

---

## ¿Por qué entender tipos de datos en el fútbol?

**Pregunta reflexiva**: ¿Has notado que algunos análisis deportivos son más profundos que otros? ¿Será porque usan diferentes tipos de datos de manera más inteligente?

### La evolución del análisis deportivo moderno:
- **¿Sabías que...?** Los scouts modernos manejan más de 15 tipos diferentes de datos por partido
- **¿Te imaginas que...?** Un solo gol genera datos numéricos, categóricos, temporales y espaciales simultáneamente
- **¿Has considerado que...?** La precisión de las predicciones depende de entender qué tipo de dato usar en cada situación

**Tu misión esta semana**: Convertirte en un "traductor" experto entre diferentes idiomas de datos deportivos.

¿Estás listo para descubrir cómo cada tipo de dato cuenta una historia única del fútbol?


# SESIÓN 1: ¿Por qué importan los tipos de datos? (50 minutos)

## Pregunta de apertura: ¿Qué tienen en común un bibliotecario y un analista de datos?

**Reflexiona antes de continuar**: Ambos organizan información de manera que sea fácil encontrar y usar. ¿Pero qué pasa si ponen novelas en la sección de matemáticas?

---

## Momento de curiosidad: ¿Por qué Python se "confunde" con algunos datos?

Imagina que le dices a Python: "Suma el nombre de Messi con la edad de Cristiano". ¿Crees que Python sabría qué hacer?

**Pregunta reflexiva**: ¿Qué información necesita Python para saber si debe sumar, contar, ordenar o buscar patrones en nuestros datos?

### ¿Qué diferencia un "3" de un "delantero" para una computadora?

Antes de analizar, necesitamos entender que Python ve diferencias que nosotros damos por hechas. ¿Has notado que tratas diferente el número de goles (puedes sumarlo) que el nombre del equipo (no puedes sumarlo)?


## ¿Cómo exploramos los diferentes "idiomas" de datos en el fútbol?

**Momento de reflexión**: En el mundo real, un partido genera información numérica (goles, minutos), textual (nombres, posiciones), fechas (cuándo se jugó), y más. ¿Pero cómo sabemos qué tipo de análisis hacer con cada uno?

**Pregunta clave**: Si tuvieras que explicarle a Python la diferencia entre "3 goles" y "3 de marzo", ¿cómo lo harías?

### ¡Vamos a ser "detectives de tipos de datos"!

Antes de analizar fútbol, necesitamos entender qué herramientas son mejores para cada tipo de información. ¿Has notado que usas diferentes métodos para organizar números que para organizar nombres?

```python
# ¿Te has preguntado qué herramientas necesita un analista para manejar datos diversos?
# Vamos a preparar nuestro "laboratorio" de tipos de datos paso a paso

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

# ¿Por qué necesitamos tantas herramientas diferentes?
# pandas -> ¿Para qué crees que sirve cuando tenemos datos mixtos? (números + texto + fechas)
# numpy -> ¿Qué ventajas tiene para generar datos realistas de diferentes tipos?
# matplotlib -> ¿Cómo visualizamos datos que no son solo números?
# seaborn -> ¿Qué hace especial para mostrar diferencias entre tipos de datos?
# datetime -> ¿Por qué Python necesita herramientas especiales para fechas?

# Configuración visual profesional
sns.set_theme(style="whitegrid", palette="viridis")
plt.rcParams['figure.figsize'] = (12, 6)

print("¡Laboratorio de tipos de datos listo!")
print("¿Te has preguntado alguna vez cómo los analistas del Barcelona manejan tantos tipos de información diferentes?")
print("¡Exactamente con las mismas herramientas que acabamos de cargar!")
print()
print("Pregunta de reflexión: ¿Por qué crees que necesitamos herramientas especializadas para diferentes tipos de datos?")
```

## ¿Cómo creamos nuestro "universo futbolístico" de práctica?

**Momento de reflexión**: En el mundo real, los datos vienen de diferentes ligas, equipos y temporadas. ¿Pero cómo podríamos simular esta diversidad para practicar con diferentes tipos de datos?

**Pregunta clave**: Si tuvieras que elegir ligas y equipos para representar el fútbol europeo, ¿cuáles serían los más reconocibles para estudiantes mexicanos?

### ¡Vamos a ser "arquitectos" de datos futbolísticos!

```python
# ¿Te has preguntado cómo los analistas organizan el universo futbolístico?
# Vamos a crear nuestra estructura básica paso a paso

# ¿Por qué es importante que nuestros datos sean reproducibles?
np.random.seed(42)

# ¿Qué equipos europeos reconoces inmediatamente?
# Reflexiona: ¿Por qué elegimos estas ligas y equipos específicos?
ligas_europeas = ['La Liga', 'Premier League', 'Serie A']
temporadas_recientes = ['2022-23', '2023-24']

# ¿Cómo se organiza jerárquicamente el fútbol europeo?
equipos_por_liga = {
    'La Liga': ['Barcelona', 'Real Madrid', 'Atletico Madrid', 'Sevilla'],
    'Premier League': ['Manchester City', 'Liverpool', 'Chelsea', 'Arsenal'],
    'Serie A': ['Juventus', 'Inter Milan', 'AC Milan', 'Napoli']
}

print("Estructura de nuestro universo futbolístico:")
for liga in ligas_europeas:
    print(f"{liga}: {len(equipos_por_liga[liga])} equipos élite")

print(f"\nTemporadas a analizar: {len(temporadas_recientes)}")
print(f"Total de equipos: {sum(len(equipos) for equipos in equipos_por_liga.values())}")

print("\nPregunta de reflexión: ¿Esta estructura representa bien la diversidad del fútbol europeo?")
print("¿Qué otros tipos de información serían importantes incluir?")
```

# ¿Qué tipos de datos podemos identificar en el fútbol?

## Pregunta de clasificación: ¿Todos los datos deportivos son iguales?

**Reflexiona**: Cuando escuchas "Barcelona 3-1 Real Madrid", ¿qué tipos diferentes de información identifies? ¿Los nombres de equipos son igual de importantes que los números de goles?

**Momento de descubrimiento**: Vamos a explorar cómo Python "entiende" diferentes tipos de información futbolística.

### TIPO 1: Datos Numéricos - ¿Los números que podemos sumar?

**Pregunta fundamental**: ¿Qué información del fútbol son números puros que podemos calcular matemáticamente?

**Ejemplos en el fútbol**:
- ¿Goles anotados, minutos jugados, edad de jugadores?
- ¿Puedes sumar goles de diferentes partidos?
- ¿Tiene sentido calcular el promedio de edad de un equipo?

**Pregunta analítica**: ¿Qué tipo de análisis puedes hacer SOLO con números?

```python
# ¿Te has preguntado cómo crear datos que representen diferentes tipos de información?
# Vamos a construir un ejemplo que incluya números, texto, fechas y más

print("CREANDO DATOS MIXTOS DE FÚTBOL")
print("="*50)

# ¿Cómo representamos información numérica en fútbol?
print("Datos NUMÉRICOS - ¿Qué podemos calcular matemáticamente?")

datos_numericos = []
for liga in ligas_europeas:
    equipos = equipos_por_liga[liga]
    for temporada in temporadas_recientes:
        # ¿Por qué simulamos 8 partidos por liga-temporada?
        for i in range(8):
            equipo_local = np.random.choice(equipos)
            # ¿Por qué un equipo no puede jugar contra sí mismo?
            equipo_visitante = np.random.choice([e for e in equipos if e != equipo_local])
            
            # ¿Qué hace realistas estos rangos de goles?
            goles_local = np.random.randint(0, 5)      # 0 a 4 goles
            goles_visitante = np.random.randint(0, 4)  # Ligera ventaja local
            
            # ¿Cómo generamos fechas realistas?
            mes = np.random.randint(8, 13)  # Temporada agosto-diciembre
            dia = np.random.randint(1, 29)
            fecha = f"2023-{mes:02d}-{dia:02d}"
            
            partido = {
                'fecha': fecha,
                'liga': liga,
                'temporada': temporada,
                'equipo_local': equipo_local,
                'equipo_visitante': equipo_visitante,
                'goles_local': goles_local,
                'goles_visitante': goles_visitante,
                'total_goles': goles_local + goles_visitante  # ¿Por qué agregamos esto?
            }
            datos_numericos.append(partido)

# ¿Qué ventajas tiene convertir listas en DataFrames?
df_partidos = pd.DataFrame(datos_numericos)

print(f"Partidos simulados: {len(df_partidos)}")
print("\nPrimeros 5 partidos de nuestro dataset:")
print(df_partidos.head())

print("\nPregunta de análisis: ¿Qué tipos de datos diferentes identificas en esta tabla?")
print("¿Cuáles son números puros y cuáles son texto?")
print("¿Qué operaciones matemáticas podrías hacer con cada columna?")
```

## ¿Cómo identificamos los tipos de datos en nuestro ejemplo?

**Momento de análisis**: Ahora que tenemos datos reales, vamos a clasificarlos. ¿Puedes identificar qué columnas son diferentes tipos de información?

**Pregunta investigativa**: ¿Cómo sabe Python automáticamente qué tipo de operaciones puede hacer con cada columna?

### TIPO 2: Datos Categóricos - ¿Las etiquetas que agrupan?

**Pregunta de clasificación**: ¿Qué información del fútbol son categorías o grupos que no podemos sumar?

**Ejemplos en el fútbol**:
- ¿Nombres de equipos, posiciones de jugadores, nombres de ligas?
- ¿Puedes "sumar" Barcelona + Real Madrid?
- ¿Tiene sentido calcular el promedio de "Delantero" + "Portero"?

**Pregunta analítica**: ¿Qué tipo de análisis requieren datos categóricos vs numéricos?

```python
# ¿Te has preguntado cómo Python "reconoce" automáticamente los tipos de datos?
# Vamos a investigar qué tipos detecta en nuestro dataset

print("INVESTIGANDO TIPOS DE DATOS EN PYTHON")
print("="*50)

# ¿Qué información nos da Python sobre nuestros datos?
print("Tipos de datos detectados automáticamente:")
print(df_partidos.dtypes)

print("\n" + "="*50)
print("ANALIZANDO CADA TIPO")
print("="*50)

# ¿Cuáles son DATOS NUMÉRICOS (podemos calcular)?
columnas_numericas = df_partidos.select_dtypes(include=[np.number]).columns
print(f"Columnas NUMÉRICAS (podemos sumar/promediar): {list(columnas_numericas)}")

# ¿Qué estadísticas podemos calcular con números?
print("\nEstadísticas de goles (datos numéricos):")
print(f"  Promedio goles locales: {df_partidos['goles_local'].mean():.2f}")
print(f"  Total de goles en todos los partidos: {df_partidos['total_goles'].sum()}")
print(f"  Máximo goles en un partido: {df_partidos['total_goles'].max()}")

print("\n" + "-"*50)

# ¿Cuáles son DATOS CATEGÓRICOS (etiquetas/grupos)?
columnas_categoricas = df_partidos.select_dtypes(include=['object']).columns
print(f"Columnas CATEGÓRICAS (nombres/etiquetas): {list(columnas_categoricas)}")

# ¿Qué operaciones hacemos con categorías?
print("\nOperaciones con datos categóricos:")
print("  Equipos únicos que jugaron como locales:")
equipos_unicos = df_partidos['equipo_local'].unique()
print(f"    {list(equipos_unicos)}")

print(f"  Número de ligas diferentes: {df_partidos['liga'].nunique()}")
print("  Frecuencia por liga:")
print(df_partidos['liga'].value_counts())

print("\nPregunta de reflexión: ¿Por qué no podemos 'sumar' nombres de equipos?")
print("¿Qué operaciones SÍ tienen sentido con datos categóricos?")
```

---

## SÍNTESIS DE LA SESIÓN 1: ¿Qué hemos descubierto sobre tipos de datos?

**Reflexión de 50 minutos**:
- ¿Cómo Python distingue automáticamente entre números y texto?
- ¿Qué operaciones son posibles con cada tipo de dato?
- ¿Por qué es importante entender estas diferencias para análisis deportivo?

**Pregunta preparatoria**: ¿Estás listo para explorar tipos de datos más complejos como fechas y ubicaciones?

---

# SESIÓN 2: ¿Qué revela cada tipo de dato? (50 minutos)

## Pregunta de apertura: ¿Cómo el "cuándo" y el "dónde" transforman el análisis deportivo?

**Reflexiona**: Has trabajado con números y texto, pero ¿qué pasa cuando necesitas analizar CUÁNDO ocurrió algo o DÓNDE en el campo sucedió una jugada?

**Desafío mental**: Si quisieras analizar la evolución del rendimiento de un equipo a lo largo de una temporada, ¿qué tipo de datos necesitarías que aún no hemos explorado?

---

## ¿Qué secretos revelan las fechas y ubicaciones en el fútbol?

**Momento de curiosidad**: Cada evento deportivo tiene una dimensión temporal y espacial. ¿Será que Python necesita herramientas especiales para entender "cuándo" y "dónde"?

```python
# ¿Te has preguntado por qué las fechas son tan importantes en el análisis deportivo?
# Vamos a explorar DATOS TEMPORALES en el fútbol

print("EXPLORANDO DATOS TEMPORALES EN FÚTBOL")
print("="*50)

# ¿Cómo Python entiende las fechas?
print("Convirtiendo fechas de texto a formato temporal:")
print("Antes:", df_partidos['fecha'].dtype)

# ¿Qué ventajas tiene convertir fechas a formato datetime?
df_partidos['fecha'] = pd.to_datetime(df_partidos['fecha'])
print("Después:", df_partidos['fecha'].dtype)

print("\nAhora podemos hacer análisis temporales:")

# ¿Qué nuevas operaciones podemos hacer con fechas?
df_partidos['mes'] = df_partidos['fecha'].dt.month
df_partidos['dia_semana'] = df_partidos['fecha'].dt.day_name()

print("Primeros 5 partidos con información temporal:")
print(df_partidos[['fecha', 'mes', 'dia_semana', 'equipo_local', 'equipo_visitante', 'total_goles']].head())

print("\n" + "="*50)
print("ANÁLISIS TEMPORAL - ¿Qué patrones emergen?")
print("="*50)

# ¿En qué meses se anotan más goles?
goles_por_mes = df_partidos.groupby('mes')['total_goles'].mean()
print("Promedio de goles por mes:")
for mes, promedio in goles_por_mes.items():
    nombre_mes = ['', 'Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 
                  'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'][mes]
    print(f"  {nombre_mes}: {promedio:.2f} goles promedio")

# ¿Hay diferencias en el rendimiento local vs visitante por mes?
print(f"\nMes con más goles promedio: {goles_por_mes.idxmax()}")
print(f"Mes con menos goles promedio: {goles_por_mes.idxmin()}")

print("\nPregunta de reflexión: ¿Por qué crees que hay diferencias entre meses?")
print("¿Qué análisis temporales serían útiles para un entrenador?")
```

## ¿Cómo creamos visualizaciones específicas para cada tipo de dato?

**Momento de descubrimiento**: Ahora que entendemos fechas, vamos a ver cómo las visualizaciones cambian según el tipo de datos que estemos analizando.

**Pregunta visual**: ¿Crees que un gráfico de barras funciona igual para mostrar goles (números) que para mostrar equipos (categorías)?

### TIPO 3: Datos Booleanos - ¿Verdadero o falso en el fútbol?

**Pregunta de clasificación**: ¿Qué información del fútbol se puede expresar como "sí/no" o "verdadero/falso"?

**Ejemplos en el fútbol**:
- ¿Gol anotado (sí/no), tarjeta recibida (sí/no), partido ganado (sí/no)?
- ¿Cómo analizamos datos que solo tienen dos opciones?
- ¿Qué porcentajes podemos calcular con datos booleanos?

```python
# ¿Te has preguntado cómo representar información de "sí/no" en el análisis deportivo?
# Vamos a crear DATOS BOOLEANOS y ver cómo se analizan

print("EXPLORANDO DATOS BOOLEANOS EN FÚTBOL")
print("="*50)

# ¿Qué información de fútbol puede ser verdadero/falso?
# Vamos a agregar datos booleanos a nuestro dataset existente

# ¿Cómo determinamos si un partido fue "goleada"?
df_partidos['goleada'] = df_partidos['total_goles'] >= 4  # 4+ goles = goleada

# ¿Cómo sabemos si el equipo local ganó?
df_partidos['victoria_local'] = df_partidos['goles_local'] > df_partidos['goles_visitante']

# ¿Qué partidos fueron empates?
df_partidos['empate'] = df_partidos['goles_local'] == df_partidos['goles_visitante']

# ¿Qué partidos fueron en "temporada alta"? (meses 10-12)
df_partidos['temporada_alta'] = df_partidos['mes'] >= 10

print("Nuevas columnas booleanas agregadas:")
print("Primeros 5 partidos con datos booleanos:")
columnas_mostrar = ['equipo_local', 'equipo_visitante', 'total_goles', 'goleada', 
                   'victoria_local', 'empate', 'temporada_alta']
print(df_partidos[columnas_mostrar].head())

print("\n" + "="*50)
print("ANÁLISIS CON DATOS BOOLEANOS")
print("="*50)

# ¿Qué porcentajes podemos calcular?
print("Estadísticas de eventos verdadero/falso:")
print(f"  Porcentaje de goleadas: {df_partidos['goleada'].mean()*100:.1f}%")
print(f"  Porcentaje de victorias locales: {df_partidos['victoria_local'].mean()*100:.1f}%")
print(f"  Porcentaje de empates: {df_partidos['empate'].mean()*100:.1f}%")
print(f"  Porcentaje en temporada alta: {df_partidos['temporada_alta'].mean()*100:.1f}%")

# ¿Hay diferencias entre ligas?
print("\nComparación por liga:")
comparacion_ligas = df_partidos.groupby('liga')[['goleada', 'victoria_local', 'empate']].mean()
print(comparacion_ligas)

print("\nPregunta de reflexión: ¿Por qué los datos booleanos son útiles para porcentajes?")
print("¿Qué otros datos verdadero/falso serían interesantes en fútbol?")
```

---

## SÍNTESIS DE LA SESIÓN 2: ¿Qué hemos revelado sobre tipos especializados?

**Reflexión de 50 minutos**:
- ¿Cómo las fechas nos permiten analizar tendencias temporales?
- ¿Qué ventajas tienen los datos booleanos para calcular porcentajes?
- ¿Por qué cada tipo de dato requiere diferentes técnicas de análisis?

**Pregunta preparatoria**: ¿Estás listo para combinar todos los tipos de datos en análisis más complejos?

---

# SESIÓN 3: ¿Cómo combinar diferentes tipos sabiamente? (50 minutos)

## Pregunta de apertura: ¿Qué pasa cuando mezclamos todos los "idiomas" de datos?

**Reflexiona**: Has aprendido a trabajar con números, texto, fechas y verdadero/falso por separado. ¿Pero qué análisis poderosos emergen cuando los combinas inteligentemente?

**Desafío integrador**: Si fueras a crear el análisis más completo posible de un equipo, ¿cómo combinarías todos estos tipos de datos para contar una historia única?

---

## ¿Qué análisis sofisticados emergen de la integración inteligente?

**Momento de síntesis**: Los analistas profesionales no usan un solo tipo de dato. La magia sucede cuando combines números + categorías + fechas + booleanos de manera estratégica.

```python
# ¿Te has preguntado cómo crear un análisis que use TODOS los tipos de datos juntos?
# Vamos a construir un análisis integrador que combine todo lo aprendido

print("ANÁLISIS INTEGRADOR: COMBINANDO TODOS LOS TIPOS DE DATOS")
print("="*60)

# ¿Cómo podemos crear un análisis temporal que combine números y categorías?
print("Análisis 1: Rendimiento por liga a lo largo del tiempo")

# Agrupamos por liga y mes (categórico + temporal + numérico)
rendimiento_temporal = df_partidos.groupby(['liga', 'mes']).agg({
    'total_goles': 'mean',          # Numérico: promedio
    'goleada': 'mean',              # Booleano: porcentaje
    'victoria_local': 'mean',       # Booleano: porcentaje
    'goles_local': 'mean'           # Numérico: promedio
}).round(2)

print("Rendimiento promedio por liga y mes:")
print(rendimiento_temporal)

print("\n" + "="*60)
print("Análisis 2: ¿Qué liga tiene más variabilidad?")
print("="*60)

# ¿Cómo comparamos la consistencia entre categorías?
variabilidad_por_liga = df_partidos.groupby('liga')['total_goles'].agg(['mean', 'std', 'min', 'max'])
variabilidad_por_liga['rango'] = variabilidad_por_liga['max'] - variabilidad_por_liga['min']

print("Estadísticas de variabilidad por liga:")
print(variabilidad_por_liga)

# ¿Qué liga es más predecible?
liga_mas_consistente = variabilidad_por_liga['std'].idxmin()
print(f"\nLiga más consistente (menor variabilidad): {liga_mas_consistente}")
print(f"Desviación estándar: {variabilidad_por_liga.loc[liga_mas_consistente, 'std']:.2f}")

print("\n" + "="*60)
print("Análisis 3: Visualización integradora")
print("="*60)

# ¿Cómo visualizamos múltiples tipos de datos simultáneamente?
fig, axes = plt.subplots(2, 2, figsize=(15, 10))
fig.suptitle('ANÁLISIS INTEGRADOR: Todos los Tipos de Datos', fontsize=16, fontweight='bold')

# Gráfico 1: Numérico por Categórico
axes[0, 0].boxplot([df_partidos[df_partidos['liga'] == liga]['total_goles'] 
                    for liga in ligas_europeas], labels=ligas_europeas)
axes[0, 0].set_title('Distribución de Goles por Liga\n(Numérico + Categórico)')
axes[0, 0].set_ylabel('Total de Goles')

# Gráfico 2: Temporal + Numérico
goles_por_mes_global = df_partidos.groupby('mes')['total_goles'].mean()
axes[0, 1].plot(goles_por_mes_global.index, goles_por_mes_global.values, marker='o')
axes[0, 1].set_title('Tendencia Temporal de Goles\n(Temporal + Numérico)')
axes[0, 1].set_xlabel('Mes')
axes[0, 1].set_ylabel('Promedio de Goles')

# Gráfico 3: Booleano por Categórico
porcentajes_por_liga = df_partidos.groupby('liga')[['goleada', 'victoria_local', 'empate']].mean() * 100
porcentajes_por_liga.plot(kind='bar', ax=axes[1, 0], width=0.8)
axes[1, 0].set_title('Porcentajes por Liga\n(Booleano + Categórico)')
axes[1, 0].set_ylabel('Porcentaje (%)')
axes[1, 0].legend(['Goleadas', 'Victorias Locales', 'Empates'])
axes[1, 0].tick_params(axis='x', rotation=45)

# Gráfico 4: Todos los tipos combinados
for liga in ligas_europeas:
    data_liga = df_partidos[df_partidos['liga'] == liga]
    x = data_liga['mes']
    y = data_liga['total_goles']
    axes[1, 1].scatter(x, y, label=liga, alpha=0.6, s=50)

axes[1, 1].set_title('Goles por Mes y Liga\n(Temporal + Numérico + Categórico)')
axes[1, 1].set_xlabel('Mes')
axes[1, 1].set_ylabel('Total de Goles')
axes[1, 1].legend()

plt.tight_layout()
plt.show()

print("Pregunta de reflexión: ¿Qué insights emergen cuando combinas todos los tipos de datos?")
print("¿Qué análisis NO serían posibles sin entender los diferentes tipos?")
```

## ¿Qué análisis avanzados emergen de la combinación inteligente?

**Momento de aplicación**: Ahora que dominas todos los tipos de datos, vamos a crear un análisis que sería imposible sin esta comprensión profunda.

**Pregunta estratégica**: ¿Cómo usarían esta información los analistas del Real Madrid para tomar decisiones tácticas?

### Actividad Práctica: Tu primer análisis profesional

**Objetivo**: Usar todos los tipos de datos para responder una pregunta específica de fútbol.

#### Pregunta de investigación: ¿Qué liga europea es más competitiva?

**Paso 1: ¿Cómo definiríamos "competitividad"?**
- Reflexiona: ¿Es la variabilidad de resultados, el equilibrio entre equipos, o la frecuencia de sorpresas?
- ¿Qué métricas de cada tipo de dato podrían ayudarnos?

**Paso 2: Analicemos con todos nuestros tipos de datos**
- Numéricos: Promedios y variabilidad de goles
- Categóricos: Distribución entre ligas
- Temporales: Consistencia a lo largo del tiempo
- Booleanos: Porcentajes de empates y goleadas

**Paso 3: ¿Qué descubrimos?**
- ¿Una liga tiene más empates (más equilibrio)?
- ¿Una liga tiene mayor variabilidad en goles (más imprevisible)?
- ¿Los patrones temporales revelan diferencias estacionales?

#### Reflexión final
- ¿Qué tipo de dato fue más revelador?
- ¿Qué análisis NO podrías hacer sin entender los tipos de datos?
- ¿Cómo cambió tu perspectiva sobre el análisis deportivo?

```python
# ¿Te has preguntado cómo los analistas profesionales responden preguntas complejas?
# Vamos a aplicar todo lo aprendido para resolver: "¿Qué liga es más competitiva?"

print("INVESTIGACIÓN FINAL: ¿QUÉ LIGA ES MÁS COMPETITIVA?")
print("="*60)

# ¿Cómo medimos competitividad usando todos los tipos de datos?
print("Definiendo competitividad con múltiples métricas:")

competitividad_analysis = {}

for liga in ligas_europeas:
    data_liga = df_partidos[df_partidos['liga'] == liga]
    
    # Métricas de competitividad
    competitividad_analysis[liga] = {
        # Numérico: ¿Poca variabilidad = más equilibrio?
        'variabilidad_goles': data_liga['total_goles'].std(),
        
        # Booleano: ¿Más empates = más equilibrio?
        'porcentaje_empates': data_liga['empate'].mean() * 100,
        
        # Booleano: ¿Menos goleadas = más competitividad?
        'porcentaje_goleadas': data_liga['goleada'].mean() * 100,
        
        # Booleano: ¿Equilibrio local-visitante?
        'ventaja_local': data_liga['victoria_local'].mean() * 100,
        
        # Temporal: ¿Consistencia a lo largo del tiempo?
        'consistencia_temporal': data_liga.groupby('mes')['total_goles'].mean().std()
    }

# ¿Qué revelan nuestros datos?
print("\nMétricas de competitividad por liga:")
print("-" * 50)

for liga, metricas in competitividad_analysis.items():
    print(f"\n{liga}:")
    print(f"  Variabilidad de goles: {metricas['variabilidad_goles']:.2f}")
    print(f"  Porcentaje de empates: {metricas['porcentaje_empates']:.1f}%")
    print(f"  Porcentaje de goleadas: {metricas['porcentaje_goleadas']:.1f}%")
    print(f"  Ventaja local: {metricas['ventaja_local']:.1f}%")
    print(f"  Consistencia temporal: {metricas['consistencia_temporal']:.2f}")

print("\n" + "="*60)
print("CONCLUSIONES INTEGRALES")
print("="*60)

# ¿Qué liga destaca en cada métrica?
liga_menos_goleadas = min(competitividad_analysis.keys(), 
                         key=lambda x: competitividad_analysis[x]['porcentaje_goleadas'])
liga_mas_empates = max(competitividad_analysis.keys(), 
                      key=lambda x: competitividad_analysis[x]['porcentaje_empates'])
liga_menos_variabilidad = min(competitividad_analysis.keys(), 
                             key=lambda x: competitividad_analysis[x]['variabilidad_goles'])

print(f"Liga con menos goleadas (más equilibrio): {liga_menos_goleadas}")
print(f"Liga con más empates (más equilibrio): {liga_mas_empates}")
print(f"Liga con menos variabilidad (más predecible): {liga_menos_variabilidad}")

print("\nTu análisis profesional está completo!")
print("Has usado datos numéricos, categóricos, temporales y booleanos para resolver una pregunta compleja.")

print("\nPREGUNTAS DE REFLEXIÓN FINAL:")
print("1. ¿Qué tipo de dato fue más revelador para medir competitividad?")
print("2. ¿Podrías haber hecho este análisis sin entender los tipos de datos?")
print("3. ¿Qué otras preguntas futbolísticas podrías responder ahora?")
print("4. ¿Cómo usaría un entrenador esta información?")
print("5. ¿Qué limitaciones tiene nuestro análisis con datos simulados?")
```

---

# SÍNTESIS FINAL: ¿Qué hemos descubierto sobre los idiomas de datos?

## Reflexión de las 3 sesiones (150 minutos totales)

### SESIÓN 1: ¿Por qué importan los tipos de datos?
**Lo que dominamos ahora**:
- Distinguir entre datos numéricos, categóricos, temporales y booleanos
- Entender qué operaciones son posibles con cada tipo
- Reconocer automáticamente los tipos que detecta Python
- Saber cuándo usar cada tipo de análisis

### SESIÓN 2: ¿Qué revela cada tipo de dato?
**Lo que revelamos**:
- Cómo las fechas permiten análisis temporales sofisticados
- Por qué los datos booleanos son perfectos para porcentajes
- Qué visualizaciones funcionan mejor para cada tipo
- Cómo cada tipo cuenta una historia diferente del fútbol

### SESIÓN 3: ¿Cómo combinar diferentes tipos sabiamente?
**Lo que integramos**:
- Análisis multidimensionales que combinan todos los tipos
- Estrategias para responder preguntas complejas
- Visualizaciones que muestran múltiples tipos simultáneamente
- Metodologías de análisis profesional en deportes

---

## Pregunta de preparación para la próxima semana:

**¿Te has dado cuenta de que ahora "hablas" todos los idiomas de datos que usan los analistas profesionales?**

### ¿Qué nuevos análisis quieres crear ahora?

**Reflexión personal**: 
- ¿Cuál tipo de dato te resultó más sorprendente?
- ¿Qué análisis te gustaría hacer con datos reales?
- ¿Cómo cambió tu comprensión sobre la complejidad del análisis deportivo?

### Vista previa de la próxima semana:
**¿Sabías que la calidad de tus análisis depende directamente de qué tan "limpios" estén tus datos?**

La próxima semana exploraremos:
- Cómo detectar y corregir errores en datos deportivos
- Estrategias para manejar información faltante
- Técnicas para preparar datos para análisis avanzados
- Métodos para validar la calidad de nuestros datasets

**Pregunta motivadora**: ¿Crees que podrías detectar si los datos de un partido fueron alterados o contienen errores?
