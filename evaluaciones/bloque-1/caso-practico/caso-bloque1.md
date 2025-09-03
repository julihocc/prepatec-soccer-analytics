# Caso Práctico Colaborativo - Bloque 1

## Análisis Básico de un Equipo de Fútbol

**Modalidad:** Colaborativa (equipos de 2-3 estudiantes)  
**Ponderación:** 15% del curso total  
**Duración:** 1 semana  
**Entrega:** Notebook de Jupyter + video de exposición (YouTube)

---

## Contexto del Problema

Eres parte de un equipo que ayuda a analizar el rendimiento básico de un equipo de fútbol local. Necesitan entender cómo jugó el equipo la temporada pasada usando Python básico.

**Situación:** Tienen datos simples de partidos y jugadores, y quieren saber cosas básicas como cuántos puntos ganaron, quién marcó más goles, etc.

---

## Objetivos de Aprendizaje

Al completar este caso práctico, los estudiantes serán capaces de:

- Usar variables, listas y diccionarios básicos en Python
- Escribir funciones simples para cálculos de fútbol
- Usar bucles for e if para procesar datos
- Trabajar en equipo para resolver un problema
- Explicar sus resultados de forma clara

---

## Datos Que Van a Usar

**NO usarán archivos CSV** - Todo será con listas y diccionarios simples en Python

### Datos de Partidos (lista simple)

```python
resultados_partidos = ["Victoria", "Derrota", "Victoria", "Empate", "Victoria", 
                      "Derrota", "Victoria", "Empate", "Victoria", "Victoria"]

goles_favor = [2, 0, 3, 1, 2, 0, 1, 2, 3, 2]
goles_contra = [1, 3, 1, 1, 0, 2, 0, 2, 1, 1]
```

### Datos de Jugadores (diccionario simple)

```python
jugadores = {
    "Carlos": {"posicion": "Delantero", "goles": 8},
    "María": {"posicion": "Mediocampo", "goles": 3},
    "Luis": {"posicion": "Defensa", "goles": 1},
    "Ana": {"posicion": "Delantero", "goles": 6}
}
```

---

## Tareas Requeridas

> NOTA IMPORTANTE: Cada subtarea incluye (a) Acción técnica y (b) Pregunta de reflexión breve. Responde siempre estas preguntas antes de continuar al siguiente bloque - te ayudarán a profundizar tu comprensión.

### Parte 1: Fundamentos y Funciones (40 puntos)

#### 1.1 Contar Resultados con Bucles (10 puntos)

Usar un bucle for para contar victorias, empates y derrotas:

- Definir las listas de datos proporcionadas en la sección de datos
- Crear variables para contar cada tipo de resultado (victorias, empates, derrotas)
- Usar bucle for e if para recorrer la lista y contar cada resultado
- Mostrar los totales obtenidos

**Pregunta de reflexión:** ¿Qué patrón observas entre victorias y empates? ¿Qué podría significar esto sobre la consistencia del equipo?

#### 1.2 Crear Funciones Simples (20 puntos)

Escribir estas 2 funciones obligatorias:

**a) Función para calcular puntos:**

- Crear función `calcular_puntos(victorias, empates)` que calcule puntos de liga
- Aplicar reglas: Victoria = 3 puntos, Empate = 1 punto, Derrota = 0 puntos
- Retornar el total de puntos calculado
- Probar la función con casos de ejemplo

**b) Función para encontrar mejor goleador:**

- Crear función `mejor_goleador(jugadores)` que reciba el diccionario de jugadores
- Iterar sobre los jugadores para encontrar quien tiene más goles
- Retornar el nombre del mejor goleador y su cantidad de goles
- Verificar que funciona correctamente con los datos dados

**Pregunta de reflexión:** ¿Por qué es útil probar una función con un caso simple antes de usarla en todo el análisis? ¿Qué te da confianza sobre tu código?

#### 1.3 Trabajar con Listas y Diccionarios (10 puntos)

Realizar análisis básicos usando las estructuras de datos:

- Calcular total de goles a favor usando la lista `goles_favor`
- Encontrar el partido con más goles marcados usando funciones básicas
- Usar el diccionario `jugadores` para extraer información por posición
- Contar cuántos jugadores hay por posición

**Pregunta de reflexión:** ¿Qué limitación notas al manejar varias listas separadas para analizar partidos? ¿Cómo crees que esto afectaría si tuvieras 100 partidos?

### Parte 2: Análisis y Métricas Básicas (30 puntos)

#### 2.1 Estadísticas Básicas del Equipo (10 puntos)

Usar las funciones creadas para realizar análisis estadístico básico:

- Usar las funciones que crearon para calcular puntos totales del equipo
- Calcular el promedio de goles por partido (total goles ÷ número de partidos)
- Determinar si el equipo marcó más goles de los que recibió
- Calcular la diferencia de goles total (goles a favor - goles en contra)

**Pregunta de reflexión:** ¿El promedio de goles refleja toda la historia del rendimiento ofensivo? ¿Qué información importante NO te dice este número?

#### 2.2 Análisis de Jugadores (10 puntos)  

Aplicar análisis usando diccionarios para entender el rendimiento individual:

- Usar su función para encontrar el mejor goleador del equipo
- Contar cuántos jugadores hay por posición (delanteros, mediocampo, defensa)
- Calcular el total de goles marcados por todos los jugadores
- Identificar qué posición tiene el promedio de goles más alto

**Pregunta de reflexión:** ¿Ser el máximo goleador implica automáticamente mayor impacto para el equipo? ¿Qué otros datos considerarías para evaluar la contribución real de un jugador?

#### 2.3 Introducción a pandas (10 puntos)

Construir un DataFrame simple para unificar los datos y comparar ventajas respecto a listas:

- Importar pandas y crear un DataFrame con los datos de partidos
- Incluir columnas: número de partido, resultado, goles a favor, goles en contra
- Calcular promedio de goles usando métodos de pandas
- Comparar la facilidad de uso entre DataFrame y listas separadas
- Mostrar las primeras filas del DataFrame creado

**Pregunta de reflexión:** ¿Qué ventaja concreta te da el DataFrame frente a manejar tres listas independientes? ¿En qué situaciones crees que esta diferencia sería aún más importante?

### Parte 3: Visualización e Interpretación (30 puntos)

#### 3.1 Visualización Básica (15 puntos)

Crear visualizaciones profesionales para comunicar los hallazgos:

**a) Gráfico de barras - Rendimiento por partido:**

- Crear gráfico de barras comparando goles a favor y en contra por partido
- Usar matplotlib para generar el gráfico con etiquetas claras
- Incluir título, etiquetas de ejes y leyenda profesional
- Configurar colores y transparencia apropiados

**b) Comparación de resultados:**

- Crear gráfico que muestre la distribución de victorias, empates y derrotas
- Usar gráfico de barras o pie chart para mostrar proporciones
- Incluir números absolutos y porcentajes en la visualización

**Pregunta de reflexión:** ¿En qué partidos la diferencia de goles fue mayor? ¿Qué hipótesis podrías proponer sobre el rendimiento del equipo en esos momentos específicos?

#### 3.2 Análisis por Posición (10 puntos)

Analizar el rendimiento de jugadores por posición:

- Agrupar jugadores por posición y calcular estadísticas básicas
- Crear visualización mostrando goles promedio por posición
- Identificar qué posiciones contribuyen más al ataque
- Comparar el rendimiento individual vs grupal

**Pregunta de reflexión:** ¿Los delanteros son los únicos responsables de los goles? ¿Qué te dice la distribución de goles por posición sobre el estilo de juego del equipo?

#### 3.3 Interpretación y Comunicación (5 puntos)

Preparar una síntesis clara de los hallazgos:

- Comparar rendimiento ofensivo vs defensivo del equipo
- Identificar fortalezas y debilidades basadas en los datos
- Evaluar la consistencia del equipo a lo largo de los partidos
- Proponer una recomendación práctica para mejorar el rendimiento

**Pregunta de reflexión:** ¿Qué le recomendarías al entrenador para mejorar el rendimiento del equipo basándote en estos datos? ¿Qué aspectos priorizarías?

---

## Reflexión Final (IMPORTANTE - Incluir en el notebook)

**ESTA SECCIÓN ES OBLIGATORIA - contribuye a su nota del rubro Reflexión y Documentación**

Al completar todas las tareas técnicas, incluye en tu notebook una sección de "Reflexión Final" donde respondas brevemente (2–4 líneas cada una) a **TRES preguntas** de las siguientes cinco opciones:

1. ¿Qué métrica adicional incluirías para evaluar solidez defensiva y por qué?
2. ¿Qué limitación tiene usar solo 10 partidos para conclusiones?
3. ¿Qué beneficio te dio el DataFrame frente a listas separadas?
4. ¿Qué mostrarías a un entrenador para convencerlo de mejorar el ataque?
5. ¿Cuál sería tu siguiente paso de análisis en el Bloque 2?

**Propósito:** Esta reflexión ayuda a consolidar tu aprendizaje y conectar los conceptos técnicos con aplicaciones reales del análisis de datos deportivos.

---

## Entregables

### 1. Notebook de Jupyter (`caso_bloque1_equipo[X].ipynb`)

- Código funcional con las dos funciones solicitadas
- Análisis paso a paso con comentarios claros
- Resultados de todos los cálculos
- Respuestas a las preguntas de reflexión

### 2. Video de Exposición (YouTube)

- **Duración máxima**: 15 minutos
- **Formato**: Video grabado subido a YouTube (puede ser no listado)
- **Contenido**: Presentación del notebook y explicación de resultados
- **Participación**: Cada integrante debe explicar al menos una parte
- **Envío**: Link de YouTube incluido en el notebook

### IMPORTANTE: Enlace en el Notebook

**Al final de su notebook, en una celda de Markdown claramente identificada, deben incluir:**

```markdown
## Video de Presentación del Equipo

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
| **Fundamentos y Funciones** | 40 | Bucles y conteo (10) + Funciones implementadas (20) + Listas y diccionarios (10) |
| **Análisis y Métricas Básicas** | 30 | Estadísticas básicas (10) + Análisis de jugadores (10) + Introducción pandas (10) |
| **Visualización e Interpretación** | 20 | Visualización básica (15) + Análisis por posición (5) |
| **Comunicación y Documentación** | 10 | Video de exposición (7) + Reflexión final y comentarios (3) + Enlace en notebook |

### Criterios de Desempeño por Componente

#### 1. Fundamentos y Funciones (40 puntos)

**Sobresaliente (40 puntos ~ 100%):**

- Trabajo de nivel profesional que supera las expectativas de preparatoria: código robusto, legible y bien documentado
- Ambas funciones `calcular_puntos` y `mejor_goleador` implementadas con pruebas exhaustivas que incluyen casos borde y validación de entradas
- Uso eficiente y claro de bucles y estructuras de control; manejo explícito de errores y condiciones inesperadas
- Variables descriptivas en español, comentarios pedagógicos y pequeñas notas que facilitan la lectura a terceros
- Manejo cohesionado de listas y diccionarios, con estructura de código preparada para ampliaciones o reuso

**Competente (36 puntos ~ 90%):**

- Código funciona correctamente en su mayoría; pequeñas mejoras de estilo o documentación pendientes
- Ambas funciones `calcular_puntos` y `mejor_goleador` están implementadas y probadas con casos sencillos
- Variables en español y nombres descriptivos, con quizás una o dos excepciones menores
- Manejo correcto de estructuras, aunque puede faltar una validación o un caso borde

**Suficiente (28 puntos ~ 70%):**

- Código funciona con errores menores
- Una función implementada correctamente
- Lógica básica presente
- Algunos errores en manejo de estructuras de datos

**Insuficiente (12 puntos ~ 30%):**

- Código parcialmente funcional
- Errores en lógica pero intento claro
- Falta alguna función o prueba
- Dificultades con bucles o estructuras de datos

**No presentó (0 puntos):**

- Código no funciona o incompleto
- Errores graves de sintaxis
- Funciones faltantes o no implementadas

#### 2. Análisis y Métricas Básicas (30 puntos)

**Sobresaliente (30 puntos ~ 100%):**

- Análisis de nivel profesional: DataFrame bien diseñado, con manejo de tipos, limpieza y comparaciones relevantes
- Estadísticas calculadas con verificaciones y visualizaciones de apoyo; interpretación profunda y conectada con contexto futbolístico
- Análisis de jugadores por posición exhaustivo, con discusión sobre sesgos y limitaciones de los datos
- Ventajas de pandas explicadas con ejemplos reproduci-bles que muestran eficiencia y reproducibilidad
- Resultados presentados de forma clara, replicable y listos para comunicación a terceros

**Competente (27 puntos ~ 90%):**

- DataFrame creado correctamente y usado para la mayoría de los cálculos; pueden faltar comparaciones secundarias
- Estadísticas calculadas correctamente con interpretaciones claras pero no exhaustivas
- Análisis de jugadores por posición presente y correcto, con pequeñas omisiones en la discusión
- Ventajas de pandas expuestas; podría mejorarse la presentación de ejemplos

**Suficiente (21 puntos ~ 70%):**

- DataFrame funcional con análisis básico
- Estadísticas calculadas correctamente
- Interpretación superficial pero presente

**Insuficiente (9 puntos ~ 30%):**

- Intento de DataFrame o análisis estadístico
- Resultados parcialmente correctos
- Poca interpretación o análisis

**No presentó (0 puntos):**

- No logra crear DataFrame o realizar análisis
- Sin estadísticas o cálculos incorrectos
- Sin interpretación de resultados

#### 3. Visualización e Interpretación (20 puntos)

**Sobresaliente (20 puntos ~ 100%):**

- Visualizaciones con calidad publicable: etiquetado impecable, escalas adecuadas y atención a accesibilidad y legibilidad
- Integración entre visualizaciones y narrativa: cada gráfico soporta una conclusión clara y accionable para entrenamiento o táctica
- Análisis por posición profundo, con comparaciones y métricas complementarias que van más allá de la media
- Interpretaciones y recomendaciones fundamentadas, con posibles acciones concretas y métricas para seguimiento

**Competente (18 puntos ~ 90%):**

- Gráficos bien implementados con títulos y etiquetas; pueden mejorarse detalles estéticos o la legibilidad fina
- Visualizaciones claras y útiles para la interpretación, aunque falta un punto adicional de análisis que las conecte con estrategia de equipo
- Análisis por posición desarrollado, con visualizaciones correctas pero sin comparación avanzada
- Recomendaciones basadas en datos sólidas pero breves

**Suficiente (14 puntos ~ 70%):**

- Gráficos básicos pero funcionales
- Interpretación superficial
- Algunas recomendaciones presentes

**Insuficiente (6 puntos ~ 30%):**

- Visualizaciones básicas o incompletas
- Poca interpretación
- Recomendaciones sin fundamento

**No presentó (0 puntos):**

- Sin visualizaciones o no funcionan
- Sin interpretación o análisis
- Sin recomendaciones

#### 4. Comunicación y Documentación (10 puntos)

**Sobresaliente (10 puntos ~ 100%):**

- Presentación de nivel profesional: video claro, bien editado, con narrativa pedagógica y evidencia de revisiones previas
- Participación equilibrada y rol definido para cada integrante; comunicación efectiva y dominio técnico en la exposición
- Reflexión final exhaustiva y bien escrita; comentarios en el código que sirven de guía para docentes y terceros
- Documentación y enlaces impecables; el notebook puede compartirse como recurso público sin ajustes

**Competente (9 puntos ~ 90%):**

- Video claro y bien estructurado dentro del tiempo recomendado; podría mejorar la profesionalidad de la presentación
- Participación equilibrada o con una ligera diferencia entre integrantes
- Reflexión final completa con 3 preguntas respondidas, comentarios en código presentes pero no exhaustivos
- Documentación y enlace en el notebook correctos, con pequeñas mejoras posibles en redacción

**Suficiente (7 puntos ~ 70%):**

- Video básico pero funcional
- Reflexión final presente
- Algunos comentarios en código

**Insuficiente (3 puntos ~ 30%):**

- Video de baja calidad o excede tiempo
- Reflexión final incompleta
- Pocos comentarios explicativos

**No presentó (0 puntos):**

- Sin video o video no accesible
- Sin reflexión final
- Código sin documentación

### Tabla Resumen de Calificación

| Componente | Puntos Máximos | Sobresaliente (~100%) | Competente (~90%) | Suficiente (~70%) | Insuficiente (~30%) | No presentó (0%) |
|------------|-----------------|-------------------|-------------------|---------------------|------------------|
| Fundamentos y Funciones | 40 | 40 puntos | 28 puntos | 12 puntos | 0 puntos |
| Análisis y Métricas Básicas | 30 | 30 puntos | 21 puntos | 9 puntos | 0 puntos |
| Visualización e Interpretación | 20 | 20 puntos | 14 puntos | 6 puntos | 0 puntos |
| Comunicación y Documentación | 10 | 10 puntos | 7 puntos | 3 puntos | 0 puntos |
| **TOTAL** | **100** | **100 puntos** | **70 puntos** | **30 puntos** | **0 puntos** |

### Requisitos Mínimos para Aprobar

- Notebook ejecuta sin errores graves
- Al menos una función implementada correctamente
- DataFrame básico creado y funcionando
- Video subido a YouTube con participación de todo el equipo
- Duración del video menor o igual 20 minutos (máximo absoluto)

### Penalizaciones

- **-5 puntos**: Video excede 20 minutos
- **-3 puntos**: No todos los integrantes participan en el video
- **-5 puntos**: Notebook no ejecuta por errores de sintaxis
- **-2 puntos**: Variables en inglés o nombres no descriptivos

---

## Cronograma de la Semana

| Día | ¿Qué hacer? | Tiempo |
|-----|-------------|--------|
| **Lunes** | Formar equipos, entender el problema | 1 hora |
| **Miércoles** | Escribir código: bucles, funciones, cálculos | 2 horas |
| **Viernes** | Terminar análisis, grabar video de exposición | 1.5 horas |

**Fecha límite de entrega**: 17 de noviembre de 2025, 11:59 PM  
**Recomendación**: Completar durante la semana del 10-14 de noviembre para evitar contratiempos

**Entrega**: Notebook + link de YouTube en Canvas

---

## Consejos Útiles

### Para el Código

- Usen variables con nombres claros: `total_victorias`, `mejor_jugador`
- Comenten su código para explicar qué hace cada parte
- Prueben sus funciones con ejemplos simples primero

### Para el Trabajo en Equipo

- **Persona 1**: Fundamentos básicos, bucles y conteo de resultados
- **Persona 2**: Funciones principales, análisis de jugadores y estadísticas básicas  
- **Persona 3**: DataFrame, visualizaciones y preparación del video
- **Todos**: Participan en interpretaciones y reflexión final

### Para el Video de Exposición

- **Duración**: Practiquen para mantenerse en 12-15 minutos
- **Participación**: Cada persona explica 4-5 minutos
- **Estructura sugerida**:
  - Introducción y datos (2 min)
  - Código y funciones (4-5 min)
  - Análisis y visualizaciones (4-5 min)
  - Resultados y conclusiones (3-4 min)
- **Técnico**: Graben pantalla mostrando el notebook, audio claro
- **Herramientas**: Pueden usar Zoom, OBS, o la grabación de pantalla del sistema operativo

### Preguntas Frecuentes

1. ¿Cómo cuento elementos en una lista? → Usar bucle for con contador
2. ¿Cómo encuentro el máximo en un diccionario? → Usar bucle para comparar valores
3. ¿Cómo calculo promedios? → suma total ÷ cantidad de elementos
4. ¿El video puede ser "no listado" en YouTube? → Sí, pero debe ser accesible con el link
5. ¿Qué pasa si mi función no funciona? → Probar con casos simples y revisar la lógica paso a paso

---

### Autoevaluación Rápida (Marcar OK / Revisar)

**Código y Análisis:**

- [ ] Conté victorias, empates y derrotas correctamente
- [ ] Implementé y probé `calcular_puntos`
- [ ] Implementé y probé `mejor_goleador`
- [ ] Calculé estadísticas básicas del equipo
- [ ] Creé DataFrame y expliqué ventajas sobre listas
- [ ] Generé visualizaciones básicas con títulos y etiquetas
- [ ] Respondí 3 preguntas de reflexión final
- [ ] Comentarios claros e intencionales en el código

**Video de Exposición:**

- [ ] Video dura máximo 15 minutos
- [ ] Cada integrante participa en la explicación
- [ ] Se explica claramente el código y los resultados
- [ ] Audio e imagen son de buena calidad
- [ ] Video subido a YouTube y link funciona

**Entrega:**

- [ ] Notebook ejecuta completamente sin errores
- [ ] Nombres de variables en español
- [ ] Link de YouTube enviado en Canvas

---

*Este caso práctico integra fundamentos técnicos, primeras nociones de pandas, visualización básica y razonamiento reflexivo para cerrar el Bloque 1 de forma completa y significativa.*
