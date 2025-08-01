# Ejercicio Semana 4: Introducción a Pandas y NumPy para Análisis Deportivo

## Información del Ejercicio

**Bloque:** 1 - Prerrequisitos de Programación  
**Peso:** 12% de la calificación del bloque (60% ÷ 5 ejercicios)  
**Tiempo estimado:** 2-2.5 horas  
**Entrega:** Final de Semana 4

## Objetivos

Al completar este ejercicio, serás capaz de:

- Crear y manipular arrays de NumPy con datos deportivos
- Implementar operaciones vectorizadas para análisis eficiente
- Crear y manipular DataFrames de pandas
- Realizar operaciones básicas de filtrado y agrupación

## Ejercicio 1: Operaciones con Arrays de NumPy (20 puntos)

### Parte A: Creación y Manipulación Básica

```python
import numpy as np

# Crear arrays con estadísticas de jugadores
goles_temporada = np.array([15, 8, 23, 12, 6, 18, 10, 14, 9, 21])
asistencias = np.array([5, 12, 8, 15, 18, 6, 11, 9, 13, 7])
partidos_jugados = np.array([20, 25, 22, 24, 26, 21, 23, 20, 25, 19])

# Tu código aquí:
# 1. Calcular promedio de goles por partido para cada jugador
# 2. Encontrar al jugador más goleador (índice y valor)
# 3. Calcular la suma total de goles y asistencias
# 4. Crear array con jugadores que han marcado más de 10 goles
# 5. Calcular estadísticas básicas: media, mediana, desviación estándar
```

### Parte B: Operaciones Matriciales

```python
# Matriz de rendimiento: [goles, asistencias, partidos] por jugador
rendimiento = np.array([
    [15, 5, 20],   # Jugador 1
    [8, 12, 25],   # Jugador 2
    [23, 8, 22],   # Jugador 3
    [12, 15, 24],  # Jugador 4
    [6, 18, 26]    # Jugador 5
])

# Tu código aquí:
# 1. Calcular promedio de goles por partido por jugador
# 2. Sumar todas las estadísticas por categoría
# 3. Encontrar al jugador más completo (mayor suma de goles + asistencias)
# 4. Crear matriz normalizada (dividir cada valor por el máximo de su columna)
# 5. Transponer la matriz y explicar qué representa
```

### Tu Respuesta - Parte A

*Completa las operaciones básicas con arrays de NumPy.*

### Tu Respuesta - Parte B

*Completa las operaciones matriciales avanzadas.*

## Ejercicio 2: Introducción a DataFrames de Pandas (20 puntos)

### Parte A: Creación y Exploración

```python
import pandas as pd

# Crear DataFrame de jugadores
datos_jugadores = {
    'Nombre': ['Messi', 'Ronaldo', 'Mbappé', 'Haaland', 'Neymar', 'Salah', 'Benzema', 'Lewandowski'],
    'Equipo': ['Inter Miami', 'Al-Nassr', 'PSG', 'Manchester City', 'Al-Hilal', 'Liverpool', 'Real Madrid', 'Barcelona'],
    'Liga': ['MLS', 'Saudi Pro', 'Ligue 1', 'Premier League', 'Saudi Pro', 'Premier League', 'La Liga', 'La Liga'],
    'Edad': [36, 39, 25, 23, 32, 31, 36, 35],
    'Goles': [12, 15, 18, 22, 8, 16, 12, 19],
    'Asistencias': [8, 3, 6, 5, 11, 7, 4, 8],
    'Partidos': [25, 28, 24, 26, 22, 29, 27, 25],
    'Valor_Mercado': [35.0, 15.0, 180.0, 170.0, 60.0, 70.0, 25.0, 45.0]  # En millones
}

df_jugadores = pd.DataFrame(datos_jugadores)

# Tu código aquí:
# 1. Mostrar información básica del DataFrame (shape, info, describe)
# 2. Mostrar los primeros 3 y últimos 3 jugadores
# 3. Calcular promedio de goles por partido
# 4. Agregar columna 'Contribucion_Gol' (goles + asistencias)
# 5. Ordenar por contribución de gol de mayor a menor
```

### Parte B: Filtrado y Selección

```python
# Continuando con el DataFrame anterior

# Tu código aquí:
# 1. Filtrar jugadores mayores de 30 años
# 2. Seleccionar solo jugadores de La Liga y Premier League
# 3. Encontrar jugadores con más de 15 goles Y más de 5 asistencias
# 4. Crear DataFrame solo con Nombre, Goles y Asistencias
# 5. Filtrar jugadores con valor de mercado superior a 50 millones
# 6. Mostrar estadísticas por liga (usar groupby)
```

### Tu Respuesta - Parte A

*Completa la creación y exploración del DataFrame.*

### Tu Respuesta - Parte B

*Completa las operaciones de filtrado y selección.*

## Ejercicio 3: Análisis de Equipos con Pandas (20 puntos)

### Instrucciones

```python
# Crear DataFrame de equipos
datos_equipos = {
    'Equipo': ['Barcelona', 'Real Madrid', 'Manchester City', 'Bayern Munich', 'PSG', 'Liverpool'],
    'Liga': ['La Liga', 'La Liga', 'Premier League', 'Bundesliga', 'Ligue 1', 'Premier League'],
    'Partidos_Jugados': [30, 30, 32, 28, 32, 31],
    'Victorias': [20, 18, 25, 21, 24, 19],
    'Empates': [6, 8, 4, 5, 6, 8],
    'Derrotas': [4, 4, 3, 2, 2, 4],
    'Goles_Favor': [68, 65, 89, 92, 75, 78],
    'Goles_Contra': [35, 32, 31, 38, 28, 42],
    'Presupuesto': [800, 750, 900, 650, 950, 550]  # En millones de euros
}

df_equipos = pd.DataFrame(datos_equipos)

# Tu código aquí:
# 1. Calcular puntos para cada equipo (3 por victoria, 1 por empate)
# 2. Calcular diferencia de goles
# 3. Calcular promedio de goles por partido (favor y contra)
# 4. Crear columna 'Eficiencia_Presupuesto' (puntos / presupuesto * 100)
# 5. Determinar el equipo más eficiente económicamente
# 6. Crear ranking de equipos por puntos
# 7. Analizar correlación entre presupuesto y rendimiento
```

### Tu Respuesta

*Completa el análisis completo de equipos.*

## Ejercicio 4: Operaciones Grupales y Agregaciones (20 puntos)

### Instrucciones

```python
# Crear DataFrame más complejo con datos de múltiples temporadas
datos_historicos = {
    'Jugador': ['Messi', 'Messi', 'Messi', 'Ronaldo', 'Ronaldo', 'Ronaldo', 
                'Mbappé', 'Mbappé', 'Haaland', 'Haaland', 'Neymar', 'Neymar'],
    'Temporada': ['2021-22', '2022-23', '2023-24', '2021-22', '2022-23', '2023-24',
                  '2022-23', '2023-24', '2022-23', '2023-24', '2021-22', '2022-23'],
    'Equipo': ['PSG', 'PSG', 'Inter Miami', 'Manchester United', 'Al-Nassr', 'Al-Nassr',
               'PSG', 'PSG', 'Borussia Dortmund', 'Manchester City', 'PSG', 'PSG'],
    'Liga': ['Ligue 1', 'Ligue 1', 'MLS', 'Premier League', 'Saudi Pro', 'Saudi Pro',
             'Ligue 1', 'Ligue 1', 'Bundesliga', 'Premier League', 'Ligue 1', 'Ligue 1'],
    'Goles': [11, 16, 12, 18, 14, 15, 28, 18, 15, 22, 13, 11],
    'Asistencias': [14, 16, 8, 3, 2, 3, 8, 6, 7, 5, 8, 9],
    'Partidos': [26, 32, 25, 30, 31, 28, 34, 24, 28, 26, 28, 29]
}

df_historico = pd.DataFrame(datos_historicos)

# Tu código aquí:
# 1. Agrupar por jugador y calcular totales de goles y asistencias
# 2. Calcular promedio de goles por partido por jugador
# 3. Agrupar por liga y mostrar estadísticas promedio
# 4. Encontrar la mejor temporada de cada jugador (más goles)
# 5. Crear tabla pivot: jugadores vs temporadas con goles
# 6. Analizar evolución de rendimiento de Messi y Ronaldo
# 7. Determinar qué liga es más competitiva (mayor promedio de goles)
```

### Tu Respuesta

*Completa todas las operaciones de agrupación y análisis temporal.*

## Ejercicio 5: Integración NumPy-Pandas (20 puntos)

### Instrucciones

```python
# Combinar NumPy y Pandas para análisis avanzado

# Datos de rendimiento semanal de un equipo (4 semanas)
rendimiento_semanal = np.array([
    [3, 1, 2, 4],  # Goles por semana
    [1, 2, 0, 1],  # Goles contra por semana
    [2, 1, 3, 2],  # Tarjetas amarillas por semana
    [0, 0, 1, 0]   # Tarjetas rojas por semana
])

# Tu código aquí:
# 1. Crear DataFrame a partir del array NumPy
# 2. Agregar nombres apropiados a filas y columnas
# 3. Calcular estadísticas semanales usando NumPy
# 4. Usar pandas para crear análisis descriptivo
# 5. Combinar ambas librerías para encontrar patrones

# Análisis de correlación entre variables
jugadores_stats = pd.DataFrame({
    'Velocidad': np.random.normal(75, 10, 20),
    'Fuerza': np.random.normal(70, 15, 20),
    'Técnica': np.random.normal(80, 12, 20),
    'Goles_Temporada': np.random.poisson(15, 20)
})

# Tu código aquí:
# 6. Calcular matriz de correlación
# 7. Identificar qué habilidad se correlaciona más con los goles
# 8. Crear categorías de jugadores basadas en sus habilidades
# 9. Usar NumPy para operaciones matemáticas y pandas para presentación
# 10. Generar reporte final integrando ambas librerías
```

### Tu Respuesta

*Completa la integración avanzada de NumPy y Pandas.*

## Ejercicio Bonus: Análisis de Rendimiento en Casa vs Visitante (10 puntos extra)

### Instrucciones

**Ejercicio opcional para puntos adicionales:**

```python
# Datos de partidos en casa y como visitante
partidos_detalle = {
    'Equipo': ['Barcelona'] * 10 + ['Real Madrid'] * 10,
    'Local_Visitante': ['Local'] * 5 + ['Visitante'] * 5 + ['Local'] * 5 + ['Visitante'] * 5,
    'Goles_Favor': [3, 2, 1, 4, 2, 1, 0, 2, 1, 3, 2, 1, 3, 2, 4, 1, 2, 0, 1, 3],
    'Goles_Contra': [1, 0, 1, 2, 1, 2, 1, 1, 2, 0, 1, 2, 1, 1, 1, 2, 1, 1, 2, 1],
    'Asistencia': [85000, 82000, 88000, 90000, 87000, 45000, 38000, 42000, 40000, 35000,
                   78000, 80000, 85000, 83000, 79000, 55000, 52000, 48000, 50000, 46000]
}

df_partidos = pd.DataFrame(partidos_detalle)

# Análisis completo casa vs visitante:
# 1. Comparar rendimiento goleador local vs visitante
# 2. Analizar impacto de la asistencia en el rendimiento
# 3. Crear métricas avanzadas usando NumPy
# 4. Generar visualización de datos con pandas
# 5. Conclusiones sobre ventaja de jugar en casa
```

### Tu Respuesta

*Ejercicio opcional: Análisis completo casa vs visitante.*

## Criterios de Evaluación

### Dominio Técnico (50%)

- [ ] Operaciones NumPy correctas y eficientes (15%)
- [ ] Manipulación de DataFrames apropiada (15%)
- [ ] Operaciones de agrupación y filtrado (10%)
- [ ] Integración NumPy-Pandas efectiva (10%)

### Análisis Deportivo (30%)

- [ ] Interpretación correcta de resultados (15%)
- [ ] Aplicación práctica relevante (15%)

### Presentación y Documentación (20%)

- [ ] Código bien comentado y explicado (10%)
- [ ] Resultados claramente presentados (10%)

## Instrucciones de Entrega

1. **Completa todos los ejercicios** en este notebook
2. **Ejecuta todas las celdas** y verifica que funcionan
3. **Incluye interpretaciones** de tus análisis
4. **Guarda como:** `ejercicio-semana-4-[tu-apellido].ipynb`
5. **Entrega antes del final de Semana 4**

## Recursos de Apoyo

- Notebook de la Semana 4: `pandas-numpy-introduccion.ipynb`
- Documentación NumPy: <https://numpy.org/doc/>
- Documentación Pandas: <https://pandas.pydata.org/docs/>
- Cheat sheets de NumPy y Pandas

---

**¡Domina las herramientas fundamentales para el análisis de datos deportivos!** ⚽📊
