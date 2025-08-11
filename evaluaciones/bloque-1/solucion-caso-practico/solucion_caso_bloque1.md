---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.17.2
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

# Caso Práctico Bloque 1 - SOLUCIÓN

## Análisis Básico de un Equipo de Fútbol

**Equipo:** Analistas Junior  
**Integrantes:** [Nombres del equipo]  
**Fecha:** [Fecha de entrega]

---

## Lo que vamos a hacer

- Usar Python básico para analizar un equipo de fútbol
- Crear funciones simples para cálculos
- Trabajar con listas y diccionarios
- Encontrar patrones en los datos

---

# PARTE 1: PYTHON BÁSICO (50 puntos)

## 1.1 Definir los Datos

```python
# DATOS DE PARTIDOS (listas simples)
resultados_partidos = ["Victoria", "Derrota", "Victoria", "Empate", "Victoria", 
                      "Derrota", "Victoria", "Empate", "Victoria", "Victoria"]

goles_favor = [2, 0, 3, 1, 2, 0, 1, 2, 3, 2]
goles_contra = [1, 3, 1, 1, 0, 2, 0, 2, 1, 1]

# DATOS DE JUGADORES (diccionario simple)
jugadores = {
    "Carlos": {"posicion": "Delantero", "goles": 8, "edad": 23},
    "María": {"posicion": "Mediocampo", "goles": 3, "edad": 21}, 
    "Luis": {"posicion": "Defensa", "goles": 1, "edad": 25},
    "Ana": {"posicion": "Delantero", "goles": 6, "edad": 22},
    "Pedro": {"posicion": "Mediocampo", "goles": 2, "edad": 24},
    "Sofia": {"posicion": "Portero", "goles": 0, "edad": 20},
    "Diego": {"posicion": "Defensa", "goles": 0, "edad": 26},
    "Carmen": {"posicion": "Delantero", "goles": 5, "edad": 19}
}

print("¡Datos cargados correctamente!")
print(f"Tenemos {len(resultados_partidos)} partidos y {len(jugadores)} jugadores")
```

## 1.2 Contar Resultados con Bucles (15 puntos)

```python
# Contar victorias, empates y derrotas usando bucle for
victorias = 0
empates = 0  
derrotas = 0

# Usar bucle for e if para contar cada tipo de resultado
for resultado in resultados_partidos:
    if resultado == "Victoria":
        victorias += 1
    elif resultado == "Empate":
        empates += 1
    else:
        derrotas += 1

print("=== RESULTADOS DE LA TEMPORADA ===")
print(f"Victorias: {victorias}")
print(f"Empates: {empates}")
print(f"Derrotas: {derrotas}")
print(f"Total de partidos: {len(resultados_partidos)}")
```

## 1.3 Crear Funciones Simples (20 puntos)

```python
# Función para calcular puntos
def calcular_puntos(victorias, empates):
    """Calcula puntos: Victoria=3, Empate=1"""
    total_puntos = victorias * 3 + empates * 1
    return total_puntos

# Probar la función
puntos_totales = calcular_puntos(victorias, empates)
print(f"Puntos totales obtenidos: {puntos_totales}")
print(f"Puntos máximos posibles: {len(resultados_partidos) * 3}")
```

```python
# Función para encontrar mejor goleador
def mejor_goleador(jugadores):
    """Encuentra quién marcó más goles"""
    nombre_mejor = ""
    goles_mejor = 0
    
    # Buscar en todos los jugadores
    for nombre, datos in jugadores.items():
        if datos["goles"] > goles_mejor:
            goles_mejor = datos["goles"]
            nombre_mejor = nombre
    
    return nombre_mejor, goles_mejor

# Probar la función
mejor_nombre, mejor_goles = mejor_goleador(jugadores)
print(f"Mejor goleador: {mejor_nombre} con {mejor_goles} goles")
```

## 1.4 Trabajar con Listas y Diccionarios (15 puntos)

```python
# Calcular total de goles a favor usando la lista
total_goles_favor = 0
for goles in goles_favor:
    total_goles_favor += goles

print(f"Total de goles marcados: {total_goles_favor}")

# También podemos usar la función sum() para hacer lo mismo
total_con_sum = sum(goles_favor)
print(f"Verificación con sum(): {total_con_sum}")
```

```python
# Encontrar el partido con más goles
goles_por_partido = []
for i in range(len(goles_favor)):
    total_partido = goles_favor[i] + goles_contra[i]
    goles_por_partido.append(total_partido)

partido_mas_goles = max(goles_por_partido)
print(f"Partido con más goles: {partido_mas_goles} goles")

# Encontrar en qué partido fue
for i in range(len(goles_por_partido)):
    if goles_por_partido[i] == partido_mas_goles:
        print(f"Fue el partido #{i+1}: {goles_favor[i]}-{goles_contra[i]} ({resultados_partidos[i]})")
        break
```

```python
# Usar el diccionario de jugadores para encontrar información básica
total_goles_jugadores = 0
jugador_mas_joven = None
edad_menor = 100  # Empezamos con un número muy alto

for nombre, datos in jugadores.items():
    # Sumar goles de todos los jugadores
    total_goles_jugadores += datos["goles"]
    
    # Encontrar el jugador más joven
    if datos["edad"] < edad_menor:
        edad_menor = datos["edad"]
        jugador_mas_joven = nombre

print(f"Total de goles marcados por todos los jugadores: {total_goles_jugadores}")
print(f"Jugador más joven: {jugador_mas_joven} ({edad_menor} años)")
```

---

# PARTE 2: ANÁLISIS SIMPLE (30 puntos)

## 2.1 Estadísticas Básicas del Equipo (15 puntos)

```python
# Usar nuestras funciones para calcular puntos totales
puntos = calcular_puntos(victorias, empates)
print(f"=== ESTADÍSTICAS DEL EQUIPO ===")
print(f"Puntos obtenidos: {puntos}")

# Calcular el promedio de goles por partido
total_partidos = len(resultados_partidos)
promedio_goles = total_goles_favor / total_partidos
print(f"Promedio de goles por partido: {promedio_goles:.1f}")

# Determinar si marcamos más goles de los que recibimos
total_goles_contra = sum(goles_contra)
diferencia = total_goles_favor - total_goles_contra

if diferencia > 0:
    print(f"¡Bien! Marcamos {diferencia} goles más de los que recibimos")
elif diferencia < 0:
    print(f"Recibimos {abs(diferencia)} goles más de los que marcamos")
else:
    print("Marcamos la misma cantidad de goles que recibimos")
```

## 2.2 Análisis de Jugadores (15 puntos)

```python
# Usar nuestra función para encontrar el mejor goleador
goleador, goles = mejor_goleador(jugadores)
print(f"=== ANÁLISIS DE JUGADORES ===")
print(f"Mejor goleador: {goleador} con {goles} goles")
print(f"Posición: {jugadores[goleador]['posicion']}")
print(f"Edad: {jugadores[goleador]['edad']} años")
```

```python
# Contar cuántos delanteros hay en el equipo
delanteros = 0
mediocampos = 0
defensas = 0
porteros = 0

for nombre, datos in jugadores.items():
    if datos["posicion"] == "Delantero":
        delanteros += 1
    elif datos["posicion"] == "Mediocampo":
        mediocampos += 1
    elif datos["posicion"] == "Defensa":
        defensas += 1
    elif datos["posicion"] == "Portero":
        porteros += 1

print(f"\nJugadores por posición:")
print(f"Delanteros: {delanteros}")
print(f"Mediocampos: {mediocampos}")
print(f"Defensas: {defensas}")
print(f"Porteros: {porteros}")
```

```python
# Calcular el total de goles marcados por todos los jugadores
total_goles_equipo = 0
goles_por_delanteros = 0

print(f"\nGoles por jugador:")
for nombre, datos in jugadores.items():
    goles_jugador = datos["goles"]
    total_goles_equipo += goles_jugador
    print(f"{nombre} ({datos['posicion']}): {goles_jugador} goles")
    
    # Contar goles de delanteros
    if datos["posicion"] == "Delantero":
        goles_por_delanteros += goles_jugador

print(f"\nTotal de goles del equipo: {total_goles_equipo}")
print(f"Goles marcados por delanteros: {goles_por_delanteros}")
print(f"Porcentaje de goles por delanteros: {(goles_por_delanteros/total_goles_equipo*100):.1f}%")
```

---

# PARTE 3: RESULTADOS Y CONCLUSIONES

## Resumen de Nuestros Hallazgos

```python
print("=== RESUMEN FINAL ===")
print(f"📊 Récord del equipo: {victorias} victorias, {empates} empates, {derrotas} derrotas")
print(f"⚽ Goles: {total_goles_favor} a favor, {total_goles_contra} en contra")
print(f"🏆 Puntos obtenidos: {puntos} de {len(resultados_partidos) * 3} posibles")
print(f"🥇 Mejor goleador: {goleador} ({goles} goles)")
print(f"👥 Jugadores por posición: {delanteros} delanteros, {mediocampos} mediocampos, {defensas} defensas, {porteros} porteros")

# Evaluación final
porcentaje_efectividad = (puntos / (len(resultados_partidos) * 3)) * 100
print(f"\n📈 Efectividad del equipo: {porcentaje_efectividad:.1f}%")

if porcentaje_efectividad >= 70:
    evaluacion = "¡Excelente temporada!"
elif porcentaje_efectividad >= 50:
    evaluacion = "Buena temporada con cosas por mejorar"
else:
    evaluacion = "Temporada difícil, necesitamos mejorar"

print(f"✨ Evaluación: {evaluacion}")
```

## Lo que Aprendimos Hoy

¡Felicitaciones! En este caso práctico aplicamos exitosamente:

### ✅ **Python Básico:**

- Variables para almacenar datos
- Bucles `for` para procesar listas
- Condicionales `if/elif/else` para tomar decisiones
- Operaciones matemáticas básicas

### ✅ **Funciones:**

- `calcular_puntos()`: Automatizó el cálculo de puntos
- `mejor_goleador()`: Encontró al mejor jugador

### ✅ **Estructuras de Datos:**

- Listas para almacenar resultados y goles
- Diccionarios para organizar información de jugadores
- Acceso a datos usando llaves y índices

### ✅ **Análisis de Datos:**

- Calculamos estadísticas importantes del equipo
- Comparamos jugadores y posiciones
- Sacamos conclusiones basadas en los datos

### 🚀 **Próximos Pasos:**

En el Bloque 2 aprenderemos a usar pandas para manejar datos más grandes y crear gráficos con seaborn.

¡Excelente trabajo aplicando Python básico al análisis deportivo!
