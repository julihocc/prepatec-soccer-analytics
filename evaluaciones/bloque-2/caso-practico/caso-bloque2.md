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

Configurar el entorno de trabajo y cargar los datos:

- Importar las librerías necesarias (pandas, matplotlib, seaborn, numpy)
- Configurar seaborn con el tema y paleta apropiados
- Cargar el dataset CSV usando pandas
- Verificar que los datos se cargaron correctamente

**Pregunta de reflexión:** ¿Por qué usamos pandas para cargar datos en lugar de leer el archivo línea por línea? ¿Qué ventajas nos da esta librería?

#### 1.2 Exploración Estructural Básica (10 puntos)

Usar métodos de pandas para entender la estructura de los datos:

- Mostrar información básica del dataset (número de filas, columnas disponibles)
- Examinar las primeras filas para entender el formato
- Contar jugadores por posición para verificar balance
- Calcular estadísticas básicas de goles y asistencias (promedio, máximo)

**Pregunta de reflexión:** ¿Qué información te da el conteo por posición sobre el balance del dataset? ¿Hay alguna posición que podría estar subrepresentada?

#### 1.3 Evaluación de Calidad de Datos (10 puntos)

Verificar la integridad y consistencia de los datos:

- Obtener información estructural completa del dataset (tipos de datos, memoria)
- Verificar tipos de datos por columna para detectar inconsistencias
- Detectar y contar valores faltantes por columna
- Verificar rangos lógicos (edades válidas, goles no negativos)
- Reportar hallazgos sobre la calidad general de los datos

**Pregunta de reflexión:** ¿Qué problemas podría causar trabajar con un dataset que tiene valores faltantes en las columnas de goles? ¿Cómo afectaría tus análisis posteriores?

#### 1.4 Estadística Descriptiva Completa (15 puntos)

Ir más allá de promedios básicos para entender la distribución de los datos:

- Generar resumen estadístico completo de variables numéricas (describe())
- Calcular estadísticas adicionales importantes (media, mediana, desviación estándar)
- Identificar al mejor goleador y mejor asistente del dataset
- Comparar media vs mediana para entender la distribución de los datos

**Pregunta de reflexión:** ¿Qué nos indica cuando la media y mediana de goles son muy diferentes? ¿Qué sugiere esto sobre la distribución de goleadores en el dataset?

### Parte 2: Análisis y Métricas Avanzadas (30 puntos)

#### 2.1 Análisis por Grupos usando GroupBy (12 puntos)

Comparar rendimiento entre diferentes posiciones usando pandas avanzado:

- Crear estadísticas agrupadas por posición (media, máximo, conteo de goles y asistencias)
- Calcular promedio de partidos jugados por posición
- Encontrar el mejor goleador de cada posición específica
- Interpretar las diferencias de rendimiento entre posiciones

**Pregunta de reflexión:** ¿Por qué es importante comparar jugadores dentro de su misma posición en lugar de comparar todos juntos? ¿Qué sesgos podríamos introducir si no agrupamos por posición?

#### 2.2 Creación de Métricas Derivadas (10 puntos)

Crear nuevas variables que nos ayuden a evaluar mejor el rendimiento:

- Calcular goles por partido para cada jugador
- Crear variable de contribución ofensiva (goles + asistencias)
- Calcular promedios de las nuevas métricas por posición
- Identificar top 5 jugadores por contribución ofensiva

**Pregunta de reflexión:** ¿Por qué `goles_por_partido` puede ser más útil que el total de goles para evaluar a un jugador? ¿En qué situaciones esta métrica podría ser engañosa?

#### 2.3 Detección de Valores Atípicos (8 puntos)

Identificar jugadores con rendimientos excepcionales que podrían afectar nuestros análisis:

- Calcular umbral para outliers usando método estadístico (media + 2 desviaciones estándar)
- Identificar jugadores con goles excepcionales comparados con sus posiciones
- Analizar si estos outliers representan talento excepcional o errores de datos
- Tomar decisión documentada sobre mantener o excluir estos jugadores

**Pregunta de reflexión:** Si encuentras un delantero con muchos más goles que el resto, ¿lo considerarías un outlier problemático o talento excepcional? ¿Cómo afectaría al promedio de su posición?

### Parte 3: Visualización e Interpretación (30 puntos)

#### 3.1 Gráficos Fundamentales (15 puntos)

Crear visualizaciones profesionales para comunicar los hallazgos:

**a) Gráfico de barras - Distribución por posición:**
- Crear gráfico de barras mostrando conteo de jugadores por posición
- Ordenar las barras de mayor a menor cantidad
- Incluir título, etiquetas de ejes y formato profesional

**b) Gráfico de cajas - Distribución de goles por posición:**
- Usar boxplot de seaborn para mostrar distribución de goles por posición
- Configurar tamaño de figura apropiado y rotación de etiquetas
- Interpretar las diferencias de variabilidad entre posiciones

**c) Gráfico de dispersión - Relación goles vs asistencias:**
- Crear scatter plot con goles en x y asistencias en y
- Usar colores diferentes por posición (hue parameter)
- Incluir leyenda y formato profesional

**Pregunta de reflexión:** ¿Qué posición muestra mayor variabilidad en goles según el boxplot? ¿Observas alguna relación clara entre goles y asistencias en el gráfico de dispersión?

#### 3.2 Visualizaciones Avanzadas (10 puntos)

Crear gráficos adicionales para profundizar en el análisis:

**a) Top 5 goleadores:**
- Crear gráfico de barras horizontales con los 5 mejores goleadores
- Mostrar valores numéricos en las barras para facilitar lectura
- Ordenar de mayor a menor número de goles

**b) Comparación de eficiencia:**
- Gráfico de dispersión con goles_por_partido vs contribucion_ofensiva
- Usar colores por posición y transparencia apropiada
- Interpretar qué jugadores son más eficientes por tiempo jugado

**c) Distribución de edades:**
- Histograma de edades de los jugadores con bins apropiados
- Usar transparencia y bordes para mejor visualización
- Analizar si hay concentración en ciertas edades

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
