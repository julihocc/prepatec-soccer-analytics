# Caso Práctico Colaborativo - Bloque 1

## Análisis Básico de un Equipo de Fútbol

**Modalidad:** Colaborativa (equipos de 2-3 estudiantes)  
**Ponderación:** 15% del 1er Parcial  
**Duración:** 1 semana  
**Entrega:** Notebook de Jupyter + presentación simple

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

## Entregables

### 1. Notebook de Jupyter (`caso_bloque1_equipo[X].ipynb`)

- Código funcional con las dos funciones solicitadas
- Análisis paso a paso con comentarios
- Resultados de todos los cálculos

### 2. Presentación Simple (`presentacion_equipo[X].pdf`)

- 3-4 diapositivas máximo
- Sus resultados principales
- Explicación de qué aprendieron

---

## Criterios de Evaluación (Rúbrica Completa Integrada)

Esta sección fusiona la rúbrica completa del Bloque 1 dentro del caso práctico (el archivo independiente ha sido retirado para simplificar la consulta). Mantiene el modelo estándar 40/30/30 y añade configuraciones del Examen Canvas para referencia global del bloque.

### 1. Examen Canvas (Referencia del Bloque)

- Banco total: 120 preguntas (Core 1–75, Extended 76–120).
- Preguntas por examen: 22 (muestreo estratificado objetivo: [R] 7-8, [C] 7-8, [A] 5-6, [S] 1-2).
- Formato: ~70% opción múltiple / ~30% numéricas (tolerancia 5%).
- Tiempo límite: 50 minutos. Intento único.
- Segmentación: Uso principal Core (≥80%) + Extended para variabilidad e interpretación ([S]).
- Temas 20% c/u: Variables y tipos, estructuras de control, funciones/modularidad, introducción pandas, visualización básica.

### 2. Caso Práctico Colaborativo (Este Documento)

Ponderación: 15% del curso. Equipos de 2–3 estudiantes. Semana de desarrollo.

### 3. Rúbrica 40 / 30 / 30 (100 puntos totales)

| Área | Puntos | Subcomponentes | Evidencia clave |
|------|--------|----------------|-----------------|
| Fundamentos de Código | 40 | Variables y estructuras (15) + Bucles y condicionales (15) + Funciones simples (10) | Código limpio, nombres descriptivos, lógica correcta, asserts |
| Análisis Básico | 30 | Cálculos (puntos, promedios, diferencia goles) (15) + Análisis jugadores (10) + Primera visualización / DataFrame (5) | Resultados correctos explicados |
| Comunicación y Colaboración | 30 | Comentarios y claridad (10) + Reflexiones fundamentadas (10) + Roles y presentación (10) | Justificaciones, roles visibles, coherencia estilo |

### 4. Criterios de Desempeño Detallados

#### 4.1 Fundamentos y Funciones (40)

- Excelente (36–40): Código sin errores, funciones probadas con `assert`, nombres descriptivos y comentarios intencionales.
- Bueno (32–35): Funciona; mínimos detalles de claridad.
- Suficiente (28–31): Funciona con errores lógicos menores o ausencia de alguna prueba.
- Insuficiente (<28): Errores graves o funciones incompletas.

#### 4.2 Análisis y Visualización (30)

- Excelente (27–30): Estadísticas correctas, DataFrame claro, gráfico legible + interpretación breve.
- Bueno (24–26): Cálculos correctos, interpretación superficial.
- Suficiente (21–23): Cálculos parcialmente correctos o visualización sin explicación.
- Insuficiente (<21): Cálculos erróneos o falta de evidencia visual.

#### 4.3 Comunicación y Razonamiento (30)

- Excelente (27–30): Presentación clara, responde preguntas reflexivas con justificación, 2 conclusiones + 1 limitación explícita.
- Bueno (24–26): Presentación clara, reflexión breve.
- Suficiente (21–23): Presentación básica, reflexión incompleta.
- Insuficiente (<21): Falta reflexión o incoherente.

### 5. Requisitos Transversales para Nivel Excelente

- Variables en español y descriptivas.
- Preguntas de reflexión respondidas en cada parte.
- Comentarios explican intención (no repiten el código literal).
- Notebook ejecuta de inicio a fin sin errores.

### 6. Integridad Académica (Aplicada a Examen y Caso)

| Componente | Examen Canvas | Caso Práctico |
|------------|---------------|---------------|
| Autoría | Individual | Colaborativa (80% código original del equipo) |
| Material externo | Limitado según instrucciones | Referencias citadas si se usan |
| IA Asistiva | Declarar si se usó (breve nota) | Declarar rol de la IA (no sustituye autoría) |
| Intentos | 1 | Iterativo con checkpoint interno |

### 7. Autoevaluación Rápida (Marcar OK / Revisar)

- [ ] Conté victorias, empates y derrotas correctamente
- [ ] Implementé y probé `calcular_puntos`
- [ ] Implementé y probé `mejor_goleador`
- [ ] Calculé promedios y diferencia de goles
- [ ] Creé DataFrame y expliqué ventaja sobre listas
- [ ] Generé gráfico barras goles a favor vs contra
- [ ] Respondí 3 preguntas de reflexión final
- [ ] Comentarios claros e intencionales
- [ ] Roles de equipo visibles

### 8. Conversión de Calificaciones (Bloque 1)

- Examen Canvas: 20% × (puntaje/100)
- Caso práctico: 15% × (puntaje/100)
- Total Bloque 1 = suma ponderada (35% del curso)

### 9. Notas de Alcance

- No se exige manejo avanzado de errores o programación orientada a objetos.
- No añadir librerías fuera del stack básico (pandas, matplotlib opcional, numpy implícito).
- Mantener tiempos: Caso debe poder repasarse en <15 min por equipo al presentar.

---

## Cronograma de la Semana

| Día | ¿Qué hacer? | Tiempo |
|-----|-------------|--------|
| **Lunes** | Formar equipos, entender el problema | 1 hora |
| **Miércoles** | Escribir código: bucles, funciones, cálculos | 2 horas |
| **Viernes** | Terminar análisis y presentar resultados | 1 hora |

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

### Preguntas Frecuentes

1. ¿Cómo cuento elementos en una lista? → Usar bucle for
2. ¿Cómo encuentro el máximo en un diccionario? → Usar bucle para comparar valores
3. ¿Cómo calculo promedios? → suma total ÷ cantidad

---

### 3. Reflexión Final (en el notebook)

Responder brevemente (2–4 líneas cada una) a TRES preguntas de las siguientes cinco opciones:

1. ¿Qué métrica adicional incluirías para evaluar solidez defensiva y por qué?
2. ¿Qué limitación tiene usar solo 10 partidos para conclusiones?
3. ¿Qué beneficio te dio el DataFrame frente a listas separadas?
4. ¿Qué mostrarías a un entrenador para convencerlo de mejorar el ataque?
5. ¿Cuál sería tu siguiente paso de análisis en el Bloque 2?

*Este caso práctico integra fundamentos técnicos, primeras nociones de pandas, visualización básica y razonamiento reflexivo para cerrar el Bloque 1 de forma completa y significativa.*
