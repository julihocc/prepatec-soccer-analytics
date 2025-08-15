# Caso Práctico Colaborativo - Bloque 2

## Análisis de Rendimiento de Jugadores con Pandas y Visualización

**Modalidad:** Colaborativa (equipos de 2-3 estudiantes)  
**Ponderación:** 15% del curso total  
**Duración:** 1 semana  
**Entrega:** Notebook de Jupyter + video de exposición (YouTube)

---

## Contexto del Problema

Eres parte de un equipo que ayuda a analizar el rendimiento avanzado de jugadores juveniles de fútbol. Una escuela deportiva necesita entender mejor a sus jugadores usando herramientas de ciencia de datos.

**Situación:** Tienen un dataset con información detallada de jugadores (goles, asistencias, edad, posición) y quieren identificar patrones, evaluar calidad de datos y crear visualizaciones profesionales para tomar decisiones informadas.

---

## Objetivos de Aprendizaje

Al completar este caso práctico, los estudiantes serán capaces de:

- Cargar y explorar datasets usando pandas avanzado
- Evaluar calidad de datos y detectar inconsistencias
- Crear métricas derivadas para análisis deportivo
- Generar visualizaciones profesionales con seaborn y matplotlib
- Aplicar estadística descriptiva para comparar grupos
- Trabajar en equipo para resolver problemas complejos
- Comunicar resultados técnicos de forma clara

---

## Datos Que Van a Usar

Trabajarán con un dataset CSV real de jugadores juveniles de fútbol mexicano.

### Dataset Principal: `jugadores_liga_juvenil.csv`

Archivo CSV con información de 50 jugadores de ligas juveniles mexicanas.

```csv
jugador_id,nombre,edad,equipo,posicion,torneo,goles,asistencias,partidos_jugados
1,Alejandro Martínez,17,Atlas Sub-20,Delantero,Liga MX Sub-20,12,5,18
2,Sofia Hernández,16,Chivas Femenil,Mediocampo,Liga MX Femenil Sub-18,3,18,20
3,Diego Ramírez,18,América Sub-20,Delantero,Liga MX Sub-20,15,3,19
4,Camila Torres,17,Tigres Femenil,Defensa,Liga MX Femenil Sub-18,1,4,22
...
```

**Descripción de columnas:**

- `jugador_id`: Número único del jugador (1-50)
- `nombre`: Nombre completo del jugador
- `edad`: Edad en años (16-18)
- `equipo`: Equipo al que pertenece (Atlas, Chivas, América, etc.)
- `posicion`: Posición en el campo (Delantero, Mediocampo, Defensa, Portero)
- `torneo`: Liga MX Sub-20 o Liga MX Femenil Sub-18
- `goles`: Cantidad total de goles marcados (0-16)
- `asistencias`: Cantidad total de asistencias dadas (0-18)
- `partidos_jugados`: Número de partidos que ha jugado (14-22)

**Características del dataset:**
- **Tamaño**: 50 jugadores (25 masculinos Sub-20, 25 femeninos Sub-18)
- **Balance por posición**: Delanteros (15), Mediocampo (15), Defensa (13), Porteros (7)
- **Sin valores faltantes**: Dataset completo y limpio
- **Outliers interesantes**: Goleador máximo con 16 goles, mejor asistente con 18 asistencias

---

## Tareas Requeridas

> NOTA IMPORTANTE: Cada subtarea incluye (a) Acción técnica y (b) Pregunta de reflexión breve. Responde siempre estas preguntas antes de continuar al siguiente bloque - te ayudarán a profundizar tu comprensión.

### Parte 1: Exploración y Calidad de Datos (40 puntos)

#### 1.1 Cargar y Configurar Entorno (5 puntos)

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Configuración obligatoria de seaborn
sns.set_theme(style="whitegrid", palette="viridis")

# Cargar el dataset
datos_jugadores = pd.read_csv('jugadores_liga_juvenil.csv')
print("Datos cargados correctamente!")
```

**Pregunta de reflexión:** ¿Por qué usamos pandas para cargar datos en lugar de leer el archivo línea por línea? ¿Qué ventajas nos da esta librería?

#### 1.2 Exploración Estructural Básica (10 puntos)

Usar métodos de pandas para entender la estructura de los datos:

```python
# Información básica del dataset
print(f"Tenemos {len(datos_jugadores)} jugadores")
print(f"Columnas disponibles: {list(datos_jugadores.columns)}")

# Ver las primeras filas
print(datos_jugadores.head())

# Contar jugadores por posición  
print(datos_jugadores['posicion'].value_counts())

# Estadísticas básicas de goles y asistencias
print(f"Promedio de goles: {datos_jugadores['goles'].mean():.1f}")
print(f"Máximo de goles: {datos_jugadores['goles'].max()}")
print(f"Promedio de asistencias: {datos_jugadores['asistencias'].mean():.1f}")
```

**Pregunta de reflexión:** ¿Qué información te da el conteo por posición sobre el balance del dataset? ¿Hay alguna posición que podría estar subrepresentada?

#### 1.3 Evaluación de Calidad de Datos (10 puntos)

Verificar la integridad y consistencia de los datos:

```python
# Información estructural completa
print("Información del dataset:")
print(datos_jugadores.info())

# Verificar tipos de datos
print("Tipos de datos por columna:")
print(datos_jugadores.dtypes)

# Detectar valores faltantes
print("Valores faltantes por columna:")
print(datos_jugadores.isna().sum())

# Verificar rangos lógicos
edades_invalidas = datos_jugadores[~datos_jugadores['edad'].between(16, 18)]
goles_negativos = datos_jugadores[datos_jugadores['goles'] < 0]

if len(edades_invalidas) > 0:
    print("Advertencia: edades fuera de rango esperado")
else:
    print("Todas las edades están en rango válido (16-18 años)")
    
if len(goles_negativos) > 0:
    print("Advertencia: goles negativos encontrados")
else:
    print("Todos los valores de goles son válidos (≥0)")
```

**Pregunta de reflexión:** ¿Qué problemas podría causar trabajar con un dataset que tiene valores faltantes en las columnas de goles? ¿Cómo afectaría tus análisis posteriores?

#### 1.4 Estadística Descriptiva Completa (15 puntos)

Ir más allá de promedios básicos para entender la distribución de los datos:

```python
# Resumen estadístico completo
resumen_numerico = datos_jugadores[['goles', 'asistencias', 'partidos_jugados', 'edad']].describe()
print("Resumen estadístico completo:")
print(resumen_numerico)

# Estadísticas adicionales importantes
estadisticas_extra = datos_jugadores[['goles', 'asistencias']].agg(['mean', 'median', 'std']).round(2)
print("Comparación media vs mediana:")
print(estadisticas_extra)

# Identificar el mejor goleador
mejor_goleador = datos_jugadores.loc[datos_jugadores['goles'].idxmax()]
print(f"Mejor goleador: {mejor_goleador['nombre']} con {mejor_goleador['goles']} goles")

# Mostrar también el mejor asistente
mejor_asistente = datos_jugadores.loc[datos_jugadores['asistencias'].idxmax()]
print(f"Mejor asistente: {mejor_asistente['nombre']} con {mejor_asistente['asistencias']} asistencias")
```

**Pregunta de reflexión:** ¿Qué nos indica cuando la media y mediana de goles son muy diferentes? ¿Qué sugiere esto sobre la distribución de goleadores en el dataset?

### Parte 2: Análisis y Métricas Avanzadas (30 puntos)

#### 2.1 Análisis por Grupos usando GroupBy (12 puntos)

Comparar rendimiento entre diferentes posiciones usando pandas avanzado:

```python
# Estadísticas por posición
estadisticas_posicion = datos_jugadores.groupby('posicion').agg({
    'goles': ['mean', 'max', 'count'],
    'asistencias': ['mean', 'max'],
    'partidos_jugados': 'mean'
}).round(2)

print("Estadísticas por posición:")
print(estadisticas_posicion)

# Encontrar el mejor jugador de cada posición
print("Mejor goleador por posición:")
for posicion in datos_jugadores['posicion'].unique():
    subset = datos_jugadores[datos_jugadores['posicion'] == posicion]
    mejor = subset.loc[subset['goles'].idxmax()]
    print(f"{posicion}: {mejor['nombre']} ({mejor['goles']} goles)")
```

**Pregunta de reflexión:** ¿Por qué es importante comparar jugadores dentro de su misma posición en lugar de comparar todos juntos? ¿Qué sesgos podríamos introducir si no agrupamos por posición?

#### 2.2 Creación de Métricas Derivadas (10 puntos)

Crear nuevas variables que nos ayuden a evaluar mejor el rendimiento:

```python
# Crear métricas de eficiencia
datos_jugadores['goles_por_partido'] = (datos_jugadores['goles'] / datos_jugadores['partidos_jugados']).round(2)
datos_jugadores['contribucion_ofensiva'] = datos_jugadores['goles'] + datos_jugadores['asistencias']

# Calcular promedios de las nuevas métricas por posición
metricas_eficiencia = datos_jugadores.groupby('posicion')[['goles_por_partido', 'contribucion_ofensiva']].mean().round(2)
print("Métricas de eficiencia por posición:")
print(metricas_eficiencia)

# Top 5 jugadores por contribución ofensiva
top_contribucion = datos_jugadores.nlargest(5, 'contribucion_ofensiva')
print("Top 5 por contribución ofensiva:")
print(top_contribucion[['nombre', 'posicion', 'goles', 'asistencias', 'contribucion_ofensiva']])
```

**Pregunta de reflexión:** ¿Por qué `goles_por_partido` puede ser más útil que el total de goles para evaluar a un jugador? ¿En qué situaciones esta métrica podría ser engañosa?

#### 2.3 Detección de Valores Atípicos (8 puntos)

Identificar jugadores con rendimientos excepcionales que podrían afectar nuestros análisis:

```python
# Método simple: media + 2 desviaciones estándar
media_goles = datos_jugadores['goles'].mean()
std_goles = datos_jugadores['goles'].std()
umbral_superior = media_goles + 2 * std_goles

# Identificar outliers en goles
outliers_goles = datos_jugadores[datos_jugadores['goles'] > umbral_superior]
print(f"Umbral para outliers en goles: {umbral_superior:.1f}")
print("Jugadores con goles excepcionales:")
print(outliers_goles[['nombre', 'posicion', 'goles', 'partidos_jugados']])

# Decisión: ¿mantenerlos o no?
print("Decisión del equipo: [Explicar aquí si mantienen o excluyen estos jugadores y por qué]")
```

**Pregunta de reflexión:** Si encuentras un delantero con muchos más goles que el resto, ¿lo considerarías un outlier problemático o talento excepcional? ¿Cómo afectaría al promedio de su posición?

### Parte 3: Visualización e Interpretación (30 puntos)

#### 3.1 Gráficos Fundamentales (15 puntos)

Crear visualizaciones profesionales para comunicar los hallazgos:

**a) Gráfico de barras - Distribución por posición:**

```python
plt.figure(figsize=(10, 6))
conteo_posiciones = datos_jugadores['posicion'].value_counts().sort_values(ascending=False)
plt.bar(conteo_posiciones.index, conteo_posiciones.values)
plt.title('Distribución de Jugadores por Posición')
plt.xlabel('Posición')
plt.ylabel('Número de Jugadores')
plt.xticks(rotation=45)
plt.show()
```

**b) Gráfico de cajas - Distribución de goles por posición:**

```python
plt.figure(figsize=(12, 6))
sns.boxplot(data=datos_jugadores, x='posicion', y='goles')
plt.title('Distribución de Goles por Posición')
plt.xlabel('Posición')
plt.ylabel('Goles')
plt.xticks(rotation=45)
plt.show()
```

**c) Gráfico de dispersión - Relación goles vs asistencias:**

```python
plt.figure(figsize=(10, 8))
sns.scatterplot(data=datos_jugadores, x='goles', y='asistencias', hue='posicion', s=100)
plt.title('Relación entre Goles y Asistencias por Posición')
plt.xlabel('Goles')
plt.ylabel('Asistencias')
plt.legend(title='Posición')
plt.show()
```

**Pregunta de reflexión:** ¿Qué posición muestra mayor variabilidad en goles según el boxplot? ¿Observas alguna relación clara entre goles y asistencias en el gráfico de dispersión?

#### 3.2 Visualizaciones Avanzadas (10 puntos)

Crear gráficos adicionales para profundizar en el análisis:

**a) Top 5 goleadores:**

```python
plt.figure(figsize=(10, 6))
top_goleadores = datos_jugadores.nlargest(5, 'goles')
plt.barh(top_goleadores['nombre'], top_goleadores['goles'])
plt.title('Top 5 Goleadores')
plt.xlabel('Goles')
plt.ylabel('Jugador')
# Añadir valores en las barras
for i, v in enumerate(top_goleadores['goles']):
    plt.text(v + 0.1, i, str(v), va='center')
plt.show()
```

**b) Comparación de eficiencia:**

```python
plt.figure(figsize=(12, 6))
sns.scatterplot(data=datos_jugadores, x='goles_por_partido', y='contribucion_ofensiva', 
                hue='posicion', s=100, alpha=0.7)
plt.title('Eficiencia: Goles por Partido vs Contribución Ofensiva')
plt.xlabel('Goles por Partido')
plt.ylabel('Contribución Ofensiva (Goles + Asistencias)')
plt.legend(title='Posición')
plt.show()
```

**c) Distribución de edades:**

```python
plt.figure(figsize=(10, 6))
plt.hist(datos_jugadores['edad'], bins=8, alpha=0.7, edgecolor='black')
plt.title('Distribución de Edades de los Jugadores')
plt.xlabel('Edad')
plt.ylabel('Frecuencia')
plt.show()
```

**Pregunta de reflexión:** ¿Los mejores goleadores también tienen alta contribución ofensiva? ¿Qué indica la distribución de edades sobre el nivel de desarrollo de los jugadores?

#### 3.3 Interpretación y Comunicación (5 puntos)

Preparar una síntesis clara de los hallazgos:

- Comparar rendimiento promedio por posición
- Identificar los 3 jugadores más valiosos del dataset
- Analizar patrones en la relación goles-asistencias
- Evaluar la distribución de edades y su impacto
- Proponer una recomendación práctica para el cuerpo técnico

---

## Reflexión Final (IMPORTANTE - Incluir en el notebook)

**ESTA SECCIÓN ES OBLIGATORIA - contribuye a su nota del rubro Reflexión y Documentación**

Al completar todas las tareas técnicas, incluye en tu notebook una sección de "Reflexión Final" donde respondas brevemente (2–4 líneas cada una) a **TRES preguntas** de las siguientes cinco opciones:

1. ¿Qué ventajas tiene usar pandas groupby en lugar de filtrar manualmente por cada posición?
2. ¿Por qué es importante evaluar la calidad de datos antes de hacer visualizaciones?
3. ¿Qué información adicional necesitarías para hacer un análisis más completo de rendimiento?
4. ¿Cómo podrían los outliers afectar las decisiones de un entrenador si no los identificas?
5. ¿Cuál sería tu siguiente paso de análisis en el Bloque 3 (Machine Learning)?

**Propósito:** Esta reflexión ayuda a consolidar tu aprendizaje y conectar los conceptos técnicos con aplicaciones reales del análisis de datos deportivos.

---

## Entregables

### 1. Notebook de Jupyter (`caso_bloque2_equipo[X].ipynb`)

- Código funcional que carga y analiza los datos correctamente
- Exploración completa con verificación de calidad de datos
- Métricas derivadas implementadas y explicadas
- Visualizaciones profesionales con títulos y etiquetas claras
- Análisis por grupos usando groupby
- Respuestas a las preguntas de reflexión intermedias
- Reflexión final completa

### 2. Video de Exposición (YouTube)

- **Duración máxima**: 15 minutos
- **Formato**: Video grabado subido a YouTube (puede ser no listado)
- **Contenido**: Presentación del notebook y explicación de hallazgos principales
- **Participación**: Cada integrante debe explicar al menos una parte
- **Envío**: Link de YouTube incluido en el notebook

### IMPORTANTE: Enlace en el Notebook

**Al final de su notebook, en una celda de Markdown claramente identificada, deben incluir:**

```markdown
## 📹 Video de Presentación del Equipo

**Enlace al video de YouTube:** [TÍTULO DEL VIDEO](URL_DEL_VIDEO_DE_YOUTUBE)

**Integrantes del equipo:**
- Nombre Completo 1 (Matrícula)
- Nombre Completo 2 (Matrícula) 
- Nombre Completo 3 (Matrícula)

**Fecha de grabación:** DD/MM/AAAA
```

---

## Criterios de Evaluación

### Rúbrica del Caso Práctico (100 puntos totales)

**Distribución**: 70% Desarrollo Técnico + 30% Comunicación y Reflexión

| Componente | Puntos | Criterios de Evaluación |
|------------|--------|------------------------|
| **Exploración y Calidad de Datos** | 40 | Carga correcta (5) + Exploración estructural (10) + Calidad y validación (10) + Estadística descriptiva (15) |
| **Análisis y Métricas Avanzadas** | 30 | GroupBy y análisis por posición (12) + Métricas derivadas (10) + Detección de outliers (8) |
| **Visualización e Interpretación** | 20 | Gráficos fundamentales (15) + Visualizaciones avanzadas (5) |
| **Comunicación y Documentación** | 10 | Video de exposición (7) + Reflexión final y comentarios (3) + Enlace en notebook |

### Criterios de Desempeño por Componente

#### 1. Exploración y Calidad de Datos (40 puntos)

**Excelente (40 puntos ~ 100%):**
- Carga datos correctamente y configura entorno
- Exploración completa con `.head()`, `.info()`, conteos por posición
- Evalúa calidad: tipos, valores faltantes, rangos válidos
- Estadística descriptiva completa con interpretación de media vs mediana

**Suficiente (28 puntos ~ 70%):**
- Carga datos y exploración básica funcional
- Evaluación superficial de calidad
- Estadísticas básicas sin interpretación profunda

**Insuficiente (12 puntos ~ 30%):**
- Exploración incompleta o con errores
- No evalúa calidad de datos
- Estadísticas mínimas

**No presentó (0 puntos):**
- No carga datos o errores graves
- Exploración ausente o no funcional

#### 2. Análisis y Métricas Avanzadas (30 puntos)

**Excelente (30 puntos ~ 100%):**
- GroupBy implementado correctamente con múltiples estadísticas
- Métricas derivadas creadas y bien explicadas
- Outliers identificados con criterio justificado
- Interpretaciones claras de los resultados

**Suficiente (21 puntos ~ 70%):**
- GroupBy básico funcional
- Al menos una métrica derivada
- Outliers identificados sin justificación profunda

**Insuficiente (9 puntos ~ 30%):**
- GroupBy parcial o con errores
- Métricas derivadas incompletas
- No identifica outliers

**No presentó (0 puntos):**
- No implementa groupby
- Falta análisis por grupos

#### 3. Visualización e Interpretación (20 puntos)

**Excelente (20 puntos ~ 100%):**
- Todos los gráficos fundamentales implementados correctamente
- Gráficos con títulos, etiquetas y formato profesional
- Visualizaciones avanzadas añaden valor al análisis
- Interpretaciones claras después de cada gráfico

**Suficiente (14 puntos ~ 70%):**
- Mayoría de gráficos implementados
- Formato básico pero legible
- Interpretaciones superficiales

**Insuficiente (6 puntos ~ 30%):**
- Solo algunos gráficos implementados
- Formato pobre o confuso
- Pocas interpretaciones

**No presentó (0 puntos):**
- Gráficos ausentes o no funcionan
- Sin interpretaciones

#### 4. Comunicación y Documentación (10 puntos)

**Excelente (10 puntos ~ 100%):**
- Video claro, bien estructurado, ≤15 minutos
- Participación equilibrada del equipo
- Reflexión final completa con 3 preguntas respondidas
- Comentarios explicativos en código

**Suficiente (7 puntos ~ 70%):**
- Video básico pero funcional
- Reflexión final presente
- Algunos comentarios en código

**Insuficiente (3 puntos ~ 30%):**
- Video de baja calidad o excede tiempo
- Reflexión final incompleta
- Pocos comentarios

**No presentó (0 puntos):**
- Sin video o video no accesible
- Sin reflexión final

### Tabla Resumen de Calificación

| Componente | Puntos Máximos | Excelente (~100%) | Suficiente (~70%) | Insuficiente (~30%) | No presentó (0%) |
|------------|-----------------|-------------------|-------------------|---------------------|------------------|
| Exploración y Calidad de Datos | 40 | 40 puntos | 28 puntos | 12 puntos | 0 puntos |
| Análisis y Métricas Avanzadas | 30 | 30 puntos | 21 puntos | 9 puntos | 0 puntos |
| Visualización e Interpretación | 20 | 20 puntos | 14 puntos | 6 puntos | 0 puntos |
| Comunicación y Documentación | 10 | 10 puntos | 7 puntos | 3 puntos | 0 puntos |
| **TOTAL** | **100** | **100 puntos** | **70 puntos** | **30 puntos** | **0 puntos** |

### Requisitos Mínimos para Aprobar

- Notebook ejecuta sin errores graves
- Implementa groupby básico y al menos una métrica derivada
- Video subido a YouTube con participación de todo el equipo
- Duración del video ≤20 minutos (máximo absoluto)

### Penalizaciones

- **-5 puntos**: Video excede 20 minutos
- **-3 puntos**: No todos los integrantes participan en el video
- **-5 puntos**: Notebook no ejecuta por errores de sintaxis
- **-2 puntos**: Variables en inglés o nombres no descriptivos

---

## Cronograma de la Semana

| Día | ¿Qué hacer? | Tiempo |
|-----|-------------|--------|
| **Lunes** | Formar equipos, cargar datos, exploración y calidad | 2 horas |
| **Miércoles** | Análisis con groupby, métricas derivadas, outliers | 2.5 horas |
| **Viernes** | Crear visualizaciones, grabar video de exposición | 2 horas |

**Fecha límite de entrega**: 17 de noviembre de 2025, 11:59 PM  
**Recomendación**: Completar durante la semana del 10-14 de noviembre para evitar contratiempos

**Entrega**: Notebook + link de YouTube en Canvas

---

## Consejos Útiles

### Para el Código

- Usen variables con nombres claros: `datos_jugadores`, `estadisticas_posicion`, `outliers_goles`
- Comenten el código para explicar decisiones importantes (por qué mantener/excluir outliers)
- Validen que todos los gráficos tengan títulos y etiquetas profesionales

### Para el Trabajo en Equipo

- **Persona 1**: Exploración, calidad de datos y estadística descriptiva
- **Persona 2**: Análisis con groupby, métricas derivadas y outliers  
- **Persona 3**: Visualizaciones y preparación del video
- **Todos**: Participan en interpretaciones y reflexión final

### Para el Video de Exposición

- **Duración**: Practiquen para mantenerse en 12-15 minutos
- **Participación**: Cada persona explica 4-5 minutos
- **Estructura sugerida**: 
  - Introducción y dataset (2 min)
  - Exploración y calidad (4-5 min)
  - Análisis y métricas (4-5 min)
  - Visualizaciones y conclusiones (3-4 min)
- **Técnico**: Graben pantalla mostrando el notebook, audio claro
- **Herramientas**: Pueden usar Zoom, OBS, o la grabación de pantalla del sistema operativo

### Preguntas Frecuentes

1. ¿Cómo interpreto un boxplot? → Las cajas muestran el rango intercuartílico, los puntos externos son outliers
2. ¿Qué hacer si encuentro valores faltantes? → Documentar cuántos hay y decidir si eliminar o mantener
3. ¿Cómo sé si una métrica derivada es útil? → Debe tener interpretación clara y aportar información nueva
4. ¿El video puede ser "no listado" en YouTube? → Sí, pero debe ser accesible con el link

---

### Autoevaluación Rápida (Marcar OK / Revisar)

**Exploración y Análisis:**
- [ ] Cargué datos correctamente y configuré seaborn
- [ ] Exploré estructura con `.head()`, `.info()`, conteos por posición
- [ ] Evalué calidad: tipos, valores faltantes, rangos válidos
- [ ] Calculé estadística descriptiva completa con interpretación
- [ ] Implementé groupby por posición con múltiples estadísticas
- [ ] Creé métricas derivadas (`goles_por_partido`, `contribucion_ofensiva`)
- [ ] Identifiqué outliers y documenté decisión

**Visualización y Comunicación:**
- [ ] Creé gráficos fundamentales (barras, boxplot, dispersión)
- [ ] Agregué visualizaciones avanzadas (top 5, eficiencia, edades)
- [ ] Todos los gráficos tienen títulos y etiquetas claras
- [ ] Respondí preguntas de reflexión intermedias
- [ ] Completé reflexión final (3 preguntas elegidas)
- [ ] Video dura máximo 15 minutos con participación equilibrada

**Entrega:**
- [ ] Notebook ejecuta completamente sin errores
- [ ] Variables y comentarios en español
- [ ] Link de YouTube enviado en Canvas

---

*Este caso práctico integra exploración avanzada de datos, estadística descriptiva, visualización profesional y análisis por grupos para preparar el camino hacia machine learning en el Bloque 3.*
