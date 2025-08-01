# Información General

**Tema:** Estructuras de Control en Python  
**Semana:** 2  
**Bloque:** 1 - Prerrequisitos de Programación  
**Tiempo estimado:** 60 minutos  
**Puntos totales:** 100 puntos  
**Fecha límite:** Final de la Semana 2  
**Archivo entrega:****¡Domina las estructuras de control y conviértete en un analista deportivo experto!**`[matricula]-ejercicio-semana-2.ipynb`

## Objetivos de Aprendizaje

Al finalizar este ejercicio, el estudiante será capaz de:

1. **Implementar condicionales** (if, elif, else) para tomar decisiones automáticas
2. **Utilizar bucles** (for, while) para procesar conjuntos de datos deportivos
3. **Aplicar estructuras de control anidadas** para resolver problemas complejos
4. **Procesar listas y diccionarios** usando iteraciones eficientes
5. **Crear sistemas de clasificación** para análisis deportivo automatizado

## Prerrequisitos

- Ejercicio de la Semana 1 completado exitosamente
- Conocimientos básicos de variables y tipos de datos en Python
- Comprensión de operadores de comparación y lógicos
- Python 3.8+ instalado y configurado en Jupyter

## Contexto del Ejercicio

Eres el **analista principal** del Real Madrid. El cuerpo técnico te ha encargado desarrollar un sistema automatizado para:

- Clasificar rendimiento de jugadores según sus estadísticas
- Analizar patrones de victoria/derrota en múltiples partidos
- Generar reportes automáticos de rendimiento del equipo
- Predecir clasificaciones de liga usando simulaciones

---

# Ejercicio Integrador: Sistema de Análisis Automático Real Madrid

## Parte 1: Clasificador de Rendimiento de Jugadores (25 puntos)

### Objetivo
Crear un sistema que clasifique automáticamente el rendimiento de jugadores usando condicionales.

### Instrucciones Detalladas

**Paso 1:** Crea un sistema de clasificación basado en estadísticas:

```python
# Datos de jugadores del Real Madrid
jugadores_real_madrid = [
    {"nombre": "Karim Benzema", "goles": 27, "asistencias": 12, "partidos": 32, "posicion": "Delantero"},
    {"nombre": "Vinicius Jr", "goles": 20, "asistencias": 20, "partidos": 35, "posicion": "Extremo"},
    {"nombre": "Luka Modric", "goles": 3, "asistencias": 12, "partidos": 30, "posicion": "Centrocampista"},
    {"nombre": "Thibaut Courtois", "goles": 0, "asistencias": 0, "partidos": 31, "posicion": "Portero"},
    {"nombre": "David Alaba", "goles": 2, "asistencias": 1, "partidos": 28, "posicion": "Defensa"}
]

# TU CÓDIGO AQUÍ:
# 1. Para cada jugador, calcula su "promedio de contribución" = (goles + asistencias) / partidos
# 2. Clasifica según promedio de contribución:
#    - "Estrella": >= 1.0
#    - "Muy Bueno": >= 0.6  
#    - "Bueno": >= 0.3
#    - "Promedio": < 0.3
# 3. Muestra un reporte detallado para cada jugador
```

### Criterios de Evaluación
- **Cálculos correctos** (10 puntos)
- **Condicionales apropiados** (10 puntos) 
- **Presentación clara** (5 puntos)

---

## Parte 2: Analizador de Patrones de Victoria (25 puntos)

### Objetivo
Usar bucles for para analizar patrones en múltiples partidos y detectar tendencias.

### Instrucciones Detalladas

**Paso 2:** Analiza los últimos 10 partidos del Real Madrid:

```python
# Resultados de los últimos 10 partidos (formato: [rival, goles_rm, goles_rival, local_visitante])
ultimos_partidos = [
    ["Barcelona", 2, 1, "visitante"],
    ["Sevilla", 3, 0, "local"],
    ["Manchester City", 1, 1, "visitante"],
    ["Atletico Madrid", 2, 0, "local"],
    ["Valencia", 2, 2, "visitante"],
    ["Real Sociedad", 4, 1, "local"],
    ["Betis", 1, 0, "visitante"],
    ["Getafe", 3, 0, "local"],
    ["Celta", 2, 1, "local"],
    ["Villarreal", 3, 2, "visitante"]
]

# TU CÓDIGO AQUÍ usando bucle FOR:
# 1. Calcula estadísticas generales:
#    - Total de victorias, empates, derrotas
#    - Goles a favor y en contra
#    - Diferencia de goles promedio
# 2. Analiza rendimiento según ubicación:
#    - Victorias como local vs visitante
#    - Promedio de goles como local vs visitante
# 3. Encuentra el partido más goleador
# 4. Identifica la mejor y peor actuación
```

### Criterios de Evaluación
- **Bucle implementado correctamente** (10 puntos)
- **Cálculos estadísticos precisos** (10 puntos)
- **Análisis de patrones completo** (5 puntos)

---

## Parte 3: Simulador de Clasificación de Liga (25 puntos)

### Objetivo  
Utilizar bucles while para simular la evolución de la tabla de clasificación.

### Instrucciones Detalladas

**Paso 3:** Simula las próximas jornadas de La Liga:

```python
# Clasificación actual (formato: [equipo, puntos, partidos_jugados, diferencia_goles])
clasificacion_actual = [
    ["Real Madrid", 78, 32, 35],
    ["Barcelona", 76, 32, 28], 
    ["Atletico Madrid", 68, 32, 18],
    ["Real Sociedad", 65, 32, 12],
    ["Villarreal", 56, 32, 8]
]

partidos_restantes = 6  # Cada equipo tiene 6 partidos restantes

# TU CÓDIGO AQUÍ usando bucle WHILE:
# 1. Simula que cada equipo gana el 60% de sus partidos restantes
# 2. Por cada victoria, suma 3 puntos y mejora diferencia de goles (+2)
# 3. Por cada no-victoria, suma 1 punto (empate) y mantén diferencia
# 4. Actualiza la tabla después de cada jornada simulada
# 5. Muestra la clasificación final proyectada
# 6. Determina quién será campeón y quiénes van a Champions League (top 4)
```

### Criterios de Evaluación
- **Bucle while correctamente implementado** (10 puntos)
- **Simulación matemáticamente correcta** (10 puntos)
- **Análisis de resultados completo** (5 puntos)

---

## Parte 4: Sistema de Recomendaciones Estratégicas (25 puntos)

### Objetivo
Combinar estructuras de control anidadas para crear un sistema de recomendaciones complejas.

### Instrucciones Detalladas

**Paso 4:** Desarrolla un asistente estratégico para el entrenador:

```python
# Datos del próximo rival
proximo_rival = {
    "nombre": "Manchester City",
    "goles_promedio_casa": 2.8,
    "goles_promedio_fuera": 2.1,
    "defensas_limpias": 15,
    "partidos_jugados": 32,
    "estilo_juego": "posesion",  # opciones: "posesion", "contraataque", "fisico"
    "ubicacion": "visitante"  # donde juega el Real Madrid
}

estado_real_madrid = {
    "jugadores_lesionados": 3,
    "partidos_seguidos": 2,  # partidos consecutivos jugados
    "goles_ultimos_5": [2, 3, 1, 2, 4],  # goles en últimos 5 partidos
    "condicion_fisica": "buena"  # opciones: "excelente", "buena", "regular", "mala"
}

# TU CÓDIGO AQUÍ usando CONDICIONALES ANIDADOS:
# 1. Analiza el nivel de amenaza del rival:
#    - Si promedio > 2.5 goles = "Muy peligroso"
#    - Si promedio > 2.0 goles = "Peligroso"  
#    - Si promedio > 1.5 goles = "Moderado"
#    - Caso contrario = "Manejable"
#
# 2. Evalúa el estado del Real Madrid:
#    - Promedio de goles en últimos 5 partidos
#    - Nivel de fatiga (si partidos_seguidos > 2)
#    - Disponibilidad de jugadores
#
# 3. Genera recomendación estratégica:
#    - Formación recomendada (defensiva/equilibrada/ofensiva)
#    - Estilo de juego sugerido
#    - Predicción de resultado
#    - Recomendaciones específicas
```

### Criterios de Evaluación
- **Lógica de condicionales anidados** (10 puntos)
- **Análisis estratégico coherente** (10 puntos)
- **Recomendaciones prácticas** (5 puntos)

---

# Criterios de Evaluación Total

## Distribución de Puntos (100 total)

### 1. Correctitud Técnica (40 puntos)
- **Sintaxis Python perfecta:** Sin errores de ejecución
- **Condicionales apropiados:** Uso correcto de if, elif, else
- **Bucles eficientes:** Implementación correcta de for y while
- **Cálculos precisos:** Operaciones matemáticas exactas

### 2. Aplicación Práctica (30 puntos)  
- **Resolución completa:** Todos los problemas resueltos
- **Contexto deportivo:** Uso apropiado del análisis futbolístico
- **Innovación:** Soluciones creativas y eficientes
- **Integración:** Combinación efectiva de conceptos

### 3. Claridad y Documentación (30 puntos)
- **Código comentado:** Explicaciones claras de la lógica
- **Variables descriptivas:** Nombres en español y apropiados
- **Presentación profesional:** Outputs claros y bien formateados
- **Interpretación:** Análisis correcto de los resultados

---

# Instrucciones de Entrega

## Lista de Verificación

Antes de entregar, asegúrate de:

1. **✅ Completar las 4 partes** del ejercicio integrador
2. **✅ Ejecutar todo el código** sin errores
3. **✅ Incluir comentarios explicativos** en español
4. **✅ Usar nombres de variables descriptivos** en español
5. **✅ Mostrar resultados claramente formateados**

## Formato de Entrega

- **Nombre del archivo:** `[matricula]-ejercicio-semana-2.ipynb`
- **Formato:** Jupyter Notebook ejecutado completamente
- **Fecha límite:** Final de la Semana 2
- **Método:** Subir a la plataforma del curso

## Recursos de Apoyo

- **Notebook principal:** `bloque-1/semana-2/estructuras-control.ipynb`
- **Documentación Python:** [Control Flow](https://docs.python.org/3/tutorial/controlflow.html)
- **Rúbrica detallada:** `evaluaciones/bloque-1/rubrica-unificada-bloque1.md`

---

**¡Domina las estructuras de control y conviértete en un analista deportivo experto!** ⚽�
