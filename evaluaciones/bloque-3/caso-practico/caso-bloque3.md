# Caso Práctico Colaborativo - Bloque 3

## Predicción de Resultados en Champions League con Machine Learning

**Modalidad:** Colaborativa (equipos de 2-3 estudiantes)  
**Ponderación:** 25% del curso total  
**Duración:** 2 semanas  
**Entrega:** Notebook de Jupyter + video de exposición (YouTube)

---

## Contexto del Problema

Eres parte de un equipo que ayuda a un club europeo a predecir resultados de partidos usando machine learning básico. El director técnico quiere entender qué factores influyen más en ganar o perder partidos de Champions League.

**Situación:** Tienen un dataset histórico con estadísticas de partidos de Champions League y quieren crear un modelo simple que les ayude a identificar patrones de victoria y derrota.

---

## Objetivos de Aprendizaje

Al completar este caso práctico, los estudiantes serán capaces de:

- Aplicar algoritmos básicos de machine learning (regresión logística, random forest)
- Preparar datos para modelos predictivos (train/test split)
- Evaluar modelos usando métricas simples (accuracy, matriz de confusión)
- Interpretar importancia de variables en contexto futbolístico
- Crear predicciones básicas sobre resultados deportivos
- Trabajar en equipo para resolver problemas complejos de ML
- Comunicar resultados de modelos de forma comprensible

---

## Datos Que Van a Usar

Trabajarán con un dataset CSV de partidos históricos de UEFA Champions League.

### Dataset Principal: `champions_league_matches.csv`

Archivo CSV con información de 50 partidos históricos de Champions League de las últimas temporadas.

**Descripción de columnas principales:**

- `match_id`: Identificador único del partido
- `fecha`: Fecha del partido (YYYY-MM-DD)
- `equipo_local`, `equipo_visitante`: Nombres de los equipos
- `goles_local`, `goles_visitante`: Goles marcados por cada equipo
- `resultado_final`: Local, Visitante, o Empate
- `fase_competicion`: Fase de Grupos, Octavos de Final, Cuartos de Final, Semifinales, Final
- `temporada`: Temporada de la competición (ej. 2023-24)
- `posesion_local`, `posesion_visitante`: Porcentaje de posesión del balón
- `tiros_local`, `tiros_visitante`: Número total de tiros
- `tiros_arco_local`, `tiros_arco_visitante`: Tiros a portería
- `corners_local`, `corners_visitante`: Número de corners
- `faltas_local`, `faltas_visitante`: Número de faltas cometidas
- `tarjetas_amarillas_local`, `tarjetas_amarillas_visitante`: Tarjetas amarillas recibidas
- `tarjetas_rojas_local`, `tarjetas_rojas_visitante`: Tarjetas rojas recibidas
- `asistencia`: Número de asistentes al estadio

**Características del dataset:**
- **Tamaño**: 50 partidos de Champions League de temporadas recientes
- **Balance**: Aproximadamente 40% victorias locales, 20% empates, 40% victorias visitantes
- **Variables numéricas**: 15+ columnas con estadísticas detalladas (goles, tiros, posesión, tarjetas, etc.)
- **Variables categóricas**: 5 columnas (equipos, resultado_final, fase_competicion, temporada, árbitro)
- **Datos limpios**: Sin valores faltantes, listo para usar
- **Equipos incluidos**: Real Madrid, Barcelona, Manchester City, Bayern Munich, Liverpool, Chelsea, PSG, AC Milan, y otros grandes clubes europeos

---

## Tareas Requeridas

> NOTA IMPORTANTE: Cada subtarea incluye (a) Acción técnica y (b) Pregunta de reflexión breve. Responde siempre estas preguntas antes de continuar al siguiente bloque - te ayudarán a profundizar tu comprensión.

### Parte 1: Exploración y Preparación de Datos (30 puntos)

#### 1.1 Cargar y Explorar Dataset (10 puntos)

Cargar el dataset y hacer exploración inicial para entender los datos:

- Cargar el archivo CSV con pandas
- Examinar estructura básica (filas, columnas, tipos de datos)
- Revisar balance de la variable objetivo (`resultado`)
- Identificar estadísticas básicas de variables numéricas

**Pregunta de reflexión:** ¿Qué te dice el balance entre victorias locales, empates y visitantes sobre la ventaja de casa en Champions League?

#### 1.2 Análisis Exploratorio Enfocado en ML (10 puntos)

Explorar los datos desde la perspectiva de machine learning:

- Analizar correlaciones entre variables estadísticas y resultados
- Identificar posibles variables predictoras importantes
- Crear visualizaciones que muestren patrones por equipo o fase del torneo
- Detectar valores atípicos que podrían afectar el modelo

**Pregunta de reflexión:** ¿Qué variable estadística crees que será la más predictiva y por qué? ¿Hay alguna sorpresa en las correlaciones?

#### 1.3 Preparación de Datos para Modelos (10 puntos)

Preparar los datos en el formato correcto para algoritmos de ML:

- Convertir variables categóricas usando pandas (get_dummies o similar)
- Separar características (X) de la variable objetivo (y)
- Dividir datos en conjuntos de entrenamiento y prueba (train_test_split)
- Verificar que no hay problemas de formato

**Pregunta de reflexión:** ¿Por qué es importante separar datos de entrenamiento y prueba desde el inicio? ¿Qué pasaría si usáramos todos los datos para entrenar?

### Parte 2: Construcción y Evaluación de Modelos (40 puntos)

#### 2.1 Modelo Baseline: Regresión Logística (15 puntos)

Implementar un modelo simple como punto de comparación:

- Entrenar una regresión logística básica
- Hacer predicciones en el conjunto de prueba
- Calcular accuracy (precisión) del modelo
- Examinar cuáles variables son más importantes según el modelo

**Pregunta de reflexión:** ¿El accuracy de tu modelo es mejor que simplemente predecir siempre "victoria local"? ¿Qué te dice esto sobre la calidad del modelo?

#### 2.2 Modelo Avanzado: Random Forest (15 puntos)

Implementar un algoritmo más sofisticado:

- Entrenar un Random Forest con parámetros básicos
- Comparar su accuracy con la regresión logística
- Analizar importancia de características según Random Forest
- Probar diferentes números de árboles y ver el efecto

**Pregunta de reflexión:** ¿El Random Forest mejora significativamente sobre regresión logística? ¿Qué variables considera más importantes cada modelo?

#### 2.3 Evaluación Detallada y Matriz de Confusión (10 puntos)

Evaluar los modelos de forma más completa:

- Crear matriz de confusión para ambos modelos
- Analizar qué tipos de partidos predice mejor/peor cada modelo
- Identificar casos específicos donde el modelo falla
- Comparar rendimiento en diferentes fases del torneo

**Pregunta de reflexión:** ¿En qué tipos de partidos fallan más tus modelos? ¿Hay algún patrón en los errores que sugiera mejoras específicas?

### Parte 3: Interpretación y Aplicación Futbolística (30 puntos)

#### 3.1 Análisis de Importancia de Variables (15 puntos)

Interpretar qué factores son más importantes para predecir victorias:

- Comparar importancia de variables entre ambos modelos
- Crear visualizaciones de las variables más predictivas
- Relacionar los resultados técnicos con conocimiento futbolístico
- Identificar insights sorprendentes o contra-intuitivos

**Pregunta de reflexión:** ¿Los factores más importantes para el modelo coinciden con lo que esperabas como aficionado al fútbol? ¿Hay alguna variable subestimada?

#### 3.2 Predicciones en Escenarios Específicos (10 puntos)

Usar los modelos para hacer predicciones prácticas:

- Crear 2-3 escenarios hipotéticos de partidos
- Hacer predicciones con ambos modelos
- Analizar la confianza/probabilidad de cada predicción
- Discutir limitaciones de estas predicciones

**Pregunta de reflexión:** Si fueras analista de un equipo, ¿usarías este modelo para tomar decisiones? ¿Qué advertencias darías sobre sus limitaciones?

#### 3.3 Recomendaciones para Equipos (5 puntos)

Traducir los hallazgos técnicos a recomendaciones prácticas:

- Sugerir qué estadísticas debería monitorear un equipo
- Identificar factores controlables vs no controlables
- Proponer estrategias basadas en los insights del modelo

**Pregunta de reflexión:** ¿Qué le dirías a un entrenador sobre cómo usar estos hallazgos para mejorar las posibilidades de victoria de su equipo?

---

## Reflexión Final (IMPORTANTE - Incluir en el notebook)

**ESTA SECCIÓN ES OBLIGATORIA - contribuye a su nota del rubro Reflexión y Documentación**

Al completar todas las tareas técnicas, incluye en tu notebook una sección de "Reflexión Final" donde respondas brevemente (2–4 líneas cada una) a **TRES preguntas** de las siguientes cinco opciones:

1. ¿Qué ventajas tiene machine learning sobre análisis estadístico tradicional para predecir resultados deportivos?
2. ¿Por qué es importante evaluar modelos con datos que no vieron durante el entrenamiento?
3. ¿Qué limitaciones encuentras en usar solo estadísticas del partido para predecir resultados?
4. ¿Cómo podrían los insights de importancia de variables cambiar la estrategia de un equipo?
5. ¿Qué otros factores (no en el dataset) crees que influyen significativamente en el resultado?

**Propósito:** Esta reflexión ayuda a consolidar tu aprendizaje y conectar los conceptos técnicos con aplicaciones reales del machine learning deportivo.

---

## Entregables

### 1. Notebook de Jupyter (`caso_bloque3_equipo[X].ipynb`)

- Código funcional que carga y explora los datos correctamente
- Implementación de al menos 2 algoritmos de ML (regresión logística + random forest)
- Evaluación comparativa de modelos con métricas apropiadas
- Análisis de importancia de variables con interpretación futbolística
- Visualizaciones profesionales de resultados y comparaciones
- Predicciones en escenarios específicos
- Respuestas a las preguntas de reflexión intermedias
- Reflexión final completa

### 2. Video de Exposición (YouTube)

- **Duración máxima**: 20 minutos
- **Formato**: Video grabado subido a YouTube (puede ser no listado)
- **Contenido**: Presentación del notebook y explicación de modelos y resultados
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
| **Exploración y Preparación** | 30 | Exploración del dataset (10) + Análisis exploratorio ML (10) + Preparación datos (10) |
| **Construcción y Evaluación de Modelos** | 40 | Regresión logística (15) + Random Forest (15) + Evaluación detallada (10) |
| **Interpretación y Aplicación** | 20 | Importancia variables (15) + Escenarios específicos (5) |
| **Comunicación y Documentación** | 10 | Video de exposición (7) + Reflexión final y comentarios (3) + Enlace en notebook |

### Criterios de Desempeño por Componente

#### 1. Exploración y Preparación de Datos (30 puntos)

**Excelente (30 puntos ~ 100%):**
- Exploración completa del dataset con análisis de balance y correlaciones
- Análisis exploratorio revela insights relevantes para ML
- Preparación correcta: train/test split, codificación categóricas
- Identificación clara de variables predictoras

**Suficiente (21 puntos ~ 70%):**
- Exploración básica funcional
- Preparación de datos correcta
- Análisis superficial de patrones

**Insuficiente (9 puntos ~ 30%):**
- Exploración incompleta o con errores
- Problemas en preparación de datos
- Análisis mínimo

**No presentó (0 puntos):**
- No explora datos o errores graves
- Preparación incorrecta o ausente

#### 2. Construcción y Evaluación de Modelos (40 puntos)

**Excelente (40 puntos ~ 100%):**
- Ambos modelos implementados correctamente
- Comparación clara de rendimiento entre modelos
- Matriz de confusión y métricas interpretadas correctamente
- Análisis de casos donde modelos fallan

**Suficiente (28 puntos ~ 70%):**
- Al menos un modelo implementado correctamente
- Evaluación básica de rendimiento
- Métricas calculadas pero interpretación superficial

**Insuficiente (12 puntos ~ 30%):**
- Modelos parcialmente implementados
- Evaluación incompleta o incorrecta
- Errores en métricas o interpretación

**No presentó (0 puntos):**
- No implementa modelos ML
- Errores graves que impiden ejecución

#### 3. Interpretación y Aplicación Futbolística (20 puntos)

**Excelente (20 puntos ~ 100%):**
- Análisis claro de importancia de variables
- Conexión sólida entre resultados técnicos y contexto futbolístico
- Predicciones en escenarios específicos bien justificadas
- Recomendaciones prácticas para equipos

**Suficiente (14 puntos ~ 70%):**
- Análisis básico de importancia
- Conexión superficial con contexto futbolístico
- Algunas predicciones específicas

**Insuficiente (6 puntos ~ 30%):**
- Interpretación técnica mínima
- Poca conexión con aplicación real
- Predicciones sin justificación

**No presentó (0 puntos):**
- Sin interpretación de resultados
- No hace predicciones específicas

#### 4. Comunicación y Documentación (10 puntos)

**Excelente (10 puntos ~ 100%):**
- Video claro, bien estructurado, ≤20 minutos
- Participación equilibrada del equipo
- Reflexión final completa con 3 preguntas respondidas
- Comentarios explicativos claros en código

**Suficiente (7 puntos ~ 70%):**
- Video básico pero funcional
- Reflexión final presente
- Algunos comentarios en código

**Insuficiente (3 puntos ~ 30%):**
- Video de baja calidad o excede tiempo significativamente
- Reflexión final incompleta
- Pocos comentarios

**No presentó (0 puntos):**
- Sin video o video no accesible
- Sin reflexión final

### Tabla Resumen de Calificación

| Componente | Puntos Máximos | Excelente (~100%) | Suficiente (~70%) | Insuficiente (~30%) | No presentó (0%) |
|------------|-----------------|-------------------|-------------------|---------------------|------------------|
| Exploración y Preparación | 30 | 30 puntos | 21 puntos | 9 puntos | 0 puntos |
| Construcción y Evaluación | 40 | 40 puntos | 28 puntos | 12 puntos | 0 puntos |
| Interpretación y Aplicación | 20 | 20 puntos | 14 puntos | 6 puntos | 0 puntos |
| Comunicación y Documentación | 10 | 10 puntos | 7 puntos | 3 puntos | 0 puntos |
| **TOTAL** | **100** | **100 puntos** | **70 puntos** | **30 puntos** | **0 puntos** |

### Requisitos Mínimos para Aprobar

- Notebook ejecuta sin errores graves
- Implementa al menos un modelo de ML correctamente
- Video subido a YouTube con participación de todo el equipo
- Duración del video ≤25 minutos (máximo absoluto)

### Penalizaciones

- **-5 puntos**: Video excede 25 minutos
- **-3 puntos**: No todos los integrantes participan en el video
- **-5 puntos**: Notebook no ejecuta por errores de sintaxis
- **-2 puntos**: Variables en inglés o nombres no descriptivos

---

## Cronograma de las 2 Semanas

| Semana | Día | ¿Qué hacer? | Tiempo |
|--------|-----|-------------|--------|
| **1** | **Lunes** | Formar equipos, exploración inicial, análisis exploratorio | 2.5 horas |
| **1** | **Miércoles** | Preparación datos, primer modelo (regresión logística) | 2.5 horas |
| **1** | **Viernes** | Segundo modelo (random forest), comparación inicial | 2 horas |
| **2** | **Lunes** | Evaluación detallada, interpretación resultados | 2.5 horas |
| **2** | **Miércoles** | Predicciones específicas, recomendaciones prácticas | 2 horas |
| **2** | **Viernes** | Preparar y grabar video de exposición | 2.5 horas |

**Fecha límite de entrega**: 1 de diciembre de 2025, 11:59 PM  
**Recomendación**: Completar durante las semanas del 18-22 y 25-29 de noviembre

**Entrega**: Notebook + link de YouTube en Canvas

---

## Consejos Útiles

### Para el Código

- Usen variables con nombres claros: `datos_champions`, `modelo_regresion`, `matriz_confusion`
- Comenten decisiones importantes (por qué elegir ciertas variables, parámetros de modelos)
- Validen que todos los modelos entrenan y predicen sin errores
- Documenten experimentos: qué probaron y qué resultados obtuvieron

### Para el Trabajo en Equipo

- **Persona 1**: Exploración, preparación de datos y regresión logística
- **Persona 2**: Random Forest, evaluación comparativa y matriz de confusión  
- **Persona 3**: Interpretación de resultados, predicciones específicas y preparación del video
- **Todos**: Participan en análisis de importancia de variables y reflexiones

### Para el Video de Exposición

- **Duración**: Practiquen para mantenerse en 15-18 minutos
- **Participación**: Cada persona explica 6-7 minutos
- **Estructura sugerida**: 
  - Introducción y dataset (3 min)
  - Exploración y preparación (5 min)
  - Modelos y comparación (6 min)
  - Interpretación y aplicaciones (4-5 min)
  - Limitaciones y conclusiones (2 min)
- **Técnico**: Graben pantalla mostrando el notebook, audio claro
- **Herramientas**: Pueden usar Zoom, OBS, o la grabación de pantalla del sistema operativo

### Preguntas Frecuentes

1. **¿Qué accuracy es "bueno" para este problema?** → Mejor que predecir siempre la clase mayoría (~40-45% sería baseline)
2. **¿Cómo interpreto la importancia de variables?** → Variables con valores altos influyen más en las predicciones del modelo
3. **¿Qué hacer si un modelo da accuracy muy bajo?** → Revisar preparación de datos, probar diferentes variables o parámetros
4. **¿El video puede ser "no listado" en YouTube?** → Sí, pero debe ser accesible con el link

---

### Autoevaluación Rápida (Marcar OK / Revisar)

**Exploración y Preparación:**
- [ ] Cargué y exploré el dataset correctamente
- [ ] Analicé correlaciones y balance de clases
- [ ] Preparé datos con train_test_split y codificación categóricas
- [ ] Identifiqué variables predictoras relevantes

**Modelos de Machine Learning:**
- [ ] Implementé regresión logística correctamente
- [ ] Implementé random forest y lo comparé con regresión
- [ ] Calculé accuracy y matriz de confusión para ambos
- [ ] Analicé importancia de variables en ambos modelos

**Interpretación y Aplicación:**
- [ ] Conecté resultados técnicos con contexto futbolístico
- [ ] Hice predicciones en escenarios específicos
- [ ] Identifiqué limitaciones de los modelos
- [ ] Propuse recomendaciones prácticas para equipos

**Comunicación:**
- [ ] Respondí preguntas de reflexión intermedias
- [ ] Completé reflexión final (3 preguntas elegidas)
- [ ] Video dura máximo 20 minutos con participación equilibrada
- [ ] Notebook ejecuta completamente sin errores

**Entrega:**
- [ ] Variables y comentarios en español
- [ ] Link de YouTube incluido en notebook
- [ ] Archivo enviado en Canvas antes de fecha límite

---

*Este caso práctico integra machine learning básico, evaluación de modelos, interpretación de resultados y aplicación práctica para culminar el aprendizaje del curso de ciencia de datos aplicada al fútbol.*

---
