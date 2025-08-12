# Caso Práctico Colaborativo - Bloque 2

## Análisis Básico, Calidad de Datos e Interpretación de Rendimiento de Jugadores

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

La estructura se reorganiza para alinear con los contenidos reales de las semanas 6–10 e incorporar calidad de datos, estadística descriptiva completa, métricas derivadas e interpretación progresiva. Se integra el enfoque socrático (preguntas para guiar el razonamiento) y se estandariza la rúbrica 40/30/30.

### Parte 1: Exploración y Calidad de Datos (40 puntos)

#### 1.1 Cargar los Datos (5 puntos)

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

Preguntas socráticas iniciales:

- ¿Por qué cargar los datos con pandas y no con otro método manual?
- ¿Qué pasaría si el archivo tuviera una columna adicional no documentada?

#### 1.2 Exploración Estructural Básica (10 puntos)

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

Preguntas socráticas de exploración:

- ¿Qué indica el número de columnas sobre la complejidad del dataset?
- ¿Hay columnas categóricas que convenga convertir a categoría más adelante?

#### 1.3 Calidad y Tipos de Datos (10 puntos)

Objetivo: Verificar tipos, valores faltantes e inconsistencias simples.

Lo que deben hacer:

- Mostrar `datos_jugadores.info()`
- Revisar tipos de datos (`datos_jugadores.dtypes`)
- Contar valores faltantes (`datos_jugadores.isna().sum()`)
- Comprobar rangos básicos (edad 15–20, goles >= 0) mediante condiciones simples

Ejemplo de código:

```python
print("Información estructural:")
print(datos_jugadores.info())
print("Tipos de datos:")
print(datos_jugadores.dtypes)
print("Valores faltantes por columna:")
print(datos_jugadores.isna().sum())

# Comprobaciones de rangos sencillas
edades_invalidas = datos_jugadores[~datos_jugadores['edad'].between(15, 20)]
if len(edades_invalidas) > 0:
    print("Advertencia: edades fuera de rango esperado:")
    print(edades_invalidas[['nombre','edad']])
```

Preguntas socráticas:

- ¿Qué implicaría encontrar valores faltantes en goles?
- Si una columna numérica aparece como `object`, ¿qué riesgo trae para los cálculos?

#### 1.4 Estadística Descriptiva Inicial (15 puntos)

Objetivo: Ir más allá de media y máximo para incluir mediana y dispersión.

Lo que deben hacer:

- Usar `.describe()` para visión general
- Calcular media, mediana y desviación estándar de goles y asistencias
- Reflexionar sobre diferencias media vs mediana

Ejemplo de código:

```python
resumen_numerico = datos_jugadores[['goles','asistencias','partidos_jugados']].describe()
print(resumen_numerico)

import numpy as np
estadisticas_extra = datos_jugadores[['goles','asistencias']].agg(['mean','median','std']).T
print("Estadísticas complementarias:\n", estadisticas_extra)

print("¿Difieren media y mediana de goles? ¿Qué sugiere sobre valores extremos?")
```

Preguntas socráticas:

- ¿Qué nos dice una desviación estándar alta en asistencias?
- ¿Por qué podría ser más robusta la mediana que la media en goles?

### Parte 2: Análisis y Métricas Derivadas (30 puntos)

#### 2.1 Estadísticas por Posición (12 puntos)

Lo que deben hacer:

- Usar `.groupby('posicion')` y `agg` con media de goles, asistencias y partidos
- Identificar mejor jugador por posición (máximo de goles)
- Redondear a 1 decimal

Ejemplo de código (base recomendado):

```python
estadisticas_posicion = datos_jugadores.groupby('posicion').agg({
    'goles': 'mean',
    'asistencias': 'mean',
    'partidos_jugados': 'mean'
}).round(1)
print("Promedios por posición:\n", estadisticas_posicion)

for pos in datos_jugadores['posicion'].unique():
    subset = datos_jugadores[datos_jugadores['posicion'] == pos]
    mejor = subset.loc[subset['goles'].idxmax()]
    print(f"{pos}: {mejor['nombre']} con {mejor['goles']} goles")
```

Preguntas socráticas:

- ¿Por qué comparar promedios por posición antes de elegir titulares?
- ¿Qué riesgo hay si solo miramos el máximo de goles y no el promedio del rol?

#### 2.2 Métricas Derivadas de Eficiencia (10 puntos)

Objetivo: Incorporar variables interpretables para decisiones deportivas.

Lo que deben hacer:

- Crear `goles_por_partido = goles / partidos_jugados`
- Crear `contribucion_ofensiva = goles + asistencias`
- Calcular promedios de estas métricas por posición
- Identificar el top 3 por contribución ofensiva total

Ejemplo:

```python
datos_jugadores['goles_por_partido'] = (datos_jugadores['goles'] / datos_jugadores['partidos_jugados']).round(2)
datos_jugadores['contribucion_ofensiva'] = datos_jugadores['goles'] + datos_jugadores['asistencias']

promedios_eficiencia = datos_jugadores.groupby('posicion')[['goles_por_partido','contribucion_ofensiva']].mean().round(2)
print(promedios_eficiencia)

top_contribucion = datos_jugadores.sort_values('contribucion_ofensiva', ascending=False).head(3)
print("Top 3 por contribución ofensiva:")
print(top_contribucion[['nombre','posicion','contribucion_ofensiva']])
```

Preguntas socráticas:

- ¿Por qué `goles_por_partido` puede ser mejor que solo goles totales?
- ¿Cuándo podría engañarnos la contribución ofensiva (ej. pocos partidos)?

#### 2.3 Detección Simple de Valores Atípicos (Outliers) (8 puntos)

Objetivo: Reconocer valores extremos básicos que pueden distorsionar conclusiones.

Lo que deben hacer:

- Calcular media y desviación estándar de goles
- Definir umbral: `media + 2 * std`
- Listar jugadores por encima de ese umbral
- Decidir (justificación escrita) si mantenerlos en el análisis

Ejemplo:

```python
media_g = datos_jugadores['goles'].mean()
std_g = datos_jugadores['goles'].std()
umbral = media_g + 2*std_g
outliers_goles = datos_jugadores[datos_jugadores['goles'] > umbral]
print(f"Umbral outlier goles: {umbral:.1f}")
print(outliers_goles[['nombre','goles','posicion']])
```

Preguntas socráticas:

- ¿Eliminarías un delantero muy por encima del umbral? ¿Por qué?
- ¿Cómo afectaría mantenerlo al promedio de su posición?

### Parte 3: Visualización, Interpretación y Comunicación (30 puntos)

#### 3.1 Gráficos Fundamentales (10 puntos)

Gráficos obligatorios (cada uno con título claro, ejes etiquetados, fuente de datos opcional en nota):

- Barras: jugadores por posición (ordenado de mayor a menor)
- Caja: distribución de goles por posición (identificar variabilidad)
- Dispersión: goles vs asistencias (distinguir posición con color)

Preguntas socráticas (después de cada gráfico):

- ¿Qué posición domina en cantidad de jugadores? ¿Eso explica algo de sus promedios?
- ¿Qué posición muestra mayor dispersión en goles? ¿Por qué podría suceder?
- ¿Observas relación entre goles y asistencias o roles diferenciados?

#### 3.2 Visualizaciones de Profundización (10 puntos)

Gráficos adicionales:

- Top 5 goleadores (barras horizontal) con valores anotados
- Comparación de `goles_por_partido` vs `contribucion_ofensiva` (scatter o barras agrupadas)
- Distribución de edades (histograma o KDE simple)

Preguntas socráticas:

- ¿El top 5 por goles coincide con el top 3 por contribución ofensiva?
- ¿Hay posiciones con jugadores jóvenes y alta eficiencia? ¿Qué implicaría para desarrollo?
- ¿La distribución de edades es equilibrada o sesgada?

#### 3.3 Síntesis y Presentación (10 puntos)

Debe incluir respuestas claras y justificadas a:

1. ¿Qué posición marca más goles en promedio y qué tan consistente es (variabilidad)?
2. ¿Quiénes son los 3 jugadores más valiosos considerando contribución ofensiva y eficiencia?
3. ¿Qué patrón observas entre goles y asistencias? (rol de creadores vs finalizadores)
4. ¿La edad promedio por posición sugiere etapas de desarrollo distintas?
5. ¿Qué decisión práctica recomendarías al entrenador (ej. reforzar mediocampo, promover un delantero)?

Formato sugerido de presentación (3–4 diapositivas):

- Diapositiva 1: Objetivo y dataset
- Diapositiva 2: Métricas clave y gráficos principales
- Diapositiva 3: Interpretaciones y outliers (decisión)
- Diapositiva 4 (opcional si cabe): Recomendaciones y próximos pasos

---

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

## Criterios de Evaluación (Rúbrica Completa Integrada)

Esta sección integra la rúbrica que antes residía en `rubricas/README.md` para centralizar criterios (archivo eliminado tras fusión). Modelo estándar 40/30/30.

### 1. Examen Canvas (Referencia Bloque 2)

- Banco: 105 preguntas (75 Núcleo + 30 Extended con [S]).
- Preguntas por examen: 22 (estratificado objetivo: [R] 7-8, [C] 7-8, [A] 5-6, [S] 1-2).
- Formato: ~70% opción múltiple / ~30% numéricas.
- Tiempo: 50 minutos. Intento único.
- Temas 20% c/u: Exploración/calidad, estadística descriptiva, métricas derivadas, agrupaciones+outliers, visualización/interpretación.

### 2. Rúbrica Caso 40 / 30 / 30 (100 puntos)

| Área | Puntos | Subcomponentes | Indicadores clave |
|------|--------|----------------|-------------------|
| Exploración y Calidad | 40 | Carga (5) + Exploración head/info (10) + Calidad/Tipos/NA (10) + Estadística descriptiva (15) | `.head()`, `.info()`, rangos validados, interpretación media vs mediana |
| Análisis y Métricas | 30 | Groupby posiciones (12) + Métricas derivadas (10) + Outliers simples (8) | `goles_por_partido`, `contribucion_ofensiva`, criterio outliers documentado |
| Visualización e Interpretación | 30 | Gráficos base (10) + Profundización (10) + Síntesis/Presentación (10) | Gráficos limpios, respuestas socráticas, recomendaciones futbolísticas |

### 3. Niveles de Desempeño

- Excelente: Completo, decisiones justificadas con métricas y reflexión.
- Bueno: 1–2 omisiones menores; interpretación razonable.
- Suficiente: Falta una métrica derivada u outliers; interpretación superficial.
- Insuficiente: Errores que impiden análisis o falta de justificación.

### 4. Requisitos para Nivel Excelente (Transversales)

- Variables en español descriptivas.
- Comentarios justifican pasos críticos (no redundantes).
- Preguntas socráticas respondidas tras cada bloque.
- Notebook ejecuta limpio desde reinicio.

### 5. Autoevaluación Rápida (OK / Revisar)

- [ ] Carga y exploración básica completa
- [ ] Calidad (NA, tipos, rangos) revisada
- [ ] Métricas derivadas creadas y explicadas
- [ ] Outliers identificados y decisión documentada
- [ ] Gráficos base implementados + interpretaciones
- [ ] Gráficos de profundización implementados + interpretaciones
- [ ] Síntesis final con recomendaciones
- [ ] Presentación preparada (3–4 diapositivas)

### 6. Integridad Académica

| Aspecto | Criterio |
|---------|---------|
| Autoría | Trabajo colaborativo (≥80% código original del equipo) |
| Fuentes | Citar si se usa código externo o adaptado |
| IA Asistiva | Declarar uso y describir apoyo (no reemplaza comprensión) |
| Reproducibilidad | Notebook ejecutable sin celdas huérfanas |

### 7. Conversión Ponderada del Bloque

- Examen Canvas: 20% × (puntaje/100)
- Caso práctico: 15% × (puntaje/100)
- Total Bloque 2 = 35% del curso

---

---

## Cronograma de la Semana

| Día | ¿Qué hacer? | Tiempo |
|-----|-------------|--------|
| **Lunes** | Formar equipos, cargar y explorar datos básicos | 2 horas |
| **Miércoles** | Crear gráficos básicos, análisis por posición | 2 horas |
| **Viernes** | Preparar presentación y entregar | 1 hora |

---

## Consejos para el Equipo

### Para Dividir el Trabajo

**Opción 1:** Por partes

- Persona 1: Exploración básica y carga de datos
- Persona 2: Gráficos y visualizaciones
- Persona 3: Análisis por posición y presentación

**Opción 2:** Todos juntos

- Trabajan todos en la misma computadora
- Van rotando quién escribe el código
- Todos participan en las decisiones

### Tips Importantes

- **Variables en español y descriptivas:** `datos_jugadores`, `goles_por_partido`, `contribucion_ofensiva`.
- **Buenas prácticas de gráficos:** títulos informativos (no genéricos), ejes con unidades, ordenar barras, anotar valores en top 5.
- **Interpretar SIEMPRE después de visualizar:** añadir una frase respondiendo a la pregunta socrática sugerida.
- **Documentar supuestos:** si decides mantener outliers, anota por qué.
- **Valida antes de entregar:** ejecutar todo el notebook desde cero sin errores.

---

*Este caso práctico ahora integra exploración estructural, calidad, estadística descriptiva, métricas de eficiencia e interpretación futbolística para preparar la transición a análisis predictivo en el siguiente bloque.*
