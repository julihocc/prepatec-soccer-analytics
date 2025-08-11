---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.17.2
  kernelspec:
    display_name: .venv (3.10.12)
    language: python
    name: python3
---

# Semana 4: ¿Cómo procesan miles de datos los analistas profesionales?

## SESIÓN 1: ¿Por qué necesitas herramientas más potentes que listas simples? (50 min)
**Pregunta guía**: ¿Cómo calcularías estadísticas de 1000 jugadores en segundos?

## SESIÓN 2: ¿Cómo organizas datos complejos como nombres, fechas y estadísticas? (50 min)  
**Pregunta guía**: ¿Qué herramienta usarían los clubes para gestionar información completa de plantillas?

## SESIÓN 3: ¿Cómo integras todo en un sistema de análisis profesional? (50 min)
**Pregunta guía**: ¿Cómo crearías un sistema que analice temporadas completas automáticamente?

---

### Pregunta Central de la Semana
**¿Te has preguntado alguna vez cómo los clubes como el Real Madrid analizan datos de cientos de jugadores y miles de partidos para tomar decisiones estratégicas?**

### Descubrimiento de la Semana
Vas a aprender las dos herramientas fundamentales que usan los científicos de datos profesionales:
- **NumPy**: La calculadora más potente del mundo para números
- **Pandas**: El organizador más inteligente para cualquier tipo de datos

### Conexión con tu experiencia
¿Recuerdas cuando calculabas promedios de goles uno por uno? ¿O cuando organizabas información de jugadores en listas separadas? ¡Eso está a punto de cambiar para siempre!

---

<!-- #region -->
# SESIÓN 1: ¿Por qué las listas normales no son suficientes para análisis masivos?
**(50 minutos)**

## Pregunta Central de la Sesión
**¿Te has preguntado cómo calculan los analistas deportivos estadísticas de temporadas completas en segundos?**

### Tu situación actual
Hasta ahora has usado listas normales de Python. ¿Recuerdas cómo calculabas el promedio de goles?
```python
goles = [2, 1, 3, 0, 2]
promedio = sum(goles) / len(goles)
```

### Reflexión inicial
¿Qué pasaría si tuvieras que calcular promedios de 10,000 jugadores con este método? ¿Cuánto tiempo tardarías?

### Analogía deportiva
**Piensa en esto**: ¿Cuál es la diferencia entre:
- Cronometrar manualmente a cada corredor en una maratón vs.
- Usar un chip electrónico que registra automáticamente todos los tiempos?

**NumPy** es como el chip electrónico para cálculos matemáticos.

---

## Descubriendo NumPy: Tu calculadora profesional

### ¿Qué hace diferente a NumPy?
- Procesa miles de números simultáneamente
- Realiza operaciones matemáticas en milisegundos
- Es la base de todas las herramientas de ciencia de datos

### Primera pregunta práctica
¿Cómo crees que se vería la diferencia en velocidad entre listas normales y NumPy?
<!-- #endregion -->

```python
# Tu primer contacto con la velocidad profesional
import numpy as np

print("NumPy importado exitosamente")
print(f"Versión: {np.__version__}")

# ¿Cuál crees que será la diferencia entre estos dos enfoques?
print("\n=== COMPARACIÓN: ¿Notas alguna diferencia? ===")

# Método anterior: Lista normal de Python
goles_lista = [15, 8, 22, 12, 18, 7, 25, 14]
print("Con lista normal:", goles_lista)
print("Tipo:", type(goles_lista))

# Método profesional: Array de NumPy
goles_array = np.array([15, 8, 22, 12, 18, 7, 25, 14])
print("Con array NumPy:", goles_array)
print("Tipo:", type(goles_array))

# Pregunta de observación: ¿Ves alguna diferencia visual?
# La magia está en lo que puedes HACER con cada uno...

print("\n¿Recuerdas cómo calcularías el promedio con listas?")
promedio_lista = sum(goles_lista) / len(goles_lista)
print(f"Promedio con listas: {promedio_lista}")

print("\n¿Cómo crees que será con NumPy?")
promedio_array = np.mean(goles_array)
print(f"Promedio con NumPy: {promedio_array}")

# Reflexión: Parece similar, ¿verdad? Pero espera a ver la siguiente demostración...
```

## ¿Cómo se procesan miles de datos simultáneamente?

### Pregunta desafiante
¿Cómo calcularías el promedio de goles por partido para 20 jugadores que han jugado diferente número de partidos?

**Con listas tradicionales**: Necesitarías un bucle que procese cada jugador individualmente.

**Con NumPy**: ¿Qué crees que pasaría si pudieras hacer todas las divisiones de una sola vez?

### Tu momento de descubrimiento
Vas a ver algo que parece imposible: matemáticas simultáneas en múltiples números.

```python
# La demostración que cambiará tu perspectiva sobre los cálculos
print("=== EL PODER DE LAS OPERACIONES SIMULTÁNEAS ===")

# Datos de rendimiento de 10 jugadores de La Liga
goles_jornada = np.array([2, 0, 1, 3, 1, 0, 2, 1, 0, 4])
partidos_jugados = np.array([25, 28, 22, 30, 26, 24, 27, 29, 21, 26])

print("Goles de 10 jugadores:", goles_jornada)
print("Partidos jugados:", partidos_jugados)

# ¿Te imaginas calcular esto uno por uno?
# ¡Mira la magia de NumPy!

print("\n=== CÁLCULOS INSTANTÁNEOS PARA TODOS ===")

# Una línea hace el trabajo de un bucle completo
promedio_goles = goles_jornada / partidos_jugados
print("Promedio goles/partido:", np.round(promedio_goles, 3))

# ¿Qué más crees que puedes calcular instantáneamente?
print(f"Mejor goleador de la jornada: {np.max(goles_jornada)} goles")
print(f"Promedio general de goles: {np.mean(goles_jornada):.2f}")
print(f"¿Qué tan dispersos están los datos?: {np.std(goles_jornada):.2f}")
print(f"Total de goles de todos: {np.sum(goles_jornada)}")

# Operaciones lógicas masivas: ¿Quiénes están sobre la media?
jugadores_destacados = goles_jornada > np.mean(goles_jornada)
print(f"Jugadores sobre la media: {np.sum(jugadores_destacados)} de {len(goles_jornada)}")

# Transformaciones instantáneas (sistema de puntos de fantasía)
puntos_fantasia = goles_jornada * 6 + (partidos_jugados * 0.1)
print("Puntos fantasía calculados:", np.round(puntos_fantasia, 1))

# Reflexión: ¿Notas que NO escribimos ni un solo bucle?
```

## ¿Cómo organizas datos de múltiples jornadas simultáneamente?

### Pregunta de escalamiento
¿Qué harías si necesitas analizar goles de 10 jugadores durante 5 jornadas diferentes?

**Con listas**: Tendrías que crear listas dentro de listas, muy complicado de manejar.

### Tu nuevo descubrimiento: Arrays 2D
¿Has visto alguna vez una tabla de Excel? NumPy puede crear "tablas" de números que se manejan como un solo objeto.

### Reflexión
¿Para qué situaciones deportivas sería útil organizar datos en forma de tabla?

```python
# Descubriendo las matrices: Datos organizados en filas y columnas
print("=== ORGANIZANDO DATOS DE MÚLTIPLES JORNADAS ===")

# ¿Cómo representarías goles de 5 jugadores en 4 jornadas?
# Filas = jugadores, Columnas = jornadas
goles_temporada = np.array([
    [2, 1, 0, 3],  # Jugador 1: goles en jornadas 1, 2, 3, 4
    [0, 2, 1, 1],  # Jugador 2: goles en jornadas 1, 2, 3, 4
    [1, 1, 2, 0],  # Jugador 3: goles en jornadas 1, 2, 3, 4
    [3, 0, 1, 2],  # Jugador 4: goles en jornadas 1, 2, 3, 4
    [1, 3, 0, 1]   # Jugador 5: goles en jornadas 1, 2, 3, 4
])

print("Matriz completa de goles:")
print(goles_temporada)
print(f"Forma de la matriz: {goles_temporada.shape}")  # (filas, columnas)

# ¿Qué análisis crees que puedes hacer ahora?

print("\n=== ANÁLISIS AUTOMÁTICO POR JUGADOR Y JORNADA ===")

# Totales por jugador (suma cada fila)
goles_por_jugador = np.sum(goles_temporada, axis=1)
print("Total goles por jugador:", goles_por_jugador)

# Totales por jornada (suma cada columna)  
goles_por_jornada = np.sum(goles_temporada, axis=0)
print("Total goles por jornada:", goles_por_jornada)

# ¿Quién es el mejor?
mejor_jugador = np.argmax(goles_por_jugador)
mejor_jornada = np.argmax(goles_por_jornada)

print(f"Mejor jugador: Jugador {mejor_jugador + 1} con {goles_por_jugador[mejor_jugador]} goles")
print(f"Jornada más goleadora: Jornada {mejor_jornada + 1} con {goles_por_jornada[mejor_jornada]} goles")

# Promedios automáticos
promedio_por_jugador = np.mean(goles_temporada, axis=1)
print("Promedio goles/jornada por jugador:", np.round(promedio_por_jugador, 2))

# Pregunta de reflexión: ¿Te das cuenta de que no escribiste bucles para nada de esto?
```

### Actividad Práctica: Análisis de tu Equipo

**Tiempo estimado: 12 minutos**

**Tu desafío**: Crea un análisis NumPy de las asistencias de 4 jugadores durante 3 jornadas.

**Datos sugeridos** (o usa datos reales de tu equipo favorito):
```
Jugador 1: [3, 1, 2] asistencias
Jugador 2: [0, 2, 1] asistencias  
Jugador 3: [1, 0, 3] asistencias
Jugador 4: [2, 2, 0] asistencias
```

**Tareas**:
1. Crear la matriz de asistencias
2. Calcular total de asistencias por jugador
3. Encontrar la jornada con más asistencias
4. Calcular el promedio por jugador
5. Identificar al mejor asistente

---

## Resumen de la Sesión 1 (50 minutos)

**¿Qué hemos descubierto sobre NumPy?**

### Conceptos Clave:
- **Arrays**: Listas súper eficientes para cálculos masivos
- **Operaciones vectorizadas**: Cálculos simultáneos en todos los elementos
- **Arrays 2D**: Matrices para organizar datos multidimensionales
- **Funciones estadísticas**: mean, sum, max, min, std automáticas

### Ventajas sobre Listas Tradicionales:
- **Velocidad**: Miles de veces más rápido
- **Simplicidad**: Una línea hace lo que antes necesitaba bucles
- **Funcionalidad**: Estadísticas avanzadas integradas
- **Profesionalidad**: Estándar en ciencia de datos

**Pregunta para reflexionar**: ¿Cómo cambiaría tu capacidad de análisis si pudieras procesar datos de temporadas completas instantáneamente?

---

**Próxima sesión**: Pandas - Hojas de cálculo inteligentes para manejar datasets complejos con nombres, fechas y múltiples tipos de datos.


# SESIÓN 2: ¿Cómo gestionas datos mixtos como nombres, fechas y estadísticas?
**(50 minutos)**

## Pregunta Central de la Sesión
**¿Te has preguntado cómo organizan los clubes información que incluye nombres de jugadores, fechas de partidos, equipos, posiciones Y estadísticas numéricas?**

### Tu situación actual
NumPy es perfecto para números, pero... ¿qué pasa cuando necesitas manejar:
- Nombres de jugadores (texto)
- Fechas de partidos 
- Posiciones (categorías)
- Equipos (texto)
- Goles y asistencias (números)

### Reflexión inicial
¿Cómo organizarías en una sola estructura datos tan diferentes entre sí?

### Analogía deportiva
**Piensa en esto**: ¿Cuál es la diferencia entre:
- Una calculadora (que solo maneja números) vs.
- Una hoja de cálculo completa (que maneja texto, fechas, números, fórmulas)?

**Pandas** es como Excel, pero programable y mil veces más potente.

---

## Descubriendo Pandas: Tu organizador inteligente

### ¿Qué hace especial a Pandas?
- Maneja cualquier tipo de dato: números, texto, fechas
- Organiza información en tablas inteligentes
- Permite filtros y búsquedas complejas
- Es la herramienta estándar para análisis de datos

### Primera pregunta práctica
¿Cómo crees que se vería una "tabla inteligente" con información completa de jugadores?

```python
# Tu primer contacto con tablas inteligentes
import pandas as pd
import numpy as np

print("Pandas importado exitosamente")
print(f"Versión: {pd.__version__}")

# ¿Cómo crees que podrías organizar información completa de jugadores?
print("\n=== CREANDO TU PRIMERA BASE DE DATOS DEPORTIVA ===")

# Información completa de jugadores del Real Madrid
datos_jugadores = {
    'nombre': ['Vinícius Jr', 'Benzema', 'Modrić', 'Courtois', 'Militão'],
    'posicion': ['Extremo', 'Delantero', 'Mediocampista', 'Portero', 'Defensa'],
    'edad': [23, 35, 37, 30, 25],
    'goles': [15, 18, 3, 0, 2],
    'asistencias': [8, 6, 12, 0, 1],
    'partidos': [28, 25, 30, 32, 26],
    'nacionalidad': ['Brasil', 'Francia', 'Croacia', 'Bélgica', 'Brasil']
}

# La magia de Pandas: crear una tabla inteligente
df_madrid = pd.DataFrame(datos_jugadores)

print("Tu primera base de datos profesional:")
print(df_madrid)
print(f"\nDimensiones: {df_madrid.shape} (filas, columnas)")

# ¿Qué información automática puedes obtener?
print(f"\nTipos de datos detectados automáticamente:")
print(df_madrid.dtypes)

# Reflexión: ¿Notas cómo Pandas maneja automáticamente texto y números?
```

## ¿Cómo exploras rápidamente miles de datos deportivos?

### Pregunta práctica
Si un director técnico recibe una base de datos con información de 500 jugadores, ¿cuáles serían las primeras preguntas que se haría?

### Tu situación como analista
Pandas tiene métodos integrados que responden automáticamente las preguntas más comunes sobre cualquier conjunto de datos.

### Reflexión
¿Qué tipo de información básica te gustaría conocer antes de analizar datos deportivos en profundidad?

```python
# Explorando el DataFrame - Métodos básicos de análisis
print("=== ANÁLISIS EXPLORATORIO BÁSICO ===")

# Información general del dataset
print("Primeras filas:")
print(df_madrid.head())
print()

print("Estadísticas descriptivas:")
print(df_madrid.describe())
print()

print("Información del DataFrame:")
print(df_madrid.info())
print()

# Accediendo a columnas específicas
print("=== ACCESO A DATOS ESPECÍFICOS ===")
print("Solo nombres de jugadores:")
print(df_madrid['nombre'].tolist())
print()

print("Goles y asistencias:")
print(df_madrid[['nombre', 'goles', 'asistencias']])
print()

# Creando nuevas columnas calculadas
print("=== CREANDO COLUMNAS CALCULADAS ===")
df_madrid['goles_por_partido'] = df_madrid['goles'] / df_madrid['partidos']
df_madrid['participaciones_gol'] = df_madrid['goles'] + df_madrid['asistencias']

print("DataFrame con nuevas columnas:")
print(df_madrid[['nombre', 'goles_por_partido', 'participaciones_gol']])
print()

# Ordenamiento
print("=== JUGADORES ORDENADOS POR PARTICIPACIONES EN GOL ===")
df_ordenado = df_madrid.sort_values('participaciones_gol', ascending=False)
print(df_ordenado[['nombre', 'posicion', 'participaciones_gol']])
```

## Filtrado y Agrupación - Análisis Avanzado

**Pregunta estratégica**: ¿Cómo encontrarías rápidamente a todos los jugadores brasileños que anotaron más de 10 goles?

Con Pandas puedes crear filtros complejos de manera muy intuitiva.

```python
# Filtrado avanzado de datos
print("=== FILTROS INTELIGENTES ===")

# Filtro simple: Jugadores con más de 10 goles
goleadores = df_madrid[df_madrid['goles'] > 10]
print("Jugadores con más de 10 goles:")
print(goleadores[['nombre', 'goles']])
print()

# Filtro múltiple: Brasileños con más de 5 goles
brasileños_goleadores = df_madrid[(df_madrid['nacionalidad'] == 'Brasil') & 
                                   (df_madrid['goles'] > 5)]
print("Brasileños goleadores:")
print(brasileños_goleadores[['nombre', 'goles', 'nacionalidad']])
print()

# Filtro por posición
atacantes = df_madrid[df_madrid['posicion'].isin(['Delantero', 'Extremo'])]
print("Jugadores ofensivos:")
print(atacantes[['nombre', 'posicion', 'participaciones_gol']])
print()

# Agrupación por nacionalidad
print("=== ANÁLISIS POR GRUPOS ===")
por_nacionalidad = df_madrid.groupby('nacionalidad').agg({
    'goles': 'sum',
    'asistencias': 'sum',
    'edad': 'mean'
}).round(1)

print("Estadísticas por nacionalidad:")
print(por_nacionalidad)
print()

# Agrupación por posición
por_posicion = df_madrid.groupby('posicion').agg({
    'goles': ['mean', 'sum'],
    'partidos': 'mean'
}).round(2)

print("Análisis por posición:")
print(por_posicion)
```

---

## Resumen de la Sesión 2 (50 minutos)

**¿Qué hemos aprendido sobre Pandas?**

### Conceptos Clave:
- **DataFrames**: Tablas inteligentes con múltiples tipos de datos
- **Exploración**: head(), describe(), info() para análisis rápido
- **Manipulación**: Crear columnas calculadas, ordenar datos
- **Filtrado**: Condiciones simples y complejas para encontrar datos específicos
- **Agrupación**: Análisis por categorías (nacionalidad, posición)

### Ventajas sobre NumPy:
- **Versatilidad**: Maneja texto, números, fechas simultáneamente
- **Etiquetas**: Columnas y filas con nombres descriptivos
- **Filtros intuitivos**: Búsquedas complejas con sintaxis simple
- **Agrupaciones**: Análisis automático por categorías

### Operaciones Fundamentales Aprendidas:
- Crear DataFrames desde diccionarios
- Acceder a columnas específicas
- Calcular nuevas columnas
- Filtrar con condiciones múltiples
- Agrupar y calcular estadísticas

**Pregunta para reflexionar**: ¿Cómo usarías Pandas para analizar datos de toda una liga con cientos de jugadores?

---

**Próxima sesión**: Proyecto integrador - Combinaremos NumPy y Pandas para crear un sistema completo de análisis de temporada futbolística.


# SESIÓN 3: ¿Cómo integras NumPy y Pandas en un sistema profesional?
**(50 minutos)**

## Pregunta Central de la Sesión
**¿Te has preguntado cómo combinan los analistas de clubes profesionales todas las herramientas que conoces para crear sistemas completos de análisis?**

### Tu evolución como analista
En estas 3 sesiones has aprendido:
- **NumPy**: Cálculos masivos instantáneos
- **Pandas**: Organización inteligente de datos complejos

### El desafío final
¿Cómo crearías un sistema que analice una temporada completa como lo hacen equipos como el Real Madrid o Barcelona?

### Tu misión profesional
Vas a combinar todo tu conocimiento para construir un sistema que:
- Procese datos de temporadas completas
- Genere tablas de posiciones automáticamente
- Calcule estadísticas avanzadas
- Produzca reportes ejecutivos

### Reflexión inicial
¿Qué información necesitaría un director técnico para evaluar el rendimiento de toda una temporada?

---

## Construyendo tu primer sistema de análisis profesional

### Pregunta estratégica
Si tuvieras acceso a todos los datos de La Liga, ¿qué análisis harías primero?

```python
# PROYECTO INTEGRADOR: Sistema Completo de Análisis de Temporada
import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

print("=== SISTEMA PROFESIONAL DE ANÁLISIS DE TEMPORADA ===")
print("Combinando NumPy + Pandas para análisis de nivel profesional")
print()

# ===============================
# GENERACIÓN DE DATASET REALISTA
# ===============================

def generar_temporada_completa(num_jornadas=38):
    """Genera un dataset completo de una temporada futbolística"""
    
    # Equipos de La Liga
    equipos = ['Real Madrid', 'Barcelona', 'Atletico Madrid', 'Sevilla', 
               'Valencia', 'Real Sociedad', 'Villarreal', 'Athletic Bilbao',
               'Real Betis', 'Osasuna', 'Celta', 'Rayo Vallecano',
               'Espanyol', 'Getafe', 'Mallorca', 'Cadiz', 'Granada', 'Almeria',
               'Valladolid', 'Elche']
    
    # Generar fechas de jornadas (cada semana)
    fecha_inicio = datetime(2024, 8, 15)
    fechas = [fecha_inicio + timedelta(weeks=i) for i in range(num_jornadas)]
    
    # Lista para almacenar todos los partidos
    partidos = []
    
    # Generar partidos para cada jornada
    for jornada in range(1, num_jornadas + 1):
        fecha = fechas[jornada - 1]
        
        # En cada jornada, cada equipo juega una vez
        equipos_disponibles = equipos.copy()
        random.shuffle(equipos_disponibles)
        
        # Crear 10 partidos por jornada (20 equipos / 2)
        for i in range(0, len(equipos_disponibles), 2):
            if i + 1 < len(equipos_disponibles):
                local = equipos_disponibles[i]
                visitante = equipos_disponibles[i + 1]
                
                # Generar resultado realista
                # Equipos top tienen mayor probabilidad de anotar más
                factor_local = 1.2 if local in equipos[:6] else 1.0
                factor_visitante = 1.0 if visitante in equipos[:6] else 0.9
                
                goles_local = np.random.poisson(1.4 * factor_local)
                goles_visitante = np.random.poisson(1.2 * factor_visitante)
                
                # Asegurar que no sean resultados extremos
                goles_local = min(goles_local, 5)
                goles_visitante = min(goles_visitante, 5)
                
                partidos.append({
                    'jornada': jornada,
                    'fecha': fecha.strftime('%Y-%m-%d'),
                    'equipo_local': local,
                    'equipo_visitante': visitante,
                    'goles_local': goles_local,
                    'goles_visitante': goles_visitante,
                    'total_goles': goles_local + goles_visitante
                })
    
    return pd.DataFrame(partidos)

# Generar dataset completo
print("Generando temporada completa de La Liga...")
df_temporada = generar_temporada_completa(20)  # 20 jornadas para el ejemplo
print(f"Dataset generado: {len(df_temporada)} partidos")
print()

# Mostrar primeros partidos
print("=== PRIMEROS PARTIDOS DE LA TEMPORADA ===")
print(df_temporada.head(10))
```

```python
# ===============================
# ANÁLISIS ESTADÍSTICO AVANZADO
# ===============================

def analizar_temporada_completa(df):
    """Análisis completo usando NumPy + Pandas"""
    
    print("=== ANÁLISIS GENERAL DE LA TEMPORADA ===")
    
    # Estadísticas básicas con NumPy
    goles_totales = df['total_goles'].values  # Convertir a array NumPy
    goles_locales = df['goles_local'].values
    goles_visitantes = df['goles_visitante'].values
    
    print(f"Total de partidos analizados: {len(df)}")
    print(f"Promedio de goles por partido: {np.mean(goles_totales):.2f}")
    print(f"Mediana de goles por partido: {np.median(goles_totales):.2f}")
    print(f"Desviación estándar: {np.std(goles_totales):.2f}")
    print(f"Partido con más goles: {np.max(goles_totales)}")
    print(f"Partido con menos goles: {np.min(goles_totales)}")
    print()
    
    # Análisis de ventaja local
    victorias_locales = np.sum(goles_locales > goles_visitantes)
    empates = np.sum(goles_locales == goles_visitantes)
    victorias_visitantes = np.sum(goles_locales < goles_visitantes)
    
    print("=== VENTAJA LOCAL ===")
    print(f"Victorias locales: {victorias_locales} ({victorias_locales/len(df)*100:.1f}%)")
    print(f"Empates: {empates} ({empates/len(df)*100:.1f}%)")
    print(f"Victorias visitantes: {victorias_visitantes} ({victorias_visitantes/len(df)*100:.1f}%)")
    print(f"Promedio goles local: {np.mean(goles_locales):.2f}")
    print(f"Promedio goles visitante: {np.mean(goles_visitantes):.2f}")
    print()
    
    # Análisis por jornadas con Pandas
    print("=== EVOLUCIÓN POR JORNADAS ===")
    analisis_jornadas = df.groupby('jornada').agg({
        'total_goles': ['mean', 'sum', 'std'],
        'goles_local': 'mean',
        'goles_visitante': 'mean'
    }).round(2)
    
    print("Estadísticas por jornada (primeras 10):")
    print(analisis_jornadas.head(10))
    print()
    
    return {
        'promedio_goles': np.mean(goles_totales),
        'total_goles_temporada': np.sum(goles_totales),
        'ventaja_local_pct': victorias_locales/len(df)*100,
        'jornadas_analizadas': analisis_jornadas
    }

# Ejecutar análisis completo
resultado_analisis = analizar_temporada_completa(df_temporada)
```

```python
# ===============================
# TABLA DE POSICIONES PROFESIONAL
# ===============================

def crear_tabla_posiciones(df):
    """Genera tabla de posiciones usando Pandas"""
    
    # Crear listas para almacenar resultados de cada equipo
    resultados_equipos = []
    
    # Obtener todos los equipos únicos
    equipos = pd.concat([df['equipo_local'], df['equipo_visitante']]).unique()
    
    for equipo in equipos:
        # Partidos como local
        partidos_local = df[df['equipo_local'] == equipo]
        # Partidos como visitante  
        partidos_visitante = df[df['equipo_visitante'] == equipo]
        
        # Estadísticas como local
        goles_favor_local = partidos_local['goles_local'].sum()
        goles_contra_local = partidos_local['goles_visitante'].sum()
        victorias_local = len(partidos_local[partidos_local['goles_local'] > partidos_local['goles_visitante']])
        empates_local = len(partidos_local[partidos_local['goles_local'] == partidos_local['goles_visitante']])
        derrotas_local = len(partidos_local[partidos_local['goles_local'] < partidos_local['goles_visitante']])
        
        # Estadísticas como visitante
        goles_favor_visitante = partidos_visitante['goles_visitante'].sum()
        goles_contra_visitante = partidos_visitante['goles_local'].sum()
        victorias_visitante = len(partidos_visitante[partidos_visitante['goles_visitante'] > partidos_visitante['goles_local']])
        empates_visitante = len(partidos_visitante[partidos_visitante['goles_visitante'] == partidos_visitante['goles_local']])
        derrotas_visitante = len(partidos_visitante[partidos_visitante['goles_visitante'] < partidos_visitante['goles_local']])
        
        # Totales
        partidos_jugados = len(partidos_local) + len(partidos_visitante)
        victorias = victorias_local + victorias_visitante
        empates = empates_local + empates_visitante
        derrotas = derrotas_local + derrotas_visitante
        goles_favor = goles_favor_local + goles_favor_visitante
        goles_contra = goles_contra_local + goles_contra_visitante
        diferencia_goles = goles_favor - goles_contra
        puntos = victorias * 3 + empates * 1
        
        resultados_equipos.append({
            'equipo': equipo,
            'partidos': partidos_jugados,
            'victorias': victorias,
            'empates': empates,
            'derrotas': derrotas,
            'goles_favor': goles_favor,
            'goles_contra': goles_contra,
            'diferencia_goles': diferencia_goles,
            'puntos': puntos
        })
    
    # Crear DataFrame y ordenar por puntos
    tabla = pd.DataFrame(resultados_equipos)
    tabla = tabla.sort_values(['puntos', 'diferencia_goles', 'goles_favor'], 
                              ascending=[False, False, False])
    tabla.reset_index(drop=True, inplace=True)
    tabla.index += 1  # Empezar posiciones desde 1
    
    return tabla

print("=== TABLA DE POSICIONES ACTUAL ===")
tabla_posiciones = crear_tabla_posiciones(df_temporada)
print(tabla_posiciones.head(10))
print()

# Análisis de tendencias con NumPy
print("=== ANÁLISIS DE TENDENCIAS ===")
top_5 = tabla_posiciones.head(5)
bottom_5 = tabla_posiciones.tail(5)

print("TOP 5 EQUIPOS:")
promedio_goles_top = np.mean(top_5['goles_favor'])
promedio_puntos_top = np.mean(top_5['puntos'])
print(f"Promedio goles favor: {promedio_goles_top:.1f}")
print(f"Promedio puntos: {promedio_puntos_top:.1f}")
print()

print("BOTTOM 5 EQUIPOS:")
promedio_goles_bottom = np.mean(bottom_5['goles_favor'])
promedio_puntos_bottom = np.mean(bottom_5['puntos'])
print(f"Promedio goles favor: {promedio_goles_bottom:.1f}")
print(f"Promedio puntos: {promedio_puntos_bottom:.1f}")
print()

print(f"Diferencia promedio goles: {promedio_goles_top - promedio_goles_bottom:.1f}")
print(f"Diferencia promedio puntos: {promedio_puntos_top - promedio_puntos_bottom:.1f}")
```

```python
# ===============================
# ANÁLISIS PREDICTIVO BÁSICO
# ===============================

def analisis_predictivo(df, tabla):
    """Predicciones básicas basadas en datos históricos"""
    
    print("=== ANÁLISIS PREDICTIVO ===")
    
    # Proyección final de puntos (extrapolando a 38 jornadas)
    jornadas_jugadas = df['jornada'].max()
    jornadas_totales = 38
    factor_proyeccion = jornadas_totales / jornadas_jugadas
    
    tabla_proyectada = tabla.copy()
    tabla_proyectada['puntos_proyectados'] = (tabla['puntos'] * factor_proyeccion).round(0).astype(int)
    tabla_proyectada['goles_proyectados'] = (tabla['goles_favor'] * factor_proyeccion).round(0).astype(int)
    
    print(f"Proyección final basada en {jornadas_jugadas} jornadas:")
    print(tabla_proyectada[['equipo', 'puntos', 'puntos_proyectados']].head(8))
    print()
    
    # Análisis de correlaciones con NumPy
    puntos = tabla['puntos'].values
    goles_favor = tabla['goles_favor'].values
    goles_contra = tabla['goles_contra'].values
    
    # Correlación entre goles favor y puntos
    correlacion_goles_puntos = np.corrcoef(goles_favor, puntos)[0, 1]
    correlacion_defensa_puntos = np.corrcoef(-goles_contra, puntos)[0, 1]  # Negativo porque menos goles contra es mejor
    
    print("=== FACTORES DE ÉXITO ===")
    print(f"Correlación goles favor - puntos: {correlacion_goles_puntos:.3f}")
    print(f"Correlación defensa - puntos: {correlacion_defensa_puntos:.3f}")
    
    if correlacion_goles_puntos > correlacion_defensa_puntos:
        print("Conclusión: El ataque es más determinante que la defensa")
    else:
        print("Conclusión: La defensa es más determinante que el ataque")
    
    return tabla_proyectada

# Ejecutar análisis predictivo
proyecciones = analisis_predictivo(df_temporada, tabla_posiciones)

print("\n" + "="*60)
print("=== REPORTE EJECUTIVO DE TEMPORADA ===")
print("="*60)

# Estadísticas clave
mejor_ataque = tabla_posiciones.loc[tabla_posiciones['goles_favor'].idxmax()]
mejor_defensa = tabla_posiciones.loc[tabla_posiciones['goles_contra'].idxmin()]
mas_goleados = tabla_posiciones.loc[tabla_posiciones['goles_contra'].idxmax()]

print(f"LÍDER: {tabla_posiciones.iloc[0]['equipo']} ({tabla_posiciones.iloc[0]['puntos']} puntos)")
print(f"MEJOR ATAQUE: {mejor_ataque['equipo']} ({mejor_ataque['goles_favor']} goles)")
print(f"MEJOR DEFENSA: {mejor_defensa['equipo']} ({mejor_defensa['goles_contra']} goles recibidos)")
print(f"MÁS GOLEADO: {mas_goleados['equipo']} ({mas_goleados['goles_contra']} goles recibidos)")
print()

print(f"PROMEDIO GOLES/PARTIDO: {resultado_analisis['promedio_goles']:.2f}")
print(f"VENTAJA LOCAL: {resultado_analisis['ventaja_local_pct']:.1f}%")
print(f"TOTAL GOLES TEMPORADA: {resultado_analisis['total_goles_temporada']}")

print("\n" + "="*60)
```

<!-- #region -->
### Actividad Final: Personaliza el Análisis

**Tiempo estimado: 15 minutos**

**Tu desafío**: Modifica el sistema para analizar aspectos específicos que te interesen.

**Opciones de personalización**:
1. **Análisis de rivalidades**: Filtra partidos entre equipos específicos
2. **Rendimiento por mes**: Agrupa datos por período temporal
3. **Análisis de localía**: Compara rendimiento local vs visitante por equipo
4. **Estadísticas extremas**: Encuentra patrones en resultados inusuales

**Preguntas para explorar**:
- ¿Qué equipo tiene mejor rendimiento como visitante?
- ¿En qué jornadas se anotan más goles?
- ¿Cuál es la diferencia de goles promedio en clásicos vs otros partidos?

**Código base para empezar**:
```python
# Ejemplo: Análisis de rendimiento visitante
rendimiento_visitante = df_temporada.groupby('equipo_visitante').agg({
    'goles_visitante': 'mean',
    'goles_local': 'mean'
}).round(2)

# Tu análisis personalizado aquí
```

---

## Resumen de la Semana 4 Completa

**¿Qué sistema profesional hemos construido en estas 3 sesiones?**

### Sesión 1: NumPy - Poder Computacional
- Arrays para cálculos masivos instantáneos
- Operaciones vectorizadas con miles de datos
- Matrices multidimensionales para análisis complejos
- Estadísticas avanzadas integradas

### Sesión 2: Pandas - Manejo de Datos
- DataFrames para datasets complejos
- Filtrado y agrupación inteligente
- Manipulación de datos estructurados
- Análisis exploratorio profesional

### Sesión 3: Sistema Integrado
- Generación de datasets realistas
- Análisis estadístico completo
- Tabla de posiciones automática
- Predicciones basadas en datos
- Reportes ejecutivos profesionales

### Logros Alcanzados:
**Has creado un sistema que puede**:
- Procesar temporadas completas instantáneamente
- Generar tablas de posiciones automáticamente
- Calcular estadísticas avanzadas con precisión científica
- Hacer proyecciones y predicciones básicas
- Producir reportes de calidad profesional

### Transformación de Capacidades:
**De herramientas básicas a sistema profesional**:
- **Antes**: Listas y cálculos manuales uno por uno
- **Ahora**: Análisis masivo de miles de datos simultáneamente
- **Antes**: Operaciones repetitivas y propensas a errores
- **Ahora**: Automatización completa con precisión científica
- **Antes**: Datos simples sin estructura
- **Ahora**: Datasets complejos con múltiples dimensiones

### Habilidades Profesionales Desarrolladas:
- **Análisis de datos masivos**: Como analistas de clubes profesionales
- **Visualización estadística**: Comprensión de patrones y tendencias
- **Pensamiento científico**: Correlaciones y predicciones basadas en datos
- **Automatización**: Sistemas que funcionan con cualquier dataset

**Pregunta de reflexión**: ¿Cómo has evolucionado de programador básico a analista de datos profesional?

---

**Próxima semana**: Visualización básica - Aprenderemos a crear gráficos y visualizaciones que conviertan nuestros análisis en insights comprensibles y presentaciones impactantes.

**¡Felicitaciones por dominar las herramientas fundamentales de la ciencia de datos aplicada al fútbol!**
<!-- #endregion -->

### 2.2 Creación de Arrays Básicos - ¿Qué son estos "súper listas"?

**Pregunta de evolución**: ¿Recuerdas las listas normales de Python? ¿Qué limitaciones tenían para cálculos matemáticos masivos?

**Descubrimiento**: Los **arrays de NumPy** son como listas optimizadas para matemáticas. ¿Cómo crees que serían diferentes?

```python
# ¿Cómo creas arrays de NumPy y qué los hace especiales?
# Empecemos con datos deportivos reales

print("=== ARRAYS DESDE LISTAS ===")

# ¿Cómo convertirías una lista normal en un array de NumPy?
goles_favor = np.array([2, 1, 3, 0, 2, 1, 4, 2, 1, 3])  # 10 partidos
print(f"Goles a favor: {goles_favor}")
print(f"Tipo de dato: {type(goles_favor)}")  # ¿Diferente de una lista?
print(f"Forma del array: {goles_favor.shape}")  # ¿Qué información da esto?

# ¿Cómo manejarías datos relacionados?
goles_contra = np.array([1, 1, 2, 1, 0, 2, 1, 1, 2, 0])
print(f"Goles en contra: {goles_contra}")

print("\n=== INFORMACIÓN DEL ARRAY ===")
print(f"Número de elementos: {goles_favor.size}")  # ¿Total de datos?
print(f"Número de dimensiones: {goles_favor.ndim}")  # ¿1D, 2D, 3D?
print(f"Tipo de datos: {goles_favor.dtype}")  # ¿Optimizado para números?

print("\n=== ARRAYS ESPECIALES ===")

# ¿Cómo crearías arrays pre-llenados para inicializar datos?
temporada_nueva = np.zeros(38)  # ¿38 partidos de temporada?
print(f"Nueva temporada (38 partidos): {temporada_nueva[:5]}...")  # ¿Solo primeros 5?

# ¿Y si quisieras marcar partidos jugados?
partidos_jugados = np.ones(10)  # ¿Todos con valor 1?
print(f"Partidos jugados: {partidos_jugados}")

# ¿Cómo generarías secuencias automáticamente?
jornadas = np.arange(1, 11)  # ¿Del 1 al 10?
print(f"Números de jornada: {jornadas}")

# ¿Y si necesitas divisiones exactas en un rango?
minutos = np.linspace(0, 90, 19)  # ¿19 puntos exactos entre 0 y 90?
print(f"Marcas de tiempo: {minutos[:5]}...")  # ¿Primeros 5?

# Pregunta de comparación: ¿Qué ventajas ves de estos arrays sobre las listas normales?
```

### 2.3 Operaciones Matemáticas con Arrays - ¿Cómo calculas con "súper poderes"?

**Pregunta de eficiencia**: Anteriormente, para sumar dos listas tenías que usar bucles. ¿Qué pasaría si pudieras operar arrays completos como si fueran números individuales?

**Desafío conceptual**: ¿Cómo crees que NumPy maneja operaciones en cientos o miles de elementos simultáneamente?

```python
# ¿Cómo realizas operaciones matemáticas instantáneas en arrays completos?
# Esta es la verdadera potencia de NumPy

print("=== OPERACIONES BÁSICAS ===")

# ¿Recuerdas estos datos del ejemplo anterior?
print(f"Goles a favor: {goles_favor}")
print(f"Goles en contra: {goles_contra}")

# ¿Cómo calcularías la diferencia de goles para TODOS los partidos de una vez?
diferencia_goles = goles_favor - goles_contra  # ¡Sin bucles!
print(f"Diferencia por partido: {diferencia_goles}")

# ¿Y el total de goles en cada partido?
total_goles = goles_favor + goles_contra  # ¡Operación vectorizada!
print(f"Total goles por partido: {total_goles}")

# ¿Cómo calcularías puntos usando lógica compleja en todo el array?
puntos = np.where(diferencia_goles > 0, 3,    # ¿Si ganó: 3 puntos?
                 np.where(diferencia_goles == 0, 1, 0))  # ¿Si empató: 1, si perdió: 0?
print(f"Puntos por partido: {puntos}")

# Pregunta de impacto: ¿Notas que no usamos ningún bucle? ¿Qué significa esto para el rendimiento?
```

## 3. Introducción a Pandas: ¿Tu hoja de cálculo con súper poderes?

### Pregunta de transición: ¿Qué pasa cuando tus datos son más complejos?

**Reflexión**: NumPy es excelente para números, pero ¿qué sucede cuando necesitas manejar nombres de jugadores, fechas de partidos, posiciones, equipos, etc., todo mezclado?

**Analogía práctica**: ¿Alguna vez has usado Excel? ¿Cómo organizarías información compleja de jugadores en filas y columnas?

### 3.1 Series - ¿Columnas inteligentes de datos?

**Pregunta conceptual**: ¿Qué pasaría si una lista pudiera tener "etiquetas" descriptivas en lugar de solo números de posición?

**Descubrimiento**: Una **Serie** es como una columna de Excel, pero con indexación personalizada. ¿Para qué datos deportivos sería útil esto?

```python
# ¿Cómo crees que representa Pandas los goles de diferentes jugadores?
# Experimenta con este ejemplo y observa:

import pandas as pd

# ¿Qué diferencias notas comparado con un array de NumPy?
goles_jugadores = pd.Series([23, 19, 15, 31, 8], 
                           index=['Messi', 'Ronaldo', 'Mbappé', 'Haaland', 'Modrić'])

print("Serie de goles por jugador:")
print(goles_jugadores)
print()

# Pregunta: ¿Cómo crees que accedes a los goles de Messi?
print("Goles de Messi:", goles_jugadores['Messi'])

# Reflexión: ¿Qué ventaja tiene esto sobre usar posiciones numéricas [0], [1], etc.?
```

### 3.2 DataFrames - ¿Múltiples Series trabajando juntas?

**Pregunta provocadora**: Si una Serie es una columna, ¿qué obtendrías al juntar varias columnas relacionadas?

**Analogía práctica**: ¿Cómo organiza un entrenador la información de todos sus jugadores? Piensa en nombre, posición, edad, goles, asistencias...

**Descubrimiento**: Un DataFrame es como una hoja de cálculo completa, donde cada columna es una Serie.

**Reflexión**: ¿Para qué tipo de análisis deportivo sería útil tener toda esta información organizada?

```python
# ¿Cómo crees que organizarías información completa de varios jugadores?
# Experimenta con este ejemplo:

# Datos de ejemplo para explorar
datos_jugadores = {
    'Nombre': ['Messi', 'Ronaldo', 'Mbappé', 'Haaland', 'Modrić'],
    'Edad': [36, 39, 25, 23, 38],
    'Posición': ['Delantero', 'Delantero', 'Delantero', 'Delantero', 'Centrocampista'],
    'Goles': [23, 19, 15, 31, 8],
    'Asistencias': [15, 8, 12, 5, 10]
}

# ¿Qué estructura crees que creará Pandas?
df_jugadores = pd.DataFrame(datos_jugadores)

print("DataFrame de jugadores:")
print(df_jugadores)
print()

# Pregunta: ¿Cómo crees que accederías solo a la columna de goles?
print("Solo los goles:")
print(df_jugadores['Goles'])

# Reflexión: ¿Qué ventajas ves en esta organización de datos?
```

## 4. Operaciones Básicas con DataFrames - ¿Qué puedes descubrir de tus datos?

### Pregunta exploratoria: ¿Cómo investigaría un entrenador su plantel?

**Contexto**: Tienes un DataFrame con información de jugadores. ¿Qué serían las primeras preguntas que te harías?

**Hipótesis**: ¿Crees que será fácil obtener estadísticas básicas como promedios, máximos, mínimos?

### 4.1 Primeras preguntas sobre los datos

**Investigación inicial**: ¿Cuáles serían las primeras cosas que querrías saber sobre un conjunto de datos deportivos?

```python
# ¿Qué información básica crees que puedes extraer fácilmente?
# Experimenta con estos métodos y observa los resultados:

# Pregunta 1: ¿Cómo ves las primeras filas?
print("Primeras 3 filas:")
print(df_jugadores.head(3))
print()

# Pregunta 2: ¿Cómo obtienes información general sobre la estructura?
print("Información del DataFrame:")
print(df_jugadores.info())
print()

# Pregunta 3: ¿Cómo calculas estadísticas básicas de todas las columnas numéricas?
print("Estadísticas descriptivas:")
print(df_jugadores.describe())
print()

# Reflexión: ¿Qué insights puedes obtener de estas estadísticas básicas?
# ¿Qué te dice el promedio de edad? ¿Y el máximo de goles?
```

### 4.2 Filtrado de Datos - ¿Cómo encontrar exactamente lo que buscas?

**Pregunta práctica**: Un entrenador quiere analizar solo jugadores con más de 20 goles. ¿Cómo crees que puede filtrar esta información?

**Analogía**: Es como usar filtros en una búsqueda de internet. ¿Qué tipos de filtros serían útiles para datos deportivos?

**Predicción**: ¿Crees que será similar a las condiciones que aprendiste con if/else?

```python
# ¿Cómo crees que puedes filtrar jugadores con más de 20 goles?
# Experimenta con estas técnicas:

# Método 1: ¿Qué crees que hace esta línea?
jugadores_goleadores = df_jugadores[df_jugadores['Goles'] > 20]
print("Jugadores con más de 20 goles:")
print(jugadores_goleadores)
print()

# Método 2: ¿Y si quieres jugadores jóvenes (menores de 30)?
jugadores_jovenes = df_jugadores[df_jugadores['Edad'] < 30]
print("Jugadores menores de 30 años:")
print(jugadores_jovenes)
print()

# Desafío: ¿Cómo combinarías ambas condiciones?
# ¿Qué símbolo crees que usarías para "Y" lógico?
jovenes_goleadores = df_jugadores[(df_jugadores['Edad'] < 30) & (df_jugadores['Goles'] > 15)]
print("Jugadores jóvenes Y goleadores:")
print(jovenes_goleadores)

# Reflexión: ¿Qué otros filtros serían útiles en análisis deportivo?
```

## 5. Comparación: NumPy vs Pandas - ¿Cuándo usar cada herramienta?

### Pregunta estratégica: ¿Son competidores o compañeros de equipo?

**Reflexión práctica**: Después de experimentar con ambas herramientas, ¿cuándo elegirías cada una?

**Analogía deportiva**: ¿Es como elegir entre diferentes tipos de jugadores para diferentes situaciones en el campo?

### Tu análisis como científico de datos

**Pregunta final**: Basándote en lo que has experimentado, ¿qué ventajas y desventajas ves en cada herramienta?

```python
# Reflexiona sobre esta comparación mientras experimentas:

print("=== COMPARACIÓN: ¿Cuándo usar cada herramienta? ===")
print()

# NumPy - ¿Para qué tipo de datos es ideal?
print("NumPy - Tu calculadora súper rápida:")
print("✓ Ideal para: Cálculos numéricos puros")
print("✓ Ejemplo: Análisis de velocidades, distancias, estadísticas simples")
print("✓ Ventaja: Velocidad extrema en operaciones matemáticas")
print()

# Pandas - ¿Para qué situaciones es mejor?
print("Pandas - Tu organizador inteligente de datos:")
print("✓ Ideal para: Datos mixtos (números, texto, fechas)")
print("✓ Ejemplo: Información completa de jugadores, resultados de partidos")
print("✓ Ventaja: Manejo de datos complejos y análisis exploratorio")
print()

# Pregunta de síntesis: ¿En qué proyectos deportivos usarías cada uno?
print("PREGUNTA FINAL:")
print("¿Para analizar qué aspectos del fútbol usarías NumPy?")
print("¿Para analizar qué aspectos del fútbol usarías Pandas?")

# Tu turno de reflexionar...
```

### Resumen de tu evolución esta semana

**¿Qué has descubierto sobre el análisis profesional de datos?**

### Tu transformación como analista
**Sesión 1**: Descubriste el poder de NumPy para cálculos masivos
- Comprendiste por qué los arrays son superiores a las listas
- Experimentaste operaciones simultáneas en miles de datos
- Organizaste información multidimensional automáticamente

**Sesión 2**: Dominaste Pandas para datos complejos
- Aprendiste a manejar información mixta (texto, números, fechas)
- Desarrollaste habilidades de filtrado y búsqueda avanzada
- Creaste análisis exploratorios profesionales

**Sesión 3**: Construiste un sistema integrado
- Combinaste NumPy y Pandas de forma profesional
- Generaste análisis automáticos de temporadas completas
- Produjiste reportes de calidad ejecutiva

### Tu nueva capacidad profesional
**Has evolucionado de programador básico a analista de datos**:
- **Antes**: Calculabas promedios uno por uno
- **Ahora**: Procesas temporadas completas instantáneamente
- **Antes**: Manejabas datos simples en listas
- **Ahora**: Organizas información compleja en sistemas integrados
- **Antes**: Hacías análisis básicos manualmente
- **Ahora**: Automatizas análisis de nivel profesional

### Reflexión final
¿Cómo aplicarías estos conocimientos para analizar tu equipo favorito o crear tu propio sistema de scouting?

### Conexión con la próxima semana
**Pregunta anticipatoria**: ¿Cómo crees que podrías convertir todos estos números y análisis en gráficos y visualizaciones que sean fáciles de entender?

**Próxima semana**: Visualización básica - Aprenderás a crear gráficos profesionales que conviertan tus análisis en insights visuales impactantes.

---

**¡Has completado tu transformación en analista de datos profesional para el fútbol!**
