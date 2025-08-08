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

### Datos de Partidos (lista simple):
```python
resultados_partidos = ["Victoria", "Derrota", "Victoria", "Empate", "Victoria", 
                      "Derrota", "Victoria", "Empate", "Victoria", "Victoria"]

goles_favor = [2, 0, 3, 1, 2, 0, 1, 2, 3, 2]
goles_contra = [1, 3, 1, 1, 0, 2, 0, 2, 1, 1]
```

### Datos de Jugadores (diccionario simple):
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

### Parte 1: Python Básico (50 puntos)

#### 1.1 Contar Resultados con Bucles (15 puntos)
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

#### 1.3 Trabajar con Listas y Diccionarios (15 puntos)
- Calcular total de goles a favor usando la lista `goles_favor`
- Encontrar el partido con más goles usando funciones básicas
- Usar el diccionario `jugadores` para encontrar información básica

### Parte 2: Análisis Simple (30 puntos)

#### 2.1 Estadísticas Básicas del Equipo (15 puntos)
- Usar las funciones que crearon para calcular puntos totales
- Calcular el promedio de goles por partido (total goles ÷ partidos)
- Determinar si el equipo marcó más goles de los que recibió

#### 2.2 Análisis de Jugadores (15 puntos)  
- Usar su función para encontrar el mejor goleador
- Contar cuántos delanteros hay en el equipo
- Calcular el total de goles marcados por todos los jugadores

### Parte 3: Presentación Simple (20 puntos)

#### 3.1 Notebook Limpio (10 puntos)
- Código funciona sin errores
- Comentarios explicando qué hace cada parte
- Estructura clara paso a paso

#### 3.2 Presentación Grupal (10 puntos)
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

## Criterios de Evaluación

### Rúbrica Simplificada (100 puntos total)

| Criterio | Puntos | ¿Qué evalúo? |
|----------|---------|--------------|
| **Python Básico** | 50 | ¿Funcionan los bucles, if, y operaciones básicas? |
| **Funciones** | 30 | ¿Crearon las 2 funciones solicitadas correctamente? |
| **Presentación** | 20 | ¿Explicaron claramente sus resultados? |

### Lo que Busco en Cada Parte:

#### Python Básico (50 puntos):
- **Excelente (45-50):** Todo el código funciona, usan bucles e if correctamente
- **Bueno (40-44):** Código funciona con errores pequeños
- **Suficiente (35-39):** Código funciona pero con algunos problemas
- **Insuficiente (<35):** Código no funciona o tiene errores graves

#### Funciones (30 puntos):
- **Excelente (27-30):** Las 2 funciones están bien hechas y funcionan
- **Bueno (24-26):** 1 función perfecta, 1 con pequeños errores
- **Suficiente (21-23):** Las funciones funcionan pero tienen errores
- **Insuficiente (<21):** Las funciones no funcionan o faltan

---

## Cronograma de la Semana

| Día | ¿Qué hacer? | Tiempo |
|-----|-------------|--------|
| **Lunes** | Formar equipos, entender el problema | 1 hora |
| **Miércoles** | Escribir código: bucles, funciones, cálculos | 2 horas |
| **Viernes** | Terminar análisis y presentar resultados | 1 hora |

---

## Consejos Útiles

### Para el Código:
- Usen variables con nombres claros: `total_victorias`, `mejor_jugador`
- Comenten su código para explicar qué hace cada parte
- Prueben sus funciones con ejemplos simples primero

### Para el Trabajo en Equipo:
- Una persona se encarga de los bucles
- Otra persona se encarga de las funciones  
- Todos participan en el análisis final

### Preguntas Frecuentes:
1. ¿Cómo cuento elementos en una lista? → Usar bucle for
2. ¿Cómo encuentro el máximo en un diccionario? → Usar bucle para comparar valores
3. ¿Cómo calculo promedios? → suma total ÷ cantidad

---

*¡Este caso práctico les ayudará a aplicar lo básico de Python (variables, bucles, funciones) con datos de fútbol!*