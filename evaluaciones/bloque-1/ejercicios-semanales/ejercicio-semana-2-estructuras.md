# Ejercicio Semana 2: Estructuras de Datos y Control de Flujo

## Información del Ejercicio

**Bloque:** 1 - Prerrequisitos de Programación  
**Peso:** 12% de la calificación del bloque (60% ÷ 5 ejercicios)  
**Tiempo estimado:** 1-2 horas  
**Entrega:** Final de Semana 2

## Objetivos

Al completar este ejercicio, serás capaz de:
- Crear y manipular listas con datos deportivos
- Usar diccionarios para almacenar información estructurada de jugadores y equipos
- Implementar bucles for y while para análisis iterativo
- Aplicar condicionales para categorizar y filtrar datos deportivos

## Ejercicio 1: Listas de Equipos (20 puntos)

### Instrucciones
Trabaja con listas de equipos de diferentes ligas europeas:

```python
# Listas de equipos por liga
la_liga = ["Barcelona", "Real Madrid", "Atletico Madrid", "Valencia", "Sevilla"]
premier_league = ["Manchester City", "Liverpool", "Chelsea", "Arsenal", "Manchester United"]
bundesliga = ["Bayern Munich", "Borussia Dortmund", "RB Leipzig", "Bayer Leverkusen"]

# Tu código aquí:
# 1. Combinar todas las listas en una sola llamada "todos_equipos"
# 2. Mostrar el total de equipos
# 3. Agregar "Paris Saint-Germain" a la lista combinada
# 4. Eliminar "RB Leipzig" de la lista combinada
# 5. Mostrar los primeros 3 y últimos 3 equipos
# 6. Verificar si "Barcelona" está en la lista
```

### Tu Respuesta
*Completa el código para todas las operaciones con listas.*

## Ejercicio 2: Diccionarios de Jugadores (20 puntos)

### Instrucciones
Crea y manipula diccionarios con información de jugadores:

```python
# Crear diccionarios de jugadores
messi = {
    "nombre": "Lionel Messi",
    "equipo": "Inter Miami",
    "posicion": "Delantero",
    "edad": 36,
    "goles_temporada": 12,
    "asistencias": 8
}

# Tu código aquí:
# 1. Crear un diccionario similar para Cristiano Ronaldo (Al-Nassr, Delantero, 39 años, 15 goles, 3 asistencias)
# 2. Crear un diccionario para Kylian Mbappé (Real Madrid, Delantero, 25 años, 18 goles, 6 asistencias)
# 3. Crear una lista llamada "jugadores" que contenga los 3 diccionarios
# 4. Mostrar el nombre y goles de cada jugador
# 5. Calcular el total de goles entre los 3 jugadores
# 6. Determinar quién tiene más asistencias
```

### Tu Respuesta
*Completa el código para crear y manipular los diccionarios de jugadores.*

## Ejercicio 3: Análisis con Bucles For (20 puntos)

### Instrucciones
Usa bucles para analizar datos de múltiples partidos:

```python
# Lista de resultados de partidos (formato: [equipo_local, goles_local, equipo_visitante, goles_visitante])
partidos = [
    ["Barcelona", 3, "Real Madrid", 1],
    ["Manchester City", 2, "Liverpool", 2],
    ["Bayern Munich", 4, "Borussia Dortmund", 1],
    ["Paris Saint-Germain", 1, "Olympique Lyon", 0],
    ["Juventus", 2, "AC Milan", 3]
]

# Tu código aquí usando bucles for:
# 1. Mostrar el resultado de cada partido en formato: "Barcelona 3-1 Real Madrid"
# 2. Contar cuántos partidos ganó el equipo local
# 3. Contar cuántos partidos fueron empates
# 4. Calcular el total de goles marcados en todos los partidos
# 5. Encontrar el partido con más goles
# 6. Crear una lista con solo los nombres de los equipos ganadores
```

### Tu Respuesta
*Completa el código usando bucles for para analizar todos los partidos.*

## Ejercicio 4: Clasificación con Bucles While (20 puntos)

### Instrucciones
Simula un sistema de clasificación usando bucles while:

```python
# Datos de equipos: [nombre, puntos_actuales, partidos_restantes]
equipos_liga = [
    ["Barcelona", 45, 5],
    ["Real Madrid", 43, 5], 
    ["Atletico Madrid", 38, 5],
    ["Valencia", 35, 5],
    ["Sevilla", 32, 5]
]

# Tu código aquí usando while:
# 1. Crear una función que simule ganar partidos (3 puntos por victoria)
# 2. Simular que cada equipo gana la mitad de sus partidos restantes (redondear hacia abajo)
# 3. Actualizar los puntos de cada equipo
# 4. Ordenar la lista por puntos (puedes usar el método sort o hacer ordenamiento manual)
# 5. Mostrar la clasificación final
# 6. Determinar el campeón y los equipos en puestos europeos (top 4)
```

### Tu Respuesta
*Completa el código usando bucles while para simular la temporada.*

## Ejercicio 5: Análisis Condicional Avanzado (20 puntos)

### Instrucciones
Categoriza equipos y jugadores usando condicionales complejos:

```python
# Estadísticas de equipos
equipos_stats = [
    {"nombre": "Barcelona", "goles_favor": 68, "goles_contra": 35, "partidos": 30},
    {"nombre": "Manchester City", "goles_favor": 89, "goles_contra": 31, "partidos": 32},
    {"nombre": "Bayern Munich", "goles_favor": 92, "goles_contra": 38, "partidos": 28},
    {"nombre": "Paris Saint-Germain", "goles_favor": 75, "goles_contra": 28, "partidos": 30}
]

# Tu código aquí usando condicionales:
# 1. Para cada equipo, calcular:
#    - Promedio de goles por partido
#    - Diferencia de goles (favor - contra)
#    - Eficiencia defensiva (goles_contra / partidos)

# 2. Categorizar cada equipo según su promedio de goles:
#    - "Muy ofensivo": >= 2.5 goles por partido
#    - "Ofensivo": >= 2.0 goles por partido  
#    - "Equilibrado": >= 1.5 goles por partido
#    - "Defensivo": < 1.5 goles por partido

# 3. Categorizar según eficiencia defensiva:
#    - "Muy sólido": <= 1.0 goles contra por partido
#    - "Sólido": <= 1.3 goles contra por partido
#    - "Regular": <= 1.6 goles contra por partido
#    - "Vulnerable": > 1.6 goles contra por partido

# 4. Crear un reporte completo para cada equipo
```

### Tu Respuesta
*Completa el análisis condicional para categorizar todos los equipos.*

## Ejercicio Bonus: Simulador de Torneo (10 puntos extra)

### Instrucciones
**Ejercicio opcional para puntos adicionales:**

```python
# Crear un simulador básico de torneo eliminatorio
import random

equipos_torneo = ["Barcelona", "Real Madrid", "Manchester City", "Bayern Munich"]

# Tu código aquí:
# 1. Simular partidos entre equipos (usar random para generar goles)
# 2. Implementar sistema de eliminación directa
# 3. Mostrar resultados de cada ronda
# 4. Determinar el campeón del torneo
# 5. Mostrar estadísticas del torneo (total de goles, partido más emocionante, etc.)
```

### Tu Respuesta
*Ejercicio opcional: Crea un simulador completo de torneo.*

## Criterios de Evaluación

### Correctitud Técnica (40%)
- [ ] Listas: Creación, manipulación y operaciones correctas (10%)
- [ ] Diccionarios: Uso apropiado para datos estructurados (10%)
- [ ] Bucles: Implementación correcta de for y while (10%)
- [ ] Condicionales: Lógica apropiada para categorización (10%)

### Aplicación Práctica (30%)
- [ ] Análisis deportivo relevante y lógico (15%)
- [ ] Resolución completa de problemas planteados (15%)

### Claridad y Presentación (30%)
- [ ] Código bien comentado y estructurado (15%)
- [ ] Resultados claramente presentados (15%)

## Instrucciones de Entrega

1. **Completa todos los ejercicios** en este notebook
2. **Ejecuta todas las celdas** y verifica resultados
3. **Guarda como:** `ejercicio-semana-2-[tu-apellido].ipynb`
4. **Entrega antes del final de Semana 2**

## Recursos de Apoyo

- Notebook de la Semana 2: `estructuras-control.ipynb`
- Documentación de Python: Listas y diccionarios
- Tutorial de bucles: https://docs.python.org/3/tutorial/controlflow.html

---

**¡Domina las estructuras de datos y el control de flujo para análisis deportivos más sofisticados!** ⚽🔄
