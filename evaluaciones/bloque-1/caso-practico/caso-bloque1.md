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

```python
# Definir las listas de datos (ya proporcionadas arriba)
resultados_partidos = ["Victoria", "Derrota", "Victoria", "Empate", "Victoria", 
                      "Derrota", "Victoria", "Empate", "Victoria", "Victoria"]

# Su código aquí: contar cada tipo de resultado
victorias = 0
empates = 0  
derrotas = 0

# Usar bucle for e if para contar
```

Pregunta de reflexión: ¿Qué patrón observas entre victorias y empates? ¿Qué podría significar esto sobre la consistencia del equipo?

#### 1.2 Crear Funciones Simples (20 puntos)

Escribir estas 2 funciones obligatorias:

**a) Función para calcular puntos:**

```python
def calcular_puntos(victorias, empates):
    """Calcula puntos: Victoria=3, Empate=1"""
    # Su código aquí
    return total_puntos
```

**b) Función para encontrar mejor goleador:**

```python
def mejor_goleador(jugadores):
    """Encuentra quién marcó más goles"""
    # Su código aquí
    return nombre_mejor, goles_mejor
```

Añade al final de cada función una prueba mínima (asegura funcionamiento):

```python
assert calcular_puntos(5, 2) == 17  # 5*3 + 2*1
```

**Pregunta de reflexión:** ¿Por qué es útil probar una función con un caso simple antes de usarla en todo el análisis? ¿Qué te da confianza sobre tu código?

#### 1.3 Trabajar con Listas y Diccionarios (10 puntos)

- Calcular total de goles a favor usando la lista `goles_favor`
- Encontrar el partido con más goles usando funciones básicas
- Usar el diccionario `jugadores` para encontrar información básica

**Pregunta de reflexión:** ¿Qué limitación notas al manejar varias listas separadas para analizar partidos? ¿Cómo crees que esto afectaría si tuvieras 100 partidos?

### Parte 2: Análisis y Visualización (30 puntos)

#### 2.1 Estadísticas Básicas del Equipo (10 puntos)

- Usar las funciones que crearon para calcular puntos totales
- Calcular el promedio de goles por partido (total goles ÷ partidos)
- Determinar si el equipo marcó más goles de los que recibió

**Pregunta de reflexión:** ¿El promedio de goles refleja toda la historia del rendimiento ofensivo? ¿Qué información importante NO te dice este número?

#### 2.2 Análisis de Jugadores (10 puntos)  

- Usar su función para encontrar el mejor goleador
- Contar cuántos delanteros hay en el equipo
- Calcular el total de goles marcados por todos los jugadores

**Pregunta de reflexión:** ¿Ser el máximo goleador implica automáticamente mayor impacto para el equipo? ¿Qué otros datos considerarías para evaluar la contribución real de un jugador?

#### 2.3 Mini Introducción a pandas (5 puntos)

Construyan un DataFrame simple para unificar los datos y comparar ventajas respecto a listas:

```python
import pandas as pd
datos_partidos = pd.DataFrame({
    'partido': range(1, len(goles_favor)+1),
    'resultado': resultados_partidos,
    'goles_favor': goles_favor,
    'goles_contra': goles_contra
})

promedio_goles_df = datos_partidos['goles_favor'].mean()
print("Promedio goles (DataFrame):", promedio_goles_df)
```

**Pregunta de reflexión:** ¿Qué ventaja concreta te da el DataFrame frente a manejar tres listas independientes? ¿En qué situaciones crees que esta diferencia sería aún más importante?

#### 2.4 Visualización Básica (5 puntos)

Crear un gráfico de barras comparando goles a favor y en contra por partido:

```python
import matplotlib.pyplot as plt
partidos = range(1, len(goles_favor)+1)
plt.bar(partidos, goles_favor, label='Goles a favor')
plt.bar(partidos, goles_contra, label='Goles en contra', alpha=0.7)
plt.xlabel('Partido')
plt.ylabel('Goles')
plt.title('Rendimiento ofensivo y defensivo')
plt.legend()
plt.show()
```

**Pregunta de reflexión:** ¿En qué partidos la diferencia fue mayor? ¿Qué hipótesis podrías proponer sobre el rendimiento del equipo en esos momentos específicos?

### Parte 3: Comunicación y Razonamiento (30 puntos)

#### 3.1 Notebook Limpio y Explicado (15 puntos)

- Código funciona sin errores
- Comentarios explicando qué hace cada parte
- Estructura clara paso a paso

#### 3.2 Presentación y Reflexión Grupal (15 puntos)

- 5 minutos máximo por equipo
- Mostrar sus resultados principales
- Cada integrante explica una parte

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

**Distribución**: 60% Desarrollo Técnico + 40% Comunicación y Reflexión

| Componente | Puntos | Criterios de Evaluación |
|------------|--------|------------------------|
| **Código y Funciones** | 35 | Bucles y conteo correcto (10) + Funciones implementadas y probadas (15) + Cálculos estadísticos (10) |
| **Análisis con Datos** | 25 | DataFrame y comparación con listas (10) + Visualización básica (10) + Interpretación de resultados (5) |
| **Video de Exposición** | 25 | Claridad en explicación (10) + Participación equilibrada del equipo (8) + Manejo del tiempo (≤15 min) (7) + Enlace en notebook |
| **Reflexión y Documentación** | 15 | Preguntas reflexivas intermedias (7) + Reflexión final (3) + Comentarios claros en código (5) |

### Criterios de Desempeño por Componente

#### 1. Código y Funciones (35 puntos)

**Excelente (35 puntos ~ 100%):**
- Bucle for cuenta correctamente victorias, empates y derrotas
- Funciones `calcular_puntos` y `mejor_goleador` implementadas y funcionan
- Incluye pruebas con `assert`
- Variables con nombres descriptivos en español

**Suficiente (25 puntos ~ 70%):**
- Código funciona con errores menores
- Una función implementada correctamente
- Lógica básica presente

**Insuficiente (11 puntos ~ 30%):**
- Código parcialmente funcional
- Errores en lógica pero intento claro
- Falta alguna función o prueba

**No presentó (0 puntos):**
- Código no funciona o incompleto
- Errores graves de sintaxis
- Funciones faltantes

#### 2. Análisis con Datos (25 puntos)

**Excelente (25 puntos ~ 100%):**
- DataFrame creado correctamente
- Explica ventajas vs listas
- Gráfico de barras legible con etiquetas
- Interpreta resultados correctamente

**Suficiente (18 puntos ~ 70%):**
- DataFrame funcional
- Gráfico básico presente
- Interpretación superficial

**Insuficiente (8 puntos ~ 30%):**
- Intento de DataFrame o visualización
- Resultados parcialmente correctos
- Poca interpretación

**No presentó (0 puntos):**
- No logra crear DataFrame
- Sin visualización o incorrecta
- Sin interpretación

#### 3. Video de Exposición (25 puntos)

**Excelente (25 puntos ~ 100%):**
- Explicación clara de código y resultados
- Cada integrante participa equitativamente
- Tiempo ≤15 minutos
- Buen manejo del notebook durante presentación

**Suficiente (18 puntos ~ 70%):**
- Explicación clara pero participación desigual
- Tiempo adecuado
- Presentación organizada

**Insuficiente (8 puntos ~ 30%):**
- Explicación básica
- Participación mínima de algunos integrantes
- Excede tiempo ligeramente (16-18 min)

**No presentó (0 puntos):**
- Explicación confusa o incompleta
- Solo una persona presenta
- Excede significativamente el tiempo (>18 min)
- Video de mala calidad o inaudible

#### 4. Reflexión y Documentación (15 puntos)

**Excelente (15 puntos ~ 100%):**
- Responde todas las preguntas reflexivas intermedias con profundidad
- Completa reflexión final con 3 preguntas (análisis detallado)
- Comentarios explican el "por qué", no solo el "qué"
- Conexiones claras entre conceptos

**Suficiente (11 puntos ~ 70%):**
- Responde la mayoría de preguntas reflexivas
- Reflexión final básica pero presente
- Comentarios básicos pero útiles

**Insuficiente (5 puntos ~ 30%):**
- Respuestas superficiales a preguntas reflexivas
- Reflexión final incompleta o muy breve
- Comentarios mínimos

**No presentó (0 puntos):**
- No responde preguntas reflexivas intermedias
- Falta reflexión final o comentarios inútiles

### Tabla Resumen de Calificación

| Componente | Puntos Máximos | Excelente (~100%) | Suficiente (~70%) | Insuficiente (~30%) | No presentó (0%) |
|------------|-----------------|-------------------|-------------------|---------------------|------------------|
| Código y Funciones | 35 | 35 puntos | 25 puntos | 11 puntos | 0 puntos |
| Análisis con Datos | 25 | 25 puntos | 18 puntos | 8 puntos | 0 puntos |
| Video de Exposición | 25 | 25 puntos | 18 puntos | 8 puntos | 0 puntos |
| Reflexión y Documentación | 15 | 15 puntos | 11 puntos | 5 puntos | 0 puntos |
| **TOTAL** | **100** | **100 puntos** | **72 puntos** | **32 puntos** | **0 puntos** |

### Requisitos Mínimos para Aprobar

- Notebook ejecuta sin errores graves
- Al menos una función implementada correctamente
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

- Una persona se encarga de los bucles
- Otra persona se encarga de las funciones  
- Todos participan en el análisis final

### Para el Video de Exposición

- **Duración**: Practiquen para mantenerse en 12-15 minutos
- **Participación**: Cada persona explica 4-5 minutos
- **Estructura sugerida**: Introducción (1 min) + Código (8-10 min) + Resultados (4-5 min) + Conclusiones (1-2 min)
- **Técnico**: Graben pantalla mostrando el notebook, audio claro
- **Herramientas**: Pueden usar Zoom, OBS, o la grabación de pantalla del sistema operativo

### Preguntas Frecuentes

1. ¿Cómo cuento elementos en una lista? → Usar bucle for
2. ¿Cómo encuentro el máximo en un diccionario? → Usar bucle para comparar valores
3. ¿Cómo calculo promedios? → suma total ÷ cantidad
4. ¿El video puede ser "no listado" en YouTube? → Sí, pero debe ser accesible con el link

---

### Autoevaluación Rápida (Marcar OK / Revisar)

**Código y Análisis:**
- [ ] Conté victorias, empates y derrotas correctamente
- [ ] Implementé y probé `calcular_puntos`
- [ ] Implementé y probé `mejor_goleador`
- [ ] Calculé promedios y diferencia de goles
- [ ] Creé DataFrame y expliqué ventaja sobre listas
- [ ] Generé gráfico barras goles a favor vs contra
- [ ] Respondí 3 preguntas de reflexión final
- [ ] Comentarios claros e intencionales

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
