# Caso Práctico Colaborativo - Bloque 2
## Análisis Básico de Jugadores de Fútbol

**Modalidad:** Colaborativa (equipos de 2-3 estudiantes)  
**Ponderación:** 15% del 2do Parcial  
**Duración:** 1 semana  
**Entrega:** Notebook de Jupyter + presentación simple

---

## Contexto del Problema

Tu equipo trabaja como analistas junior para una escuela de fútbol que quiere conocer mejor a sus jugadores. Tienen datos básicos de jugadores de diferentes equipos y necesitan crear un análisis simple para entender quiénes son los mejores.

**Situación:** La escuela tiene información básica de jugadores (goles, asistencias, edad, posición) y quiere saber qué jugadores destacan más en cada posición.

---

## Objetivos de Aprendizaje

Al completar este caso práctico, los estudiantes serán capaces de:
- Cargar y explorar datos de jugadores usando pandas
- Crear gráficos básicos con seaborn y matplotlib
- Calcular estadísticas simples (promedio, máximo, mínimo)
- Comparar rendimiento entre posiciones
- Presentar resultados de forma clara

---

## Dataset Proporcionado

### Dataset Principal: `jugadores_liga_juvenil.csv`
**Versión simplificada con solo las columnas esenciales**
```csv
jugador_id,nombre,edad,equipo,posicion,torneo,goles,asistencias,partidos_jugados
1,Alejandro Martínez,17,Atlas Sub-20,Delantero,Liga MX Sub-20,12,5,18
2,Sofia Hernández,16,Chivas Femenil,Mediocampo,Liga MX Femenil Sub-18,3,18,20
3,Diego Ramírez,18,América Sub-20,Delantero,Liga MX Sub-20,15,3,19
4,Camila Torres,17,Tigres Femenil,Defensa,Liga MX Femenil Sub-18,1,4,22
...
```

**Descripción de columnas:**
- `jugador_id`: Número único del jugador
- `nombre`: Nombre completo del jugador
- `edad`: Edad en años (16-18)
- `equipo`: Equipo al que pertenece
- `posicion`: Posición en el campo (Delantero, Mediocampo, Defensa, Portero)
- `torneo`: Liga MX Sub-20 o Liga MX Femenil Sub-18
- `goles`: Cantidad total de goles marcados
- `asistencias`: Cantidad total de asistencias dadas
- `partidos_jugados`: Número de partidos que ha jugado

---

## Tareas Requeridas

### Parte 1: Exploración Básica de Datos (40 puntos)

#### 1.1 Cargar los Datos (10 puntos)

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración obligatoria de seaborn
sns.set_theme(style="whitegrid", palette="viridis")

# Cargar el dataset simplificado
datos_jugadores = pd.read_csv('jugadores_liga_juvenil.csv')
print("¡Datos cargados correctamente!")
```

#### 1.2 Explorar la Información Básica (15 puntos)

**Lo que deben hacer:**

- Ver las primeras filas con `.head()`
- Contar cuántos jugadores hay por posición con `.value_counts()`
- Calcular estadísticas básicas con `.mean()`, `.max()`, `.min()`
- Identificar quién es el mejor goleador

**Ejemplo de código:**
```python
# Información básica
print(f"Tenemos {len(datos_jugadores)} jugadores")
print(f"Columnas disponibles: {list(datos_jugadores.columns)}")

# Jugadores por posición  
print(datos_jugadores['posicion'].value_counts())

# Estadísticas básicas de goles
print(f"Promedio de goles: {datos_jugadores['goles'].mean():.1f}")
print(f"Máximo de goles: {datos_jugadores['goles'].max()}")
```

#### 1.3 Crear Gráficos Básicos (15 puntos)

**Gráficos obligatorios:**

- Gráfico de barras: jugadores por posición
- Gráfico de cajas: goles por posición  
- Gráfico de dispersión: goles vs asistencias

### Parte 2: Análisis por Posición (30 puntos)

#### 2.1 Calcular Estadísticas por Posición (15 puntos)

**Lo que deben hacer:**

- Usar `.groupby()` para agrupar por posición
- Calcular promedios de goles y asistencias
- Encontrar el mejor jugador de cada posición

**Ejemplo de código:**
```python
# Estadísticas por posición
estadisticas_posicion = datos_jugadores.groupby('posicion').agg({
    'goles': 'mean',
    'asistencias': 'mean', 
    'partidos_jugados': 'mean'
}).round(1)

print("Promedios por posición:")
print(estadisticas_posicion)

# Mejor jugador por posición
for posicion in datos_jugadores['posicion'].unique():
    jugadores_posicion = datos_jugadores[datos_jugadores['posicion'] == posicion]
    mejor_jugador = jugadores_posicion.loc[jugadores_posicion['goles'].idxmax()]
    print(f"{posicion}: {mejor_jugador['nombre']} con {mejor_jugador['goles']} goles")
```

#### 2.2 Crear Más Visualizaciones (15 puntos)

**Gráficos adicionales:**

- Top 5 goleadores con gráfico de barras horizontal
- Comparación de goles vs asistencias por posición
- Distribución de edades

### Parte 3: Presentación de Resultados (30 puntos)

#### 3.1 Conclusiones Escritas (15 puntos)

**Deben responder estas preguntas:**

1. ¿Qué posición marca más goles en promedio?
2. ¿Quiénes son los 3 mejores goleadores?
3. ¿Hay algún patrón entre goles y asistencias?
4. ¿Cuál es la edad promedio por posición?

#### 3.2 Presentación Final (15 puntos)

**Crear una presentación simple con:**

- 3-4 diapositivas máximo
- Sus gráficos más importantes
- Conclusiones principales
- Lo que aprendieron del análisis

**Formato sugerido:**
- Diapositiva 1: ¿Qué analizamos?
- Diapositiva 2: Gráficos principales  
- Diapositiva 3: ¿Qué descubrimos?
- Diapositiva 4: Conclusiones

---

## Entregables

### 1. Notebook Principal (`analisis_jugadores_equipo[X].ipynb`)

**Debe incluir:**
- Importaciones y carga de datos
- Exploración básica (`.head()`, `.info()`, estadísticas)
- Gráficos obligatorios bien etiquetados
- Análisis por posición
- Conclusiones escritas

### 2. Presentación (`presentacion_equipo[X].pdf`)

**Debe incluir:**
- 3-4 diapositivas con sus mejores gráficos
- Conclusiones principales  
- Lo que aprendió cada integrante del equipo

---

## Criterios de Evaluación

### Rúbrica Simplificada (100 puntos total)

| Criterio | Puntos | ¿Qué evalúo? |
|----------|---------|--------------|
| **Exploración de Datos** | 40 | ¿Cargaron bien los datos? ¿Usaron `.head()`, `.info()`, estadísticas básicas? |
| **Análisis por Posición** | 30 | ¿Usaron `.groupby()` correctamente? ¿Encontraron el mejor jugador por posición? |
| **Visualizaciones** | 20 | ¿Crearon los 3 gráficos obligatorios? ¿Tienen títulos y etiquetas claras? |
| **Presentación** | 10 | ¿Su presentación es clara? ¿Respondieron las preguntas principales? |

### Lo que Busco en Cada Parte

#### Parte 1 - Exploración (40 puntos)

- **Excelente (36-40):** Código funciona sin errores, usan todas las funciones pedidas
- **Bueno (32-35):** Código funciona, pequeños errores menores
- **Suficiente (28-31):** Código funciona pero falta alguna función importante  
- **Insuficiente (<28):** Errores graves o código no funciona

#### Parte 2 - Análisis (30 puntos)

- **Excelente (27-30):** Usan `.groupby()` correctamente, encuentran mejores jugadores
- **Bueno (24-26):** Análisis correcto con pequeños errores
- **Suficiente (21-23):** Análisis básico pero incompleto
- **Insuficiente (<21):** No logran hacer el análisis por posición

---

## Cronograma de la Semana

| Día | ¿Qué hacer? | Tiempo |
|-----|-------------|--------|
| **Lunes** | Formar equipos, cargar y explorar datos básicos | 2 horas |
| **Miércoles** | Crear gráficos básicos, análisis por posición | 2 horas |
| **Viernes** | Preparar presentación y entregar | 1 hora |

---

## Consejos para el Equipo

### Para Dividir el Trabajo:

**Opción 1:** Por partes
- Persona 1: Exploración básica y carga de datos
- Persona 2: Gráficos y visualizaciones
- Persona 3: Análisis por posición y presentación

**Opción 2:** Todos juntos
- Trabajan todos en la misma computadora
- Van rotando quién escribe el código
- Todos participan en las decisiones

### Tips Importantes:

- **Usen variables en español:** `datos_jugadores`, `goleadores_top`
- **Pongan títulos descriptivos a los gráficos**
- **Comenten su código para explicar qué hace**
- **Prueben que todo funciona antes de entregar**

---

*¡Este caso práctico les ayudará a aplicar lo aprendido sobre pandas, seaborn y análisis básico de datos con un contexto divertido de fútbol!*