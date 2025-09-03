---
marp: true
theme: default
paginate: true
class: lead
---

# Semana 4: ¿Cómo procesan miles de datos los analistas profesionales?

**Programación Básica 1 – Prepa Tec**

---

# SESIÓN 1: ¿Por qué necesitas herramientas más potentes que listas simples? (50 min)

---

## Pregunta guía

¿Cómo calcularías estadísticas de 1000 jugadores en segundos?

---

### Teoría: El límite de las listas normales

¿Recuerdas cómo calculabas el promedio de goles con listas?

```python
goles = [2, 1, 3, 0, 2]
promedio = sum(goles) / len(goles)
```

---

### Reflexión inicial

¿Qué pasaría si tuvieras que calcular promedios de 10,000 jugadores con este método?

---

### Analogía deportiva

¿Cuál es la diferencia entre cronometrar manualmente a cada corredor en una maratón y usar un chip electrónico que registra automáticamente todos los tiempos?

**NumPy** es como el chip electrónico para cálculos matemáticos.

---

## Descubriendo NumPy: Tu calculadora profesional

- Procesa miles de números simultáneamente
- Realiza operaciones matemáticas en milisegundos
- Es la base de todas las herramientas de ciencia de datos

---

### Práctica: Tu primer contacto con la velocidad profesional

```python
import numpy as np
print("NumPy importado exitosamente")
print(f"Versión: {np.__version__}")

goles_lista = [15, 8, 22, 12, 18, 7, 25, 14]
print("Con lista normal:", goles_lista)
print("Tipo:", type(goles_lista))

goles_array = np.array([15, 8, 22, 12, 18, 7, 25, 14])
print("Con array NumPy:", goles_array)
print("Tipo:", type(goles_array))

promedio_lista = sum(goles_lista) / len(goles_lista)
print(f"Promedio con listas: {promedio_lista}")

promedio_array = np.mean(goles_array)
print(f"Promedio con NumPy: {promedio_array}")
```

---

### Reflexión

¿Notas alguna diferencia visual o de velocidad? ¿Qué ventajas ves?

---

### Práctica: Operaciones simultáneas

```python
# Datos de rendimiento de 10 jugadores de La Liga
goles_jornada = np.array([2, 0, 1, 3, 1, 0, 2, 1, 0, 4])
partidos_jugados = np.array([25, 28, 22, 30, 26, 24, 27, 29, 21, 26])

promedio_goles = goles_jornada / partidos_jugados
print("Promedio goles/partido:", np.round(promedio_goles, 3))
print(f"Mejor goleador de la jornada: {np.max(goles_jornada)} goles")
print(f"Promedio general de goles: {np.mean(goles_jornada):.2f}")
print(f"¿Qué tan dispersos están los datos?: {np.std(goles_jornada):.2f}")
print(f"Total de goles de todos: {np.sum(goles_jornada)}")
```

---

### Reflexión

¿Notas que no escribimos ni un solo bucle? ¿Qué más podrías calcular instantáneamente?

---

### Práctica: Arrays 2D (tablas de datos)

```python
goles_temporada = np.array([
    [2, 1, 0, 3],
    [0, 2, 1, 1],
    [1, 1, 2, 0],
    [3, 0, 1, 2],
    [1, 3, 0, 1]
])
print("Matriz completa de goles:")
print(goles_temporada)
print(f"Forma de la matriz: {goles_temporada.shape}")

goles_por_jugador = np.sum(goles_temporada, axis=1)
print("Total goles por jugador:", goles_por_jugador)

goles_por_jornada = np.sum(goles_temporada, axis=0)
print("Total goles por jornada:", goles_por_jornada)
```

---

### Reflexión

¿Para qué situaciones deportivas sería útil organizar datos en forma de tabla?

---

### Actividad práctica

Crea un análisis NumPy de las asistencias de 4 jugadores durante 3 jornadas. Calcula total, promedio y mejor asistente.

---

## Síntesis de la sesión 1

- Arrays: Listas súper eficientes para cálculos masivos
- Operaciones vectorizadas: Cálculos simultáneos
- Arrays 2D: Matrices para datos multidimensionales
- Funciones estadísticas: mean, sum, max, min, std
- Ventajas: velocidad, simplicidad, profesionalidad

---

# SESIÓN 2: ¿Cómo organizas datos complejos como nombres, fechas y estadísticas? (50 min)

---

## Pregunta guía

¿Qué herramienta usarían los clubes para gestionar información completa de plantillas?

---

### Teoría: El límite de NumPy

NumPy es perfecto para números, pero ¿qué pasa cuando necesitas manejar nombres, fechas, posiciones y equipos?

---

### Analogía deportiva

¿Cuál es la diferencia entre una calculadora (solo números) y una hoja de cálculo (texto, fechas, números, fórmulas)?

**Pandas** es como Excel, pero programable y mil veces más potente.

---

## Descubriendo Pandas: Tu organizador inteligente

- Maneja cualquier tipo de dato: números, texto, fechas
- Organiza información en tablas inteligentes
- Permite filtros y búsquedas complejas
- Es la herramienta estándar para análisis de datos

---

### Práctica: Tu primera base de datos deportiva

```python
import pandas as pd
import numpy as np
print("Pandas importado exitosamente")
print(f"Versión: {pd.__version__}")

datos_jugadores = {
    'nombre': ['Vinícius Jr', 'Benzema', 'Modrić', 'Courtois', 'Militão'],
    'posicion': ['Extremo', 'Delantero', 'Mediocampista', 'Portero', 'Defensa'],
    'edad': [23, 35, 37, 30, 25],
    'goles': [15, 18, 3, 0, 2],
    'asistencias': [8, 6, 12, 0, 1],
    'partidos': [28, 25, 30, 32, 26],
    'nacionalidad': ['Brasil', 'Francia', 'Croacia', 'Bélgica', 'Brasil']
}

plantilla = pd.DataFrame(datos_jugadores)
print(plantilla)
```

---

### Reflexión

¿En qué se parece esta tabla a una hoja de cálculo de Excel? ¿Qué ventajas tiene sobre las listas o arrays?

---

### Práctica: Filtrar y analizar datos

```python
# ¿Cuántos jugadores tienen más de 10 goles?
jugadores_goleadores = plantilla[plantilla['goles'] > 10]
print(jugadores_goleadores)

# ¿Quién es el jugador más joven?
joven = plantilla.loc[plantilla['edad'].idxmin()]
print("Jugador más joven:", joven['nombre'])
```

---

### Práctica: Estadísticas rápidas

```python
print("Promedio de goles:", plantilla['goles'].mean())
print("Máximo de asistencias:", plantilla['asistencias'].max())
print("Total de partidos:", plantilla['partidos'].sum())
```

---

### Actividad práctica

Crea un DataFrame con datos de tu equipo favorito. Calcula el promedio de edad, el máximo de goles y filtra los jugadores con más de 5 asistencias.

---

## Síntesis de la sesión 2

- DataFrames: Tablas inteligentes para datos mixtos
- Filtros y búsquedas: Selección rápida de información
- Estadísticas automáticas: mean, max, sum
- Ventajas: flexibilidad, claridad, análisis profesional

---

# SESIÓN 3: ¿Cómo integras todo en un sistema de análisis profesional? (50 min)

---

## Pregunta guía

¿Cómo crearías un sistema que analice temporadas completas automáticamente?

---

### Teoría: Integración de NumPy y Pandas

¿Cómo combinarías cálculos masivos y organización de datos complejos?

---

### Práctica: Análisis profesional de una temporada

```python
# Supón que tienes datos de goles por jornada para varios equipos
goles_temporada = {
    'Barcelona': [2, 3, 1, 4, 2],
    'Real Madrid': [1, 2, 2, 3, 1],
    'Atletico': [0, 1, 2, 1, 2]
}

df_goles = pd.DataFrame(goles_temporada)
print(df_goles)

# Calcular totales y promedios por equipo
totales = df_goles.sum()
promedios = df_goles.mean()
print("Totales por equipo:", totales)
print("Promedios por equipo:", promedios)
```

---

### Práctica: Visualización básica (opcional)

```python
import matplotlib.pyplot as plt
df_goles.plot(kind='bar')
plt.title('Goles por equipo en la temporada')
plt.xlabel('Jornada')
plt.ylabel('Goles')
plt.show()
```

---

### Reflexión

¿Qué ventajas tiene automatizar el análisis de temporadas completas? ¿Cómo podrías aplicar esto a otros deportes o áreas?

---

## Síntesis de la sesión 3

- Integración de NumPy y Pandas para análisis profesional
- Automatización de cálculos y organización de datos
- Visualización básica para comunicar resultados

---

# Preguntas para tu autoevaluación

- ¿Qué fue lo más claro y lo más desafiante?
- ¿Cómo aplicarías estos patrones fuera del fútbol?
- ¿Qué te gustaría automatizar en tu vida diaria usando lógica similar?

---

# Próxima semana

- Visualización avanzada de datos
- Análisis estadístico más profundo
- Reportes profesionales

**¿Listo para el siguiente nivel?**
