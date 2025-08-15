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

## Parte 3: Intérprete Estratégico (30 puntos)

### Misión: Convierte Datos en Sabiduría Táctica

Los números por sí solos no significan nada si no puedes explicar qué implican para el mundo real. Esta es tu oportunidad de demostrar que entiendes tanto la técnica como el fútbol.

#### Análisis de Tu Modelo (15 puntos)

**Responde estas preguntas con profundidad**:

1. **¿Qué aprendió tu modelo?** ¿Cuáles variables considera más importantes? ¿Te sorprende?
2. **¿Dónde se equivoca más?** Usa matriz de confusión y ejemplos concretos
3. **¿Qué tipo de partidos predice mejor?** ¿Los cerrados? ¿Los de muchos goles?
4. **¿Cómo cambiarían las tácticas basándose en tu modelo?** Si fueras entrenador, ¿qué harías diferente?

#### Aplicación al Mundo Real (15 puntos)

**Elige UNA de estas situaciones y desarrollala completamente**:

**Situación A**: Eres analista del Real Madrid antes de la final de Champions. Basándote en tu modelo, ¿qué recomendaciones tácticas específicas darías al entrenador?

**Situación B**: Un equipo de la Premier League te contrata para ayudarles a clasificar a Champions. ¿Cómo adaptarías tu modelo? ¿Qué limitaciones tendría?

**Situación C**: Una casa de apuestas quiere usar tu modelo para establecer cuotas. ¿Qué les dirías sobre su confiabilidad? ¿Cuáles son los riesgos?

**Criterio clave**: Demuestra que entiendes las limitaciones de tu modelo y puedes comunicar hallazgos técnicos en lenguaje futbolístico.

---

## Tu Producto Final

### Lo Que Debes Entregar

**1. Tu Notebook/Script Completo**
- Tu análisis exploratorio con hallazgos originales
- El código de tu modelo predictivo (con comentarios que expliquen tus decisiones)
- Visualizaciones que cuenten historias interesantes
- Experimentación documentada: qué probaste y por qué

**2. Reporte Ejecutivo (1-2 páginas)**
Escribe como si fueras a presentar esto al director técnico de un equipo profesional:
- ¿Qué descubriste que no sabíamos antes?
- ¿Qué tan confiable es tu sistema predictivo?
- ¿Cómo podría un equipo usar estos hallazgos en la práctica?
- ¿Cuáles son las limitaciones y riesgos de tu modelo?

### Cómo Te Evaluaremos

**Creatividad y Experimentación (40%)**
- Originalidad en tu análisis exploratorio
- Innovación en tu enfoque de modelado
- Calidad de tus experimentos y variaciones
- Pensamiento crítico sobre tus resultados

**Aplicación Futbolística (30%)**
- Conexión entre hallazgos técnicos y realidad deportiva
- Recomendaciones prácticas y viables
- Comprensión de las limitaciones del modelo
- Comunicación clara a audiencia no técnica

**Rigor Técnico (30%)**
- Código funcional y bien documentado
- Uso apropiado de técnicas de machine learning
- Evaluación honesta de la calidad del modelo
- Metodología sólida en experimentación

### Consejos para Destacar

1. **Sé curioso**: Las mejores notas van para quienes encuentran patrones inesperados
2. **Experimenta libremente**: Prueba enfoques diferentes, documenta qué funciona y qué no
3. **Piensa como entrenador**: Conecta tus hallazgos con decisiones tácticas reales
4. **Sé honesto**: Reconocer limitaciones demuestra más madurez que pretender perfección
5. **Cuenta historias**: Los datos sin contexto deportivo son solo números

---

**¡Esto es TU proyecto!** No hay una respuesta "correcta". Los mejores trabajos serán los más creativos, reflexivos y conectados con la realidad del fútbol.

**Tiempo sugerido**: 6-8 horas de exploración, experimentación y análisis.  
**Modalidad**: Individual, pero puedes discutir ideas con compañeros.  
**Fecha límite**: [Definida por el profesor]

---

## Rúbrica de Evaluación Detallada

### Criterios Técnicos (40%)

| Criterio | Excelente (~100%) | Suficiente (~70%) | Insuficiente (~30%) | No presentó (0%) |
|----------|-------------------|-------------------|---------------------|-------------------|
| **Código funcional** | Ejecuta sin errores, sintaxis perfecta, cumple objetivos | Ejecuta con errores menores, cumple objetivos principales | Errores significativos, objetivos parcialmente logrados | No ejecuta o no entregado |
| **Uso de librerías ML** | sklearn, pandas, numpy usados correctamente y eficientemente | Uso básico correcto con pequeñas ineficiencias | Uso incorrecto o confuso de algunas funciones | No usa las librerías requeridas |
| **Calidad del modelo** | Modelo bien configurado, evaluación completa, precisión razonable | Modelo básico funcional, evaluación simple | Modelo problemático, evaluación incompleta | No crea modelo válido |

### Criterios de Aplicación (30%)

| Criterio | Excelente (~100%) | Suficiente (~70%) | Insuficiente (~30%) | No presentó (0%) |
|----------|-------------------|-------------------|---------------------|-------------------|
| **Contexto futbolístico** | Excelente conexión entre análisis y conceptos deportivos reales | Conexión básica adecuada con el contexto | Conexión débil o superficial | Sin conexión deportiva |
| **Interpretación resultados** | Análisis profundo y significativo de patrones y predicciones | Interpretación básica correcta | Interpretación superficial o incorrecta | No interpreta resultados |
| **Casos prácticos** | Escenarios realistas, análisis completo de implicaciones | Escenarios básicos, análisis simple | Escenarios poco realistas o análisis pobre | No incluye casos prácticos |

### Criterios de Comunicación y Razonamiento (30%)

| Criterio | Excelente (~100%) | Suficiente (~70%) | Insuficiente (~30%) | No presentó (0%) |
|----------|-------------------|-------------------|---------------------|-------------------|
| **Reflexiones escritas** | Respuestas profundas, pensamiento crítico evidente | Respuestas adecuadas, comprensión básica | Respuestas superficiales o incorrectas | No responde preguntas |
| **Documentación del proceso** | Experimentos bien documentados, decisiones justificadas | Documentación básica, algunas justificaciones | Documentación limitada o confusa | Sin documentación del proceso |
| **Comunicación técnica** | Explica conceptos complejos claramente, audiencia apropiada | Comunicación básica comprensible | Comunicación confusa o técnicamente incorrecta | No comunica hallazgos |

### Notas Importantes:
- **Requisito mínimo**: Código debe ejecutar sin errores fatales para obtener calificación aprobatoria
- **Creatividad valorada**: Enfoques innovadores recibirán puntuación adicional
- **Honestidad académica**: Reconocer limitaciones es más valioso que pretender perfección

---

## Cronograma Sugerido

### Semana 1: Exploración y Experimentación Inicial

- **Días 1-2**: Análisis exploratorio libre, identificación de patrones interesantes
- **Días 3-4**: Experimentación con diferentes variables y combinaciones
- **Días 5-7**: Construcción inicial de modelos, pruebas de diferentes enfoques

### Semana 2: Refinamiento y Análisis Profundo

- **Días 1-3**: Optimización de modelos, análisis de importancia de variables
- **Días 4-5**: Interpretación de resultados, conexión con contexto futbolístico
- **Días 6-7**: Documentación final, reflexiones críticas, preparación de entregables

---

## Recursos de Apoyo

### Dataset y Herramientas
- **Dataset Champions League**: Proporcionado por el profesor con documentación incluida
- **Librerías requeridas**: pandas, numpy, sklearn, matplotlib, seaborn
- **Entorno sugerido**: Jupyter Notebook o Google Colab

### Consultas y Soporte
- **Horario de oficina**: Disponible para dudas técnicas y metodológicas
- **Foros de discusión**: Para intercambio de ideas entre estudiantes (sin compartir código)
- **Documentación oficial**: Links a recursos de sklearn, pandas, etc.

### Ejemplos de Referencia

- **Análisis exploratorios**: Ejemplos de visualizaciones efectivas para datos deportivos
- **Interpretación de modelos**: Cómo explicar importancia de variables en contexto futbolístico
- **Presentación de resultados**: Formatos para comunicar hallazgos a audiencias no técnicas

---

## Entregables Específicos

### 1. Notebook Principal (`caso_bloque3_[TuNombre].ipynb`)

**Estructura mínima requerida:**

1. **Introducción y Objetivos** (1 sección)
   - Descripción de tu enfoque personal al problema
   - Hipótesis iniciales sobre qué factores pueden predecir mejor

2. **Análisis Exploratorio** (2-3 secciones)
   - Visualizaciones que revelen patrones interesantes
   - Estadísticas descriptivas relevantes para tu análisis
   - Al menos 3 insights únicos sobre los datos

3. **Construcción y Evaluación de Modelos** (2-3 secciones)
   - Experimentación con al menos 2 algoritmos diferentes
   - Evaluación comparativa de rendimiento
   - Análisis de importancia de variables/características

4. **Interpretación Futbolística** (1-2 secciones)
   - Conexión entre resultados técnicos y realidad deportiva
   - Casos específicos donde el modelo acierta o falla
   - Implicaciones para entrenadores, analistas o aficionados

5. **Reflexiones Finales** (1 sección)
   - Limitaciones de tu análisis
   - Posibles mejoras futuras
   - Aprendizajes personales del proceso

### 2. Documento de Reflexión (`reflexion_caso3_[TuNombre].pdf`)

**Extensión**: 2-3 páginas máximo, formato libre

**Preguntas guía para la reflexión** (no es cuestionario rígido):
- ¿Qué fue lo más sorprendente que descubriste en los datos?
- ¿Qué variables resultaron más importantes y por qué crees que es así?
- Si fueras un director técnico, ¿cómo usarías estos insights?
- ¿Qué limitaciones encontraste en tu análisis?
- ¿Cómo ha cambiado tu perspectiva sobre el análisis deportivo?

### 3. Presentación de Hallazgos (`presentacion_caso3_[TuNombre].pptx/pdf`)

**Formato**: 8-10 diapositivas máximo

**Contenido sugerido**:
- Slide 1: Tu enfoque único al problema
- Slides 2-4: Hallazgos clave del análisis exploratorio
- Slides 5-6: Comparación de modelos y mejores resultados
- Slides 7-8: Interpretación futbolística e implicaciones prácticas
- Slides 9-10: Limitaciones y oportunidades futuras

---

## Criterios de Evaluación por Entregable

### Notebook Principal (50% de la calificación total)
- **Código funcional y bien organizado** (20%)
- **Análisis técnico profundo** (15%)  
- **Creatividad en el enfoque** (10%)
- **Documentación clara** (5%)

### Documento de Reflexión (30% de la calificación total)
- **Profundidad de reflexión** (15%)
- **Conexión teoría-práctica** (10%)
- **Autocrítica y reconocimiento de limitaciones** (5%)

### Presentación de Hallazgos (20% de la calificación total)
- **Claridad comunicativa** (10%)
- **Síntesis efectiva de resultados** (5%)
- **Impacto visual y profesionalismo** (5%)

---

## Consejos Prácticos para el Éxito

### Gestión del Tiempo
- **No te obsesiones con la perfección técnica**: Enfócate en insights interesantes
- **Documenta mientras trabajas**: No dejes la reflexión para el final
- **Prueba rápido, itera frecuentemente**: Mejor varios enfoques simples que uno complejo

### Enfoque Analítico
- **Comienza con preguntas simples**: "¿Qué equipos tienen mejor rendimiento local vs visitante?"
- **Visualiza antes de modelar**: Las gráficas revelan patrones que guían el análisis
- **No ignores resultados inesperados**: Los "errores" del modelo pueden ser los insights más valiosos

### Comunicación Efectiva
- **Habla como analista deportivo, no como programador**: Tu audiencia ama el fútbol
- **Usa analogías deportivas**: "Este modelo es como un scout que identifica patrones..."
- **Sé honesto sobre limitaciones**: Reconocer problemas demuestra madurez analítica

### Conexión con el Contexto Real
- **Investiga un poco sobre los equipos**: Conocer su historia enriquece el análisis
- **Piensa como diferentes stakeholders**: ¿Qué le importaría a un entrenador vs un aficionado?
- **Propón aplicaciones concretas**: "Los equipos podrían usar esto para..."

---

## Apoyo Durante el Desarrollo

### ¿Cuándo Buscar Ayuda?
- **Errores técnicos bloqueantes**: Si tu código no ejecuta después de varios intentos
- **Interpretación de resultados confusos**: Cuando los números no tienen sentido deportivo
- **Dirección del análisis**: Si sientes que te perdiste o no sabes cómo continuar

### ¿Qué NO es Válido para Ayuda?
- **Escribir código por ti**: El análisis debe ser tu trabajo original
- **Elegir tu enfoque**: La creatividad y decisiones analíticas deben ser tuyas
- **Garantizar resultados**: No todos los experimentos funcionan, y eso está bien

### Recursos Disponibles
- **Documentación técnica**: Links directos a pandas, sklearn, etc.
- **Ejemplos metodológicos**: Patrones generales de análisis (sin soluciones específicas)
- **Sesiones de consulta**: Para discutir enfoques e interpretar resultados

---

## Fecha de Entrega y Modalidades

**Fecha límite**: [A definir por el profesor - mínimo 2 semanas de desarrollo]

**Modalidad de entrega**: 
- Subir archivos al LMS institucional
- Nombrar archivos con tu nombre: `caso_bloque3_[TuNombre].*`
- Formato aceptado: `.ipynb`, `.pdf`, `.pptx`

**Presentaciones orales**: [Opcional - a definir por el profesor]
- 5 minutos por estudiante
- Enfoque en hallazgos más interesantes
- Q&A breve con compañeros

---

**¡Recuerda**: Este caso práctico vale 25% de tu calificación total del curso. Invierte el tiempo necesario, pero sobre todo... ¡disfruta explorando el fascinante mundo donde el fútbol se encuentra con los datos!
