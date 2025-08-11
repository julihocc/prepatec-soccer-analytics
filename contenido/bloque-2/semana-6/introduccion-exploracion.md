# Semana 6: ¿Qué secretos esconden los datos del fútbol?

## ¿Alguna vez te has preguntado qué historia cuentan los números?

**Reflexión inicial**: Cada partido de fútbol genera cientos de datos. ¿Crees que estos números contienen información que no podemos ver solo mirando el partido?

### Pregunta motivadora para la semana:
Si fueras analista del FC Barcelona, ¿qué le preguntarías a los datos de los últimos 200 partidos para descubrir patrones ocultos?

---

## ESTRUCTURA SEMANAL: 3 Sesiones de Descubrimiento

### SESIÓN 1: ¿Cómo interrogamos a los datos? (50 min)
**Pregunta guía**: ¿Qué preguntas pueden responder los números que no vemos a simple vista?
- ¿Cómo preparamos nuestro "laboratorio" de análisis?
- ¿Qué revela la primera inspección de datos futbolísticos?
- ¿Cómo calculamos las estadísticas que importan?

### SESIÓN 2: ¿Qué patrones emergen visualmente? (50 min)  
**Pregunta guía**: ¿Cómo hacer que los datos "hablen" a través de gráficos?
- ¿Qué revelan las distribuciones de goles?
- ¿Cómo identificamos relaciones entre variables?
- ¿Qué correlaciones sorprendentes podemos descubrir?

### SESIÓN 3: ¿Cómo validamos nuestros descubrimientos? (50 min)
**Pregunta guía**: ¿Cuándo podemos confiar en lo que nos dicen los datos?
- ¿Existe realmente la ventaja de jugar en casa?
- ¿Qué sesgos pueden engañarnos en nuestro análisis?
- ¿Cómo comunicamos hallazgos de manera convincente?

---

## ¿Por qué explorar datos deportivos?

**Pregunta reflexiva**: ¿Has notado que algunos entrenadores parecen tomar decisiones "mágicas" que resultan exitosas? ¿Será intuición o habrá datos detrás?

### La revolución silenciosa del fútbol moderno:
- **¿Sabías que...?** El FC Barcelona usa más de 40 métricas diferentes para evaluar cada jugador
- **¿Te imaginas que...?** Los equipos pueden predecir lesiones analizando patrones de movimiento
- **¿Has considerado que...?** Las decisiones de fichajes millonarios se basan en análisis de datos

**Tu misión esta semana**: Convertirte en detective deportivo usando Python como tu lupa de investigación.

¿Estás listo para descubrir qué secretos esconden realmente los datos del fútbol?


# SESIÓN 1: ¿Cómo interrogamos a los datos? (50 minutos)

## Pregunta de apertura: ¿Qué tienen en común un detective y un analista deportivo?

**Reflexiona antes de continuar**: Ambos buscan pistas, investigan patrones y construyen teorías basadas en evidencia. ¿Qué herramientas crees que necesita cada uno?

---

## Momento de curiosidad: ¿Por dónde empezamos nuestra investigación?

Imagina que acabas de ser contratado como analista del Real Madrid. Tu primera misión: **analizar el rendimiento del equipo en los últimos partidos**. 

**Pregunta reflexiva**: ¿Cuáles serían tus primeras 3 preguntas para los datos?

### ¿Qué herramientas necesita nuestro "laboratorio digital"?

Antes de investigar, necesitamos preparar nuestras herramientas. ¿Has notado que un chef prepara todos sus ingredientes antes de cocinar? ¡Nosotros haremos lo mismo con nuestras bibliotecas!

```python
# ¿Por qué necesitamos estas herramientas específicas?
# Pregúntate: ¿Qué hace cada una en nuestro análisis deportivo?

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random

# ¿Sabías que cada herramienta tiene un propósito específico?
# pandas -> ¿Para qué crees que sirve? (Pista: piensa en tablas de Excel)
# numpy -> ¿Qué tipo de cálculos matemáticos necesitaremos?
# matplotlib -> ¿Cómo visualizarías el rendimiento de un equipo?
# seaborn -> ¿Qué hace que un gráfico sea atractivo y profesional?

# Configuración visual profesional (como un analista real)
sns.set_theme(style="whitegrid", palette="viridis")

print("¡Herramientas listas!")
print("¿Te has preguntado alguna vez qué software usan los analistas del Manchester City?")
print("¡Exactamente las mismas herramientas que acabamos de cargar!")
print()
print("Pregunta de reflexión: ¿Por qué crees que elegimos estas bibliotecas específicamente?")
```

## ¿Cómo creamos nuestro propio "laboratorio" de datos futbolísticos?

**Momento de reflexión**: En el mundo real, los datos vienen de cámaras, sensores GPS, aplicaciones móviles... ¿Pero qué pasaría si pudiéramos simular partidos de fútbol para practicar nuestro análisis?

**Pregunta clave**: Si tuvieras que inventar los resultados de 30 partidos entre equipos europeos, ¿qué información incluirías para que fuera realista?

### ¡Vamos a ser "directores técnicos" de nuestro propio dataset!

```python
# ¿Qué equipos europeos reconoces inmediatamente?
# Reflexiona: ¿Por qué elegimos equipos famosos para nuestro análisis?

equipos_europeos = [
    'FC Barcelona', 'Real Madrid', 'Manchester City', 'Liverpool',
    'Bayern Munich', 'Paris Saint-Germain', 'Juventus', 'Chelsea',
    'Arsenal', 'Borussia Dortmund', 'Atletico Madrid', 'Inter Milan'
]

print("Equipos seleccionados para nuestro análisis:")
for i, equipo in enumerate(equipos_europeos, 1):
    print(f"{i:2d}. {equipo}")

print(f"\n¿Cuántos equipos tenemos? ¡Descubrámoslo juntos: {len(equipos_europeos)} equipos!")
print("\nPregunta reflexiva: ¿Qué tienen en común todos estos equipos?")
print("(Pista: piensa en nivel competitivo y reconocimiento mundial)")

# ¿Te has preguntado cómo simular resultados realistas?
# Vamos a crear nuestro "generador de partidos" paso a paso

print("\n" + "="*50)
print("CREANDO NUESTRO DATASET DE PARTIDOS")
print("="*50)

partidos_futbol = []

# ¿Por qué 30 partidos? ¿Es suficiente para encontrar patrones?
for partido_num in range(30):
    # ¿Cómo elegimos dos equipos diferentes para cada partido?
    equipo_local = random.choice(equipos_europeos)
    # Pregunta: ¿Por qué el equipo visitante no puede ser el mismo que el local?
    equipo_visitante = random.choice([e for e in equipos_europeos if e != equipo_local])
    
    # ¿Qué rango de goles es realista en fútbol profesional?
    goles_local = random.randint(0, 4)     # ¿Por qué máximo 4 goles?
    goles_visitante = random.randint(0, 4)  # ¿Es común que un equipo anote más de 4?
    
    # ¿En qué temporadas recientes podríamos basar nuestro análisis?
    temporada = random.choice(['2023-24', '2024-25'])
    
    # Creamos el "registro" de cada partido
    partido_info = {
        'Equipo_Local': equipo_local,
        'Equipo_Visitante': equipo_visitante,
        'Goles_Local': goles_local,
        'Goles_Visitante': goles_visitante,
        'Temporada': temporada
    }
    
    partidos_futbol.append(partido_info)

# ¿Qué ventajas tiene convertir nuestra lista en un DataFrame?
datos_futbol = pd.DataFrame(partidos_futbol)

print(f"¡Dataset creado exitosamente!")
print(f"Tenemos {len(datos_futbol)} partidos simulados")
print(f"Entre {len(equipos_europeos)} equipos europeos")
print("\nPregunta de curiosidad: ¿Qué patrones crees que podremos descubrir en estos datos?")
```

## ¿Cómo realizamos nuestra primera "inspección" de los datos?

**Pregunta detective**: Cuando llegas a la escena de un crimen, ¿qué haces primero? ¡Exacto! Observas todo el panorama general.

**En análisis de datos hacemos lo mismo**. Antes de buscar patrones específicos, necesitamos conocer:
- ¿Qué tipo de información tenemos?
- ¿Cuántos registros hay?
- ¿Existen datos faltantes o extraños?

**Pregunta reflexiva**: Si fueras entrenador y recibieras un reporte de 30 partidos, ¿qué querrías saber primero sobre esos datos?


## Creación de Dataset Futbolístico de Prueba

Para aprender exploración de datos, comenzaremos con un dataset simulado que representa características reales del fútbol profesional.

### Estructura de Datos Deportivos

En el análisis futbolístico, los datos típicamente incluyen:

#### Variables Básicas:
- **Equipos**: Local y visitante
- **Resultados**: Goles marcados por cada equipo
- **Contexto temporal**: Temporada, jornada, fecha
- **Ubicación**: Estadio, ciudad, país

#### Variables Derivadas:
- **Resultado final**: Victoria, empate, derrota
- **Total de goles**: Suma de goles de ambos equipos
- **Diferencia de goles**: Margen de victoria
- **Productividad**: Goles por tiempo de juego

#### Métricas Avanzadas (futuras sesiones):
- **Posesión de balón**: Porcentaje de control
- **Ocasiones de gol**: Tiros a puerta, corners
- **Aspectos disciplinarios**: Tarjetas, faltas
- **Eficiencia**: Conversión de ocasiones en goles

### Importancia de Datos Simulados

Los datos simulados permiten:
1. **Control total**: Conocemos la estructura exacta
2. **Aprendizaje sin limitaciones**: Sin restricciones de privacidad
3. **Experimentación**: Podemos modificar parámetros
4. **Preparación**: Base para trabajar con datos reales

```python
# INSPECCIÓN GENERAL: ¿Qué nos revelan los primeros vistazo?

print("PRIMER VISTAZO A NUESTROS DATOS")
print("="*40)

# ¿Qué información básica deberíamos conocer sobre nuestro dataset?
print(f"Total de partidos analizados: {len(datos_futbol)}")
print(f"Número de columnas (variables): {len(datos_futbol.columns)}")
print(f"Equipos únicos participantes: {datos_futbol['Equipo_Local'].nunique() + datos_futbol['Equipo_Visitante'].nunique()}")

print("\n" + "="*40)
print("ESTRUCTURA DE NUESTROS DATOS")
print("="*40)

# ¿Qué tipos de datos tenemos y por qué es importante saberlo?
print("Información técnica del dataset:")
print(datos_futbol.info())

print("\n¿Observas algo interesante en esta información técnica?")
print("Pregunta reflexiva: ¿Por qué es importante saber el tipo de datos de cada columna?")
```

```python
# ¿CÓMO SE VEN NUESTROS DATOS REALMENTE?

print("MUESTRA DE PARTIDOS SIMULADOS")
print("="*45)

# ¿Por qué es útil ver las primeras filas de nuestros datos?
print("Primeros 5 partidos de nuestro dataset:")
print(datos_futbol.head())

print("\n" + "-"*45)
print("¿Qué observas en estos primeros registros?")

# ¿Y qué hay de los últimos registros? ¿Serán diferentes?
print("\nÚltimos 3 partidos para comparar:")
print(datos_futbol.tail(3))

print("\n" + "="*45)
print("PREGUNTAS DE REFLEXIÓN")
print("="*45)
print("1. ¿Los nombres de equipos te parecen realistas?")
print("2. ¿Los marcadores están dentro de rangos normales?")
print("3. ¿Qué patrones iniciales puedes identificar?")
print("4. ¿Algún resultado te sorprende o parece poco probable?")

# ¿Hay datos faltantes o problemáticos?
print(f"\nVerificación de calidad:")
print(f"   Datos faltantes: {datos_futbol.isnull().sum().sum()}")
print(f"   Partidos duplicados: {datos_futbol.duplicated().sum()}")
print("\n¿Por qué es crucial verificar la calidad de los datos antes de analizarlos?")
```

---

## SÍNTESIS DE LA SESIÓN 1: ¿Qué hemos descubierto juntos?

**Reflexión final de 50 minutos**:
- ¿Qué herramientas de análisis dominamos ahora?
- ¿Cómo construimos un dataset realista desde cero?
- ¿Qué pasos seguimos para inspeccionar datos nuevos?

**Pregunta preparatoria**: ¿Estás listo para que los datos comiencen a "hablar" a través de números y estadísticas?

---

# SESIÓN 2: ¿Qué patrones emergen visualmente? (50 minutos)

## Pregunta de apertura: ¿Cómo hacemos que los números cobren vida?

**Reflexiona**: Has visto miles de estadísticas deportivas en televisión, pero ¿alguna vez te has preguntado cómo los analistas extraen conclusiones significativas de filas y columnas de números?

**Desafío mental**: Si tuvieras que explicarle a tu abuela el rendimiento del Barcelona usando solo números, ¿qué estadísticas elegirías y por qué?

---

## ¿Qué revelan las matemáticas ocultas en el fútbol?

**Momento de curiosidad**: Cada gol, cada partido, cada temporada genera patrones matemáticos. ¿Será posible descubrir tendencias que ni los entrenadores han notado?


## Estadísticas Descriptivas: Primeros Insights

Las **estadísticas descriptivas** proporcionan un resumen cuantitativo de las características principales del dataset, revelando patrones iniciales y aspectos destacables.

### Métricas Fundamentales:

#### Tendencia Central:
- **Media**: Valor promedio, sensible a valores extremos
- **Mediana**: Valor central, robusto ante outliers
- **Moda**: Valor más frecuente, útil para datos categóricos

#### Variabilidad:
- **Desviación estándar**: Dispersión promedio respecto a la media
- **Rango**: Diferencia entre máximo y mínimo
- **Percentiles**: División de datos en proporciones específicas

#### Distribución:
- **Asimetría**: Tendencia hacia valores altos o bajos
- **Curtosis**: Concentración de datos en el centro o extremos

### Aplicación en Fútbol:

En análisis deportivo, estas métricas revelan:
- **Tendencias ofensivas**: Promedio de goles por equipo
- **Variabilidad de rendimiento**: Consistencia de resultados
- **Patrones estacionales**: Diferencias entre temporadas
- **Comportamiento competitivo**: Distribución de victorias/empates/derrotas

```python
# DESCUBRIENDO LOS SECRETOS ESTADÍSTICOS

print("ANÁLISIS ESTADÍSTICO DE GOLES")
print("="*50)

# ¿Qué nos dicen los promedios sobre el fútbol moderno?
promedio_goles_local = datos_futbol['Goles_Local'].mean()
promedio_goles_visitante = datos_futbol['Goles_Visitante'].mean()

print(f"Promedio de goles equipos locales: {promedio_goles_local:.2f}")
print(f"Promedio de goles equipos visitantes: {promedio_goles_visitante:.2f}")

# ¿Existe realmente la "ventaja de jugar en casa"?
diferencia_promedio = promedio_goles_local - promedio_goles_visitante
print(f"\nDiferencia promedio (Local - Visitante): {diferencia_promedio:.2f}")

if diferencia_promedio > 0:
    print("¡Parece que hay ventaja de jugar en casa!")
else:
    print("Los equipos visitantes están rindiendo igual o mejor")

print("\n" + "="*50)
print("ESTADÍSTICAS DESCRIPTIVAS COMPLETAS")
print("="*50)

# ¿Qué información adicional nos revelan estas estadísticas?
print("Análisis detallado de goles por equipo:")
estadisticas_detalladas = datos_futbol[['Goles_Local', 'Goles_Visitante']].describe()
print(estadisticas_detalladas)

print("\nPREGUNTAS DE REFLEXIÓN:")
print("1. ¿Cuál es el máximo de goles que anotó un equipo?")
print("2. ¿Qué te dice la 'desviación estándar' sobre la variabilidad?")
print("3. ¿El 50% de los partidos tienen cuántos goles o menos?")
print("4. ¿Los rangos de goles son realistas comparados con fútbol real?")

# ¿Qué equipos aparecen más frecuentemente en nuestros datos?
print(f"\nPARTICIPACIÓN DE EQUIPOS")
print("="*30)

equipos_como_local = datos_futbol['Equipo_Local'].value_counts()
equipos_como_visitante = datos_futbol['Equipo_Visitante'].value_counts()

print("Los 5 equipos que más jugaron como locales:")
print(equipos_como_local.head())

print("\nPregunta de análisis: ¿La distribución de partidos es equilibrada entre equipos?")
print("¿Esto afectaría nuestras conclusiones sobre rendimiento?")
```

## ¿Cómo transformamos números en historias visuales?

**Pregunta reflexiva**: ¿Alguna vez has notado que una imagen vale más que mil palabras? En análisis de datos, ¡un gráfico puede valer más que mil números!

**Desafío mental**: Si tuvieras que convencer al presidente de un club de fútbol sobre una estrategia usando solo un gráfico, ¿qué información mostrarías?

### ¿Qué patrones se vuelven obvios cuando graficamos nuestros descubrimientos?

<!-- #region -->
---

## Actividades Prácticas - Sesión 1 (40 minutos)

### Ejercicio 1: Análisis Exploratorio Básico (15 minutos)

**Objetivo**: Aplicar técnicas de inspección inicial a un subset de datos

1. **Filtrado de datos**: Selecciona solo partidos de la temporada '2023-24'
2. **Estadísticas específicas**: Calcula media y desviación estándar de goles por equipo
3. **Identificación de extremos**: Encuentra el partido con mayor y menor total de goles

```python
# Tu código aquí:
temporada_actual = df_partidos[df_partidos['temporada'] == '2023-24']
# Completa el análisis...
```

### Ejercicio 2: Comparación Temporal (15 minutos)

**Objetivo**: Analizar diferencias entre temporadas

1. **Agrupación**: Separa datos por temporada
2. **Comparación**: Calcula promedio de goles totales por temporada
3. **Interpretación**: ¿Qué temporada fue más goleadora?

### Ejercicio 3: Análisis de Equipos (10 minutos)

**Objetivo**: Identificar patrones específicos de equipos

1. **Top goleadores**: ¿Qué equipos promedian más goles como locales?
2. **Defensas sólidas**: ¿Qué equipos reciben menos goles como visitantes?
3. **Equilibrio**: ¿Hay equipos con rendimiento similar en casa y fuera?

**Entregable**: Resumen de 3 hallazgos principales con datos numéricos que los respalden.
<!-- #endregion -->

```python
# SESIÓN 2: TÉCNICAS DE ANÁLISIS EXPLORATORIO
**Duración**: 50 minutos | **Objetivo**: Dominar visualización exploratoria y detección de patrones

## Visualización Exploratoria de Datos (EDA Visual)

La **visualización exploratoria** transforma números en insights visuales, revelando patrones que no son evidentes en tablas estadísticas.

### Tipos de Gráficos por Propósito:

#### Distribución de Variables:
- **Histogramas**: Frecuencia de valores continuos
- **Box plots**: Distribución, quartiles y outliers
- **Violin plots**: Distribución detallada con densidad

#### Relaciones entre Variables:
- **Scatter plots**: Correlación entre variables numéricas
- **Heatmaps**: Correlaciones múltiples simultáneas
- **Pair plots**: Relaciones matriciales

#### Comparaciones Categóricas:
- **Bar plots**: Frecuencias por categoría
- **Count plots**: Conteos automáticos
- **Group comparisons**: Análisis por subgrupos

### Estrategia de Exploración Visual:

1. **Univariada**: Una variable a la vez
2. **Bivariada**: Relaciones entre pares
3. **Multivariada**: Patrones complejos múltiples

---

## Distribuciones de Goles: Análisis Univariado
```

```python
# ===============================
# ¿CÓMO CREAMOS GRÁFICOS QUE REVELEN PATRONES?
# ===============================

# ¿Te has preguntado cómo los analistas deportivos "ven" patrones en miles de datos?
print("¿Cómo podemos hacer que los números nos 'hablen' visualmente?")
print("¡Vamos a descubrir el poder de las gráficas!")

# ¿Qué ventaja tiene crear múltiples gráficos en una sola imagen?
fig, axes = plt.subplots(2, 2, figsize=(15, 12))
fig.suptitle('ANÁLISIS DE DISTRIBUCIONES - GOLES EN FÚTBOL EUROPEO', 
             fontsize=16, fontweight='bold', y=0.98)

# 1. ¿Cómo se distribuyen los goles de equipos locales?
print("\nPregunta: ¿Es más común que un equipo local anote 1, 2 o 3 goles?")
axes[0, 0].hist(df_partidos['goles_local'], bins=range(0, 8), 
                alpha=0.7, color='skyblue', edgecolor='black')
axes[0, 0].set_title('Distribución: Goles de Equipos Locales')
axes[0, 0].set_xlabel('Goles por Partido')
axes[0, 0].set_ylabel('Frecuencia')
axes[0, 0].grid(True, alpha=0.3)

# ¿Qué información nos da agregar la línea del promedio?
media_local = df_partidos['goles_local'].mean()
axes[0, 0].axvline(media_local, color='red', linestyle='--', 
                   label=f'Media: {media_local:.2f}')
axes[0, 0].legend()

# 2. Distribución de goles visitantes
axes[0, 1].hist(df_partidos['goles_visitante'], bins=range(0, 8), 
                alpha=0.7, color='lightcoral', edgecolor='black')
axes[0, 1].set_title('Distribución: Goles de Equipos Visitantes')
axes[0, 1].set_xlabel('Goles por Partido')
axes[0, 1].set_ylabel('Frecuencia')
axes[0, 1].grid(True, alpha=0.3)

# Añadiendo línea de media
media_visitante = df_partidos['goles_visitante'].mean()
axes[0, 1].axvline(media_visitante, color='red', linestyle='--', 
                   label=f'Media: {media_visitante:.2f}')
axes[0, 1].legend()

# 3. Box plot comparativo
data_goles = [df_partidos['goles_local'], df_partidos['goles_visitante']]
axes[1, 0].boxplot(data_goles, labels=['Local', 'Visitante'])
axes[1, 0].set_title('Comparación: Local vs Visitante (Box Plot)')
axes[1, 0].set_ylabel('Goles por Partido')
axes[1, 0].grid(True, alpha=0.3)

# 4. Distribución de total de goles
axes[1, 1].hist(df_partidos['total_goles'], bins=range(0, 12), 
                alpha=0.7, color='gold', edgecolor='black')
axes[1, 1].set_title('Distribución: Total de Goles por Partido')
axes[1, 1].set_xlabel('Total de Goles')
axes[1, 1].set_ylabel('Frecuencia')
axes[1, 1].grid(True, alpha=0.3)

# Añadiendo estadísticas descriptivas
media_total = df_partidos['total_goles'].mean()
mediana_total = df_partidos['total_goles'].median()
axes[1, 1].axvline(media_total, color='red', linestyle='--', 
                   label=f'Media: {media_total:.2f}')
axes[1, 1].axvline(mediana_total, color='green', linestyle='--', 
                   label=f'Mediana: {mediana_total:.1f}')
axes[1, 1].legend()

plt.tight_layout()
plt.show()

# Análisis interpretativo
print("=== INTERPRETACIÓN DE DISTRIBUCIONES ===")
print(f"\n1. GOLES LOCALES:")
print(f"   • Media: {media_local:.2f} goles")
print(f"   • Moda: {df_partidos['goles_local'].mode().iloc[0]} goles")
print(f"   • Desviación estándar: {df_partidos['goles_local'].std():.2f}")

print(f"\n2. GOLES VISITANTES:")
print(f"   • Media: {media_visitante:.2f} goles")
print(f"   • Moda: {df_partidos['goles_visitante'].mode().iloc[0]} goles")
print(f"   • Desviación estándar: {df_partidos['goles_visitante'].std():.2f}")

print(f"\n3. INSIGHTS CLAVE:")
diferencia_medias = media_local - media_visitante
print(f"   • Ventaja local promedio: {diferencia_medias:+.2f} goles")
print(f"   • Promedio total por partido: {media_total:.2f} goles")
print(f"   • Partido típico (mediana): {mediana_total:.0f} goles")

# Análisis de forma de distribución
if media_total > mediana_total:
    sesgo = "sesgada hacia la derecha (más partidos con pocos goles)"
else:
    sesgo = "sesgada hacia la izquierda (más partidos con muchos goles)"
    
print(f"   • La distribución está {sesgo}")
```

## Análisis de Relaciones: Explorando Correlaciones

El análisis de **relaciones bivariadas** revela cómo diferentes variables se influencian mutuamente, proporcionando insights sobre patrones subyacentes en el comportamiento futbolístico.

### Tipos de Relaciones:

#### Correlación Positiva:
- A mayor valor de X, mayor valor de Y
- Ejemplo: Goles a favor vs Puntos obtenidos

#### Correlación Negativa:
- A mayor valor de X, menor valor de Y  
- Ejemplo: Goles en contra vs Puntos obtenidos

#### Sin Correlación:
- No hay relación sistemática entre variables
- Ejemplo: Número de jornada vs Goles totales

### Métricas de Correlación:
- **Coeficiente de Pearson**: Relaciones lineales (-1 a +1)
- **Coeficiente de Spearman**: Relaciones monotónicas
- **Matriz de correlación**: Relaciones múltiples simultáneas

```python
# VISUALIZACIÓN 1: ¿Cómo se distribuyen los goles en el fútbol?

print("CREANDO NUESTRO PRIMER GRÁFICO ANALÍTICO")
print("="*50)

# ¿Qué revela la distribución de goles sobre la naturaleza del fútbol?
plt.figure(figsize=(12, 5))

# Subplot 1: ¿Cómo se distribuyen los goles de equipos locales?
plt.subplot(1, 2, 1)
sns.countplot(data=datos_futbol, x='Goles_Local', palette='viridis')
plt.title('¿Cuántos goles anotan los equipos en casa?', fontsize=12, fontweight='bold')
plt.xlabel('Goles anotados como local')
plt.ylabel('Frecuencia (número de partidos)')

# Subplot 2: ¿Y los equipos visitantes?
plt.subplot(1, 2, 2)  
sns.countplot(data=datos_futbol, x='Goles_Visitante', palette='plasma')
plt.title('¿Cuántos goles anotan visitando?', fontsize=12, fontweight='bold')
plt.xlabel('Goles anotados como visitante')
plt.ylabel('Frecuencia (número de partidos)')

plt.tight_layout()
plt.show()

print("\nANÁLISIS DE LOS GRÁFICOS:")
print("="*30)

# Calculemos algunas observaciones numéricas que apoyen lo visual
partidos_sin_goles_local = len(datos_futbol[datos_futbol['Goles_Local'] == 0])
partidos_sin_goles_visitante = len(datos_futbol[datos_futbol['Goles_Visitante'] == 0])

print(f"Partidos donde el local no anotó: {partidos_sin_goles_local}")
print(f"Partidos donde el visitante no anotó: {partidos_sin_goles_visitante}")

goles_altos_local = len(datos_futbol[datos_futbol['Goles_Local'] >= 3])
goles_altos_visitante = len(datos_futbol[datos_futbol['Goles_Visitante'] >= 3])

print(f"Partidos con 3+ goles del local: {goles_altos_local}")
print(f"Partidos con 3+ goles del visitante: {goles_altos_visitante}")

print("\nPREGUNTAS DE REFLEXIÓN:")
print("1. ¿Qué diferencias observas entre los dos gráficos?")
print("2. ¿Es más común que un equipo anote 1 gol o 2 goles?")
print("3. ¿Los resultados de 0 goles son frecuentes en ambos casos?")
print("4. ¿Qué nos dice esto sobre la dificultad de anotar fuera de casa?")
```

```python
# VISUALIZACIÓN 2: ¿Existe correlación entre goles locales y visitantes?

print("BUSCANDO RELACIONES OCULTAS EN LOS DATOS")
print("="*50)

# ¿Los partidos con muchos goles locales también tienen muchos goles visitantes?
plt.figure(figsize=(10, 6))

# Crear scatter plot para buscar patrones
plt.scatter(datos_futbol['Goles_Local'], datos_futbol['Goles_Visitante'], 
           alpha=0.7, s=80, c='darkblue', edgecolors='white', linewidth=1)

plt.title('¿Los goles locales predicen los goles visitantes?', fontsize=14, fontweight='bold')
plt.xlabel('Goles del equipo local')
plt.ylabel('Goles del equipo visitante')

# Añadir líneas de referencia para análisis visual
plt.axhline(y=promedio_goles_visitante, color='red', linestyle='--', alpha=0.7, 
           label=f'Promedio visitante: {promedio_goles_visitante:.1f}')
plt.axvline(x=promedio_goles_local, color='green', linestyle='--', alpha=0.7,
           label=f'Promedio local: {promedio_goles_local:.1f}')

plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

# ¿Qué nos dice la correlación matemática?
correlacion = datos_futbol['Goles_Local'].corr(datos_futbol['Goles_Visitante'])
print(f"\nCorrelación entre goles locales y visitantes: {correlacion:.3f}")

if abs(correlacion) > 0.5:
    print("¡Hay una correlación fuerte!")
elif abs(correlacion) > 0.3:
    print("Hay una correlación moderada")
else:
    print("La correlación es débil o inexistente")

print("\nINTERPRETACIÓN DEL GRÁFICO:")
print("="*35)
print("Observa cada punto en el gráfico:")
print("   - Cada punto = un partido específico")
print("   - Eje X = goles del equipo local")  
print("   - Eje Y = goles del equipo visitante")
print("   - Líneas punteadas = promedios generales")

print("\nPREGUNTAS DE ANÁLISIS:")
print("1. ¿Hay más puntos arriba o abajo de la línea roja?")
print("2. ¿Hay más puntos a la derecha o izquierda de la línea verde?")
print("3. ¿Ves algún patrón en la distribución de puntos?")
print("4. ¿Los partidos con muchos goles son raros o comunes?")
print("5. ¿Qué significa que la correlación sea positiva/negativa/cero?")
```

---

## SÍNTESIS DE LA SESIÓN 2: ¿Qué patrones hemos revelado?

**Reflexión de 50 minutos**:
- ¿Cómo las estadísticas descriptivas nos ayudan a entender el fútbol?
- ¿Qué diferencias importantes descubrimos entre equipos locales y visitantes?
- ¿Cómo los gráficos hacen obvios patrones que los números ocultan?

**Pregunta preparatoria**: ¿Estás listo para aplicar todo este conocimiento a situaciones de análisis deportivo real?

---

# SESIÓN 3: ¿Cómo validamos nuestros descubrimientos? (50 minutos)

## Pregunta de apertura: ¿Cuándo podemos confiar en lo que nos dicen los datos?

**Reflexiona**: Has escuchado la frase "las estadísticas pueden mentir". ¿Pero cómo sabemos cuándo nuestros análisis son confiables y cuándo pueden estar engañándonos?

**Desafío profesional**: Si fueras analista del Real Madrid y tuvieras que presentar conclusiones al entrenador, ¿cómo te asegurarías de que tus recomendaciones son sólidas?

---

## ¿Qué preguntas específicas pueden responder nuestros datos?

**Momento de aplicación**: Ahora que dominamos las herramientas básicas, vamos a investigar preguntas específicas que cualquier aficionado al fútbol se haría.

```python
# ===============================
# VALIDACIÓN 1: VENTAJA LOCAL
# ===============================

from scipy.stats import ttest_ind, chi2_contingency
import numpy as np

print("=== VALIDACIÓN DE HIPÓTESIS: VENTAJA LOCAL ===")

# Preparación de datos para análisis
goles_locales = df_partidos['goles_local']
goles_visitantes = df_partidos['goles_visitante']
resultados = df_partidos['resultado'].value_counts()

# Test estadístico: Comparación de medias
t_stat, p_value = ttest_ind(goles_locales, goles_visitantes)

print(f"\n1. ANÁLISIS DE GOLES:")
print(f"   Media goles locales: {goles_locales.mean():.3f}")
print(f"   Media goles visitantes: {goles_visitantes.mean():.3f}")
print(f"   Diferencia promedio: {goles_locales.mean() - goles_visitantes.mean():+.3f}")

print(f"\n2. TEST ESTADÍSTICO (t-test):")
print(f"   Estadístico t: {t_stat:.3f}")
print(f"   Valor p: {p_value:.3f}")

# Interpretación del test
if p_value < 0.05:
    significancia = "SÍ hay diferencia estadísticamente significativa"
else:
    significancia = "NO hay diferencia estadísticamente significativa"
    
print(f"   Conclusión: {significancia}")

# Análisis de proporciones de victoria
print(f"\n3. ANÁLISIS DE RESULTADOS:")
total_partidos = len(df_partidos)
for resultado, cantidad in resultados.items():
    porcentaje = (cantidad / total_partidos) * 100
    print(f"   • {resultado}: {cantidad}/{total_partidos} ({porcentaje:.1f}%)")

# Test de chi-cuadrado para independencia de resultados
tabla_contingencia = pd.crosstab(df_partidos['resultado'], df_partidos['temporada'])
chi2, p_chi2, dof, expected = chi2_contingency(tabla_contingencia)

print(f"\n4. TEST DE INDEPENDENCIA (Chi²):")
print(f"   Chi² estadístico: {chi2:.3f}")
print(f"   Valor p: {p_chi2:.3f}")
print(f"   Grados de libertad: {dof}")

# Visualización de la evidencia
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# Gráfico 1: Comparación de distribuciones
ax1.hist(goles_locales, alpha=0.7, label='Local', bins=range(0, 8), color='skyblue')
ax1.hist(goles_visitantes, alpha=0.7, label='Visitante', bins=range(0, 8), color='lightcoral')
ax1.axvline(goles_locales.mean(), color='blue', linestyle='--', label=f'Media Local: {goles_locales.mean():.2f}')
ax1.axvline(goles_visitantes.mean(), color='red', linestyle='--', label=f'Media Visitante: {goles_visitantes.mean():.2f}')
ax1.set_title('Distribución de Goles: Local vs Visitante')
ax1.set_xlabel('Goles por Partido')
ax1.set_ylabel('Frecuencia')
ax1.legend()
ax1.grid(True, alpha=0.3)

# Gráfico 2: Proporción de resultados
colores = ['lightblue', 'lightcoral', 'lightgreen']
wedges, texts, autotexts = ax2.pie(resultados.values, labels=resultados.index, 
                                   autopct='%1.1f%%', colors=colores)
ax2.set_title('Distribución de Resultados de Partidos')

plt.tight_layout()
plt.show()

# Conclusión integral
print(f"\n=== CONCLUSIÓN SOBRE VENTAJA LOCAL ===")
ventaja_numerica = goles_locales.mean() - goles_visitantes.mean()
porcentaje_victorias_local = (resultados['Victoria Local'] / total_partidos) * 100

if p_value < 0.05 and ventaja_numerica > 0:
    conclusion = "CONFIRMADA"
    explicacion = "Los datos apoyan estadísticamente la existencia de ventaja local"
elif ventaja_numerica > 0:
    conclusion = "PARCIALMENTE CONFIRMADA"
    explicacion = "Hay indicios de ventaja local pero no son estadísticamente significativos"
else:
    conclusion = "REFUTADA"
    explicacion = "Los datos no apoyan la existencia de ventaja local"

print(f"Estado de la hipótesis: {conclusion}")
print(f"Explicación: {explicacion}")
print(f"Evidencia numérica: {ventaja_numerica:+.3f} goles de ventaja promedio")
print(f"Evidencia de resultados: {porcentaje_victorias_local:.1f}% de victorias locales")
```

## Identificación de Sesgos y Limitaciones

El **pensamiento crítico** en análisis de datos requiere reconocer las limitaciones inherentes de nuestro estudio y los posibles sesgos que pueden influir en las conclusiones.

### Tipos de Sesgos en Datos Deportivos:

#### Sesgos de Muestreo:
- **Representatividad**: ¿Nuestra muestra representa toda la población?
- **Temporalidad**: ¿Los datos abarcan períodos suficientemente largos?
- **Selección**: ¿Hay equipos o situaciones sobrerrepresentados?

#### Sesgos de Medición:
- **Precisión**: ¿Los datos capturan lo que realmente queremos medir?
- **Completitud**: ¿Faltan variables importantes para el análisis?
- **Consistencia**: ¿Los criterios de medición son uniformes?

#### Sesgos de Interpretación:
- **Confirmación**: ¿Buscamos solo evidencia que confirme nuestras ideas?
- **Causalidad**: ¿Confundimos correlación con causación?
- **Generalización**: ¿Extrapolamos más allá de lo que permiten los datos?

### Limitaciones de Nuestro Estudio:

#### Datos Simulados:
- **Ventaja**: Control total sobre la estructura
- **Limitación**: Pueden no reflejar complejidades reales
- **Impacto**: Resultados válidos para aprendizaje, no para decisiones profesionales

#### Tamaño de Muestra:
- **Actual**: 200 partidos
- **Ideal para conclusiones generales**: 1000+ partidos
- **Consecuencia**: Menor poder estadístico para detectar efectos pequeños

#### Variables Ausentes:
- **Calidad de equipos**: Presupuesto, ranking, historial
- **Contexto situacional**: Importancia del partido, clima, lesiones
- **Métricas avanzadas**: Posesión, tiros, corners, faltas

```python
# ===============================
# EVALUACIÓN CRÍTICA DE NUESTRO ANÁLISIS
# ===============================

print("=== AUTOEVALUACIÓN CRÍTICA DEL ESTUDIO ===")

# 1. Análisis de representatividad
equipos_unicos = df_partidos['equipo_local'].nunique()
partidos_por_equipo = df_partidos.groupby('equipo_local').size()
equipos_balanceados = (partidos_por_equipo.std() / partidos_por_equipo.mean()) * 100

print(f"\n1. REPRESENTATIVIDAD DE LA MUESTRA:")
print(f"   • Equipos únicos analizados: {equipos_unicos}")
print(f"   • Partidos promedio por equipo: {partidos_por_equipo.mean():.1f}")
print(f"   • Coeficiente de variación: {equipos_balanceados:.1f}%")

if equipos_balanceados < 30:
    balance_evaluacion = "BUENO - Distribución relativamente equilibrada"
else:
    balance_evaluacion = "REGULAR - Algunos equipos sobrerrepresentados"
    
print(f"   • Evaluación del balance: {balance_evaluacion}")

# 2. Análisis de poder estadístico
n_total = len(df_partidos)
effect_size = abs(goles_locales.mean() - goles_visitantes.mean()) / np.sqrt(
    (goles_locales.var() + goles_visitantes.var()) / 2)

print(f"\n2. PODER ESTADÍSTICO:")
print(f"   • Tamaño de muestra: {n_total} partidos")
print(f"   • Tamaño del efecto (Cohen's d): {effect_size:.3f}")

if effect_size < 0.2:
    effect_interpretation = "PEQUEÑO"
elif effect_size < 0.5:
    effect_interpretation = "MEDIANO"
else:
    effect_interpretation = "GRANDE"
    
print(f"   • Interpretación del efecto: {effect_interpretation}")

# 3. Evaluación de consistencia temporal
consistencia_temporal = df_partidos.groupby('temporada').agg({
    'goles_local': 'mean',
    'goles_visitante': 'mean',
    'total_goles': 'mean'
}).round(3)

print(f"\n3. CONSISTENCIA TEMPORAL:")
print(consistencia_temporal)

# Calcular variabilidad entre temporadas
variabilidad_temporal = consistencia_temporal.std().mean()
print(f"   • Variabilidad promedio entre temporadas: {variabilidad_temporal:.3f}")

if variabilidad_temporal < 0.1:
    consistencia_eval = "ALTA - Patrones estables entre temporadas"
elif variabilidad_temporal < 0.3:
    consistencia_eval = "MODERADA - Algunas diferencias temporales"
else:
    consistencia_eval = "BAJA - Grandes diferencias entre temporadas"
    
print(f"   • Evaluación de consistencia: {consistencia_eval}")

# 4. Identificación de outliers potenciales
q1_total = df_partidos['total_goles'].quantile(0.25)
q3_total = df_partidos['total_goles'].quantile(0.75)
iqr = q3_total - q1_total
limite_inferior = q1_total - 1.5 * iqr
limite_superior = q3_total + 1.5 * iqr

outliers = df_partidos[(df_partidos['total_goles'] < limite_inferior) | 
                       (df_partidos['total_goles'] > limite_superior)]

print(f"\n4. ANÁLISIS DE VALORES EXTREMOS:")
print(f"   • Rango intercuartílico (IQR): {iqr:.1f}")
print(f"   • Límites de outliers: [{limite_inferior:.1f}, {limite_superior:.1f}]")
print(f"   • Partidos outliers detectados: {len(outliers)} ({len(outliers)/len(df_partidos)*100:.1f}%)")

if len(outliers) > 0:
    print(f"   • Ejemplos de outliers:")
    for idx, outlier in outliers.head(3).iterrows():
        print(f"     - {outlier['equipo_local']} vs {outlier['equipo_visitante']}: {outlier['total_goles']} goles")

# 5. Evaluación de la calidad general
print(f"\n=== EVALUACIÓN GENERAL DE CALIDAD ===")

criterios_calidad = {
    'Tamaño de muestra': 'ADECUADO' if n_total >= 150 else 'INSUFICIENTE',
    'Balance de equipos': 'BUENO' if equipos_balanceados < 30 else 'REGULAR',
    'Consistencia temporal': consistencia_eval.split(' - ')[0],
    'Presencia de outliers': 'CONTROLADO' if len(outliers)/len(df_partidos) < 0.05 else 'REQUIERE ATENCIÓN',
    'Significancia estadística': 'DETECTADA' if p_value < 0.05 else 'NO DETECTADA'
}

for criterio, evaluacion in criterios_calidad.items():
    status_symbol = "OK" if evaluacion in ['ADECUADO', 'BUENO', 'ALTA', 'CONTROLADO', 'DETECTADA'] else "ATENCION"
    print(f"   {status_symbol} {criterio}: {evaluacion}")

# Recomendaciones para mejoras
print(f"\n=== RECOMENDACIONES PARA MEJORAS ===")
print("1. INCREMENTAR tamaño de muestra a 500+ partidos")
print("2. INCLUIR variables adicionales: posesión, tiros, faltas")
print("3. AGREGAR contexto situacional: importancia del partido")
print("4. VALIDAR con datos reales de ligas profesionales")
print("5. APLICAR técnicas de machine learning para patrones complejos")
```

---

## SESIÓN 3: ¿Cómo aplicamos lo aprendido? (50 minutos)

**Pregunta guía**: ¿Podemos responder preguntas sencillas con nuestros datos?

### Actividad Práctica: Mini-investigación guiada

**Objetivo**: Usar las herramientas básicas que acabamos de aprender para responder preguntas simples sobre fútbol.

#### Pregunta de investigación: ¿Cuál equipo tiene mejor rendimiento ofensivo?

**Paso 1: ¿Qué significa "mejor rendimiento ofensivo"?**
- Reflexiona: ¿Es mejor el equipo que anota más goles en total o el que tiene mejor promedio?
- ¿Por qué podría ser importante considerar cuántos partidos ha jugado cada equipo?

**Paso 2: Analicemos los datos**
- Calculemos goles totales por equipo
- Calculemos promedio de goles por partido
- Comparemos los resultados

**Paso 3: ¿Qué descubrimos?**
- ¿El equipo con más goles totales es el mismo que tiene mejor promedio?
- ¿Qué equipo elegirías para tu equipo fantástico?

#### Reflexión final
- ¿Qué fue lo más sorprendente que descubriste?
- ¿Qué otras preguntas te surgieron?
- ¿Cómo podrías mejorar este análisis?

```python
# INVESTIGACIÓN SIMPLE: ¿Qué equipos anotan más goles?

print("ANÁLISIS DE RENDIMIENTO POR EQUIPO")
print("="*50)

# ¿Te has preguntado alguna vez cómo un analista deportivo determina cuál equipo tiene mejor ataque?
print("¿Cómo medirías tú el poder ofensivo de un equipo?")
print("Reflexiona: ¿Mejor el que anota más goles totales o el que tiene mejor promedio?")

print("\nPaso 1: Calculemos goles totales por equipo")
print("-"*40)

# ¿Qué información necesitamos recopilar de cada equipo?
equipos_goles = []

# Vamos a investigar equipo por equipo
for equipo in equipos_europeos:
    # ¿Cuántos goles anota este equipo cuando juega en casa?
    print(f"\nAnalizando a {equipo}...")
    goles_casa = datos_futbol[datos_futbol['Equipo_Local'] == equipo]['Goles_Local'].sum()
    partidos_casa = len(datos_futbol[datos_futbol['Equipo_Local'] == equipo])
    
    # ¿Y cuántos cuando visita otros estadios?
    goles_visitante = datos_futbol[datos_futbol['Equipo_Visitante'] == equipo]['Goles_Visitante'].sum()
    partidos_visitante = len(datos_futbol[datos_futbol['Equipo_Visitante'] == equipo])
    
    # ¿Cuál es su rendimiento total?
    goles_totales = goles_casa + goles_visitante
    partidos_totales = partidos_casa + partidos_visitante
    
    # ¿Cómo calculamos el promedio? ¿Por qué es importante?
    if partidos_totales > 0:
        promedio = goles_totales / partidos_totales
        print(f"  Goles en casa: {goles_casa}, Goles visitando: {goles_visitante}")
        print(f"  Total: {goles_totales} goles en {partidos_totales} partidos")
        print(f"  Promedio: {promedio:.2f} goles por partido")
    else:
        promedio = 0
        print(f"  Este equipo no jugó partidos en nuestros datos")
    
    equipos_goles.append({
        'Equipo': equipo,
        'Goles_Totales': goles_totales,
        'Partidos_Jugados': partidos_totales,
        'Promedio_Goles': promedio_goles,
        'Goles_Casa': goles_como_local,
        'Goles_Visitante': goles_como_visitante
    })

# Convertir a DataFrame para análisis más fácil
rendimiento_df = pd.DataFrame(equipos_rendimiento)

print("TOP 5 EQUIPOS POR TOTAL DE GOLES:")
top_goleadores = rendimiento_df.sort_values('Goles_Totales', ascending=False).head()
print(top_goleadores[['Equipo', 'Goles_Totales', 'Partidos_Jugados', 'Promedio_Goles']])

print("\nTOP 5 EQUIPOS POR PROMEDIO DE GOLES:")
top_promedio = rendimiento_df.sort_values('Promedio_Goles', ascending=False).head()
print(top_promedio[['Equipo', 'Promedio_Goles', 'Goles_Totales', 'Partidos_Jugados']])

print("\nANÁLISIS CASA vs VISITANTE:")
print("="*35)

for _, fila in rendimiento_df.head(5).iterrows():
    equipo = fila['Equipo']
    goles_casa = fila['Goles_Casa'] 
    goles_visitante = fila['Goles_Visitante']
    
    if goles_casa > goles_visitante:
        rendimiento = "Mejor en casa"
    elif goles_visitante > goles_casa:
        rendimiento = "Mejor visitando"
    else:
        rendimiento = "Igual rendimiento"
    
    print(f"{equipo:20} | Casa: {goles_casa:2d} | Visitante: {goles_visitante:2d} | {rendimiento}")

print("\nPREGUNTAS DE REFLEXIÓN FINAL:")
print("="*35)
print("1. ¿El equipo con más goles totales es también el de mejor promedio?")
print("2. ¿Qué equipos muestran clara 'ventaja de casa'?")
print("3. ¿Algún equipo rinde mejor como visitante? ¿Por qué podría ser?")
print("4. ¿Los resultados te sorprenden o eran esperables?")
print("5. ¿Qué limitaciones tiene nuestro análisis con solo 30 partidos?")

print("\nPENSAMIENTO CRÍTICO:")
print("¿Qué factores del fútbol real NO están capturados en estos datos?")
print("(Ejemplos: calidad de rivales, importancia del partido, lesiones, clima...)")
```

---

# SÍNTESIS FINAL: ¿Qué hemos descubierto juntos esta semana?

## Reflexión de las 3 sesiones (150 minutos totales)

### SESIÓN 1: ¿Cómo interrogamos a los datos?
**Lo que dominamos ahora**:
- Configurar nuestro "laboratorio" de análisis deportivo
- Crear datasets realistas desde cero
- Realizar inspecciones técnicas de calidad de datos
- Identificar tipos de variables y estructuras de información

### SESIÓN 2: ¿Qué patrones emergen visualmente?
**Lo que revelamos**:
- Calcular estadísticas descriptivas significativas
- Descubrir la posible "ventaja de casa" en datos
- Crear visualizaciones que hacen obvios los patrones ocultos
- Interpretar correlaciones entre variables deportivas

### SESIÓN 3: ¿Cómo validamos nuestros descubrimientos?
**Lo que investigamos**:
- Analizar rendimiento individualizado por equipo
- Comparar métricas diferentes (totales vs promedios)
- Evaluar limitaciones y sesgos en nuestros análisis
- Formular preguntas críticas sobre nuestras conclusiones

---

## Pregunta de preparación para la próxima semana:

**¿Te has dado cuenta de que acabas de hacer el mismo trabajo que los analistas profesionales del FC Barcelona o Manchester City?**

### ¿Qué nuevas preguntas quieres responder ahora?

**Reflexión personal**: 
- ¿Cuál fue tu descubrimiento más sorprendente?
- ¿Qué aspecto del análisis te resultó más desafiante?
- ¿Cómo cambió tu perspectiva sobre el uso de datos en deportes?

### Vista previa de la próxima semana:
**¿Sabías que existen diferentes tipos de datos deportivos más allá de goles y resultados?**

La próxima semana exploraremos:
- Datos de rendimiento individual de jugadores
- Métricas de tiempo y ubicación en el campo
- Estadísticas físicas como distancia recorrida y velocidad
- Precisión de pases y efectividad en diferentes zonas

**Pregunta motivadora**: ¿Crees que podrías predecir qué jugador será la próxima estrella mundial analizando sus datos?
