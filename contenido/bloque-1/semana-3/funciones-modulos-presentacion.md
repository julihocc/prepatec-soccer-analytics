---
marp: true
theme: default
paginate: true
class: lead
---

# Semana 3: Sistemas elegantes y reutilizables en análisis de fútbol

**Curso de Ciencia de Datos aplicada al Fútbol (Preparatoria)**

---

# SESIÓN 1: ¿Cómo diseñamos jugadas maestras reutilizables? (50 min)

---

## Pregunta guía

¿Qué hace especial a una jugada maestra? ¿Por qué los grandes entrenadores tienen "manuales de jugadas"?

---

- ¿Cómo puedes crear tu propio sistema de análisis en Python?

---

## Teoría: Funciones en Python

¿Cómo diseñar funciones que puedas usar en cualquier situación?

---

## Ejemplo: Análisis de efectividad goleadora

```python
def calcular_promedio_goles(goles_totales, partidos_jugados):
    if partidos_jugados == 0:
        return 0
    return goles_totales / partidos_jugados

print(calcular_promedio_goles(36, 35))  # Haaland
```

---

¿Por qué es importante validar los datos antes de calcular?

---

## Práctica: Crea tu jugada maestra para porteros

¿Qué información necesitas para evaluar a un portero?

---

¿Cómo evitarías errores como división por cero?

---

## Funciones avanzadas: análisis multidimensional

¿Cómo evaluarías a un jugador considerando goles, asistencias y posición?

---

¿Por qué no todos los jugadores deben evaluarse igual?

---

## Ejemplo: Evaluación integral de jugadores

```python
def analizar_rendimiento_jugador(nombre, goles, asistencias, partidos, posicion):
    if partidos == 0:
        return f"{nombre}: Sin datos"
    goles_por_partido = goles / partidos
    if posicion == "delantero" and goles_por_partido >= 0.8:
        return "ÉLITE MUNDIAL"
    # ...más lógica según posición...
```

---

¿Por qué es clave contextualizar los números según el rol?

---

## Síntesis de la sesión 1

- ¿Qué ventajas tiene usar funciones para evitar repetir código?
- ¿Cómo ayuda esto a pensar como un estratega?

---

# SESIÓN 2: ¿Cómo aprovechamos herramientas de expertos? (50 min)

---

## Pregunta guía

¿Por qué los grandes clubes no reinventan todo? ¿Qué ventajas tiene usar herramientas creadas por expertos?

---

## Teoría: Módulos en Python

¿Qué módulos conoces que te ayuden a analizar datos deportivos?

---

## Ejemplo: Usando módulos profesionales

```python
import math

def calcular_distancia(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(calcular_distancia(5, 50, 95, 55))
```

---

## Importaciones: diferentes estilos según la situación

- import math
- import math as mat
- from math import sqrt

---

¿En qué casos usarías cada estilo?

---

## Práctica: Crea tu propio módulo

¿Qué cálculos haces repetidamente?

---

¿Cómo organizarías tus funciones por especialidad?

---

## Ejemplo: Departamento de análisis personalizado

```python
def calcular_puntos_equipo(victorias, empates, derrotas):
    return victorias * 3 + empates

def analizar_forma_equipo(ultimos_resultados):
    # ...lógica para analizar racha...
    pass
```

---

¿Qué otras funciones añadirías para un análisis más completo?

---

## Síntesis de la sesión 2

- ¿Qué ventajas tiene organizar tus herramientas en módulos?
- ¿Cómo te ayuda esto a pensar como un club profesional?

---

# SESIÓN 3: ¿Cómo integramos todo en un sistema profesional? (50 min)

---

## Pregunta guía

¿Cómo integrarías funciones y módulos para analizar equipos reales?

---

- Integra funciones y módulos para analizar equipos reales
- Presenta resultados como un analista profesional

---

## Proyecto integrador: sistema de análisis profesional

(Desarrolla un pequeño sistema que use funciones y módulos para analizar datos de un equipo)

---

## Síntesis y reflexión

- ¿Qué ventajas tiene organizar tu código en funciones y módulos?
- ¿Cómo te ayuda esto a pensar como un estratega?
- ¿Qué aprendiste sobre la reutilización y la especialización?

---

# Preguntas para tu autoevaluación

- ¿Podrías explicar a un compañero qué es una función usando solo analogías futbolísticas?
- ¿Cómo aprovecharías módulos creados por otros expertos?
- ¿Qué te gustaría automatizar en tu propio análisis deportivo?

---

# Próxima semana

- Visualización de datos y análisis estadístico avanzado
- Creación de reportes profesionales

**¿Listo para el siguiente nivel?**
