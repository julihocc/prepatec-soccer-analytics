# Banco de Preguntas Canvas - Bloque 1
## Python Fundamentals y Análisis de Datos Básico

**Instrucciones para Canvas:**
- Preguntas de opción múltiple: 4 opciones (A, B, C, D)
- Preguntas numéricas: respuesta exacta con tolerancia del 5%
- Selección aleatoria de 20-25 preguntas por examen
- Tiempo sugerido: 45-60 minutos

---

## SEMANA 1: FUNDAMENTOS DE PYTHON

### 1. Variables y Tipos de Datos

**1.** ¿Cuál es el resultado de ejecutar `type(42)` en Python?
A) `<class 'float'>`
B) `<class 'int'>`
C) `<class 'str'>`
D) `<class 'number'>`
**Respuesta: B**

**2.** Si ejecuto `nombre = "Barcelona"` y luego `print(len(nombre))`, ¿qué se imprime?
A) 8
B) 9
C) 10
D) Error
**Respuesta: B**

**3.** ¿Cuál de estos es un nombre de variable válido en Python?
A) `2equipo`
B) `equipo-favorito`
C) `equipo_favorito`
D) `equipo.favorito`
**Respuesta: C**

**4.** (Numérica) Si `goles = 25` y `partidos = 10`, ¿cuál es el resultado de `goles/partidos`?
**Respuesta: 2.5**

**5.** ¿Qué tipo de dato es el resultado de `"Messi" + " " + "Barcelona"`?
A) int
B) float
C) str
D) list
**Respuesta: C**

### 2. Estructuras de Control

**6.** En el código `if goles > 20: print("Goleador")`, ¿cuándo se ejecuta el print?
A) Siempre
B) Cuando goles es exactamente 20
C) Cuando goles es mayor que 20
D) Cuando goles es menor que 20
**Respuesta: C**

**7.** ¿Cuál es la salida del siguiente código?
```python
edad = 25
if edad >= 18:
    print("Mayor de edad")
else:
    print("Menor de edad")
```
A) Mayor de edad
B) Menor de edad
C) Error
D) No imprime nada
**Respuesta: A**

**8.** (Numérica) ¿Cuántas veces se ejecuta `print("Gol")` en este código?
```python
for i in range(3):
    print("Gol")
```
**Respuesta: 3**

**9.** En un bucle `for jugador in ['Messi', 'Ronaldo', 'Neymar']:`, ¿cuántas iteraciones habrá?
A) 2
B) 3
C) 4
D) Infinitas
**Respuesta: B**

**10.** ¿Qué imprime este código?
```python
contador = 0
while contador < 2:
    print(contador)
    contador += 1
```
A) 0, 1
B) 1, 2
C) 0, 1, 2
D) Error infinito
**Respuesta: A**

---

## SEMANA 2: FUNCIONES

**11.** ¿Cómo se define una función en Python que calcula el promedio de goles?
A) `function promedio_goles():`
B) `def promedio_goles():`
C) `promedio_goles() def:`
D) `create promedio_goles():`
**Respuesta: B**

**12.** En la función `def calcular_puntos(victorias, empates):`, ¿cuántos parámetros recibe?
A) 1
B) 2
C) 3
D) 0
**Respuesta: B**

**13.** ¿Qué hace la palabra clave `return` en una función?
A) Imprime un valor
B) Devuelve un valor al código que llamó la función
C) Termina el programa
D) Define una variable
**Respuesta: B**

**14.** (Numérica) Si tengo `def goles_promedio(total, partidos): return total/partidos`, ¿cuál es el resultado de `goles_promedio(30, 10)`?
**Respuesta: 3**

**15.** ¿Cuál es la diferencia entre parámetros y argumentos en funciones?
A) Son lo mismo
B) Parámetros son en la definición, argumentos al llamar la función
C) Argumentos son en la definición, parámetros al llamar la función
D) Los parámetros son opcionales
**Respuesta: B**

---

## SEMANA 3: LISTAS Y DICCIONARIOS

### Listas

**16.** ¿Cómo accedo al primer elemento de la lista `jugadores = ['Messi', 'Ronaldo', 'Neymar']`?
A) `jugadores[1]`
B) `jugadores[0]`
C) `jugadores.first()`
D) `jugadores(0)`
**Respuesta: B**

**17.** (Numérica) ¿Cuál es el resultado de `len(['Barcelona', 'Real Madrid', 'Atletico'])`?
**Respuesta: 3**

**18.** ¿Qué hace el método `.append()` en una lista?
A) Elimina el último elemento
B) Ordena la lista
C) Agrega un elemento al final
D) Cuenta los elementos
**Respuesta: C**

**19.** Si `goles = [1, 0, 2, 3]`, ¿qué devuelve `max(goles)`?
A) 1
B) 2
C) 3
D) 6
**Respuesta: C**

**20.** ¿Cómo obtengo los primeros 2 elementos de `equipos = ['Barça', 'Madrid', 'City']`?
A) `equipos[0:2]`
B) `equipos[1:2]`
C) `equipos[0:1]`
D) `equipos[2]`
**Respuesta: A**

### Diccionarios

**21.** En el diccionario `jugador = {'nombre': 'Messi', 'edad': 36}`, ¿cómo accedo a la edad?
A) `jugador['edad']`
B) `jugador.edad`
C) `jugador[1]`
D) `jugador(edad)`
**Respuesta: A**

**22.** ¿Qué método uso para obtener todas las llaves de un diccionario?
A) `.values()`
B) `.keys()`
C) `.items()`
D) `.get()`
**Respuesta: B**

**23.** (Numérica) Si `estadisticas = {'goles': 25, 'asistencias': 10}`, ¿cuál es `estadisticas['goles'] + estadisticas['asistencias']`?
**Respuesta: 35**

---

## SEMANA 4: INTRODUCCIÓN A PANDAS

### Conceptos Básicos

**24.** ¿Cuál es el comando correcto para importar pandas?
A) `import pandas`
B) `import pandas as pd`
C) `from pandas import pd`
D) `import pd`
**Respuesta: B**

**25.** ¿Cómo se llama la estructura principal de datos en pandas?
A) Array
B) List
C) DataFrame
D) Dict
**Respuesta: C**

**26.** ¿Qué función uso para leer un archivo CSV en pandas?
A) `pd.open_csv()`
B) `pd.load_csv()`
C) `pd.read_csv()`
D) `pd.import_csv()`
**Respuesta: C**

**27.** Si tengo un DataFrame `df`, ¿cómo veo las primeras 5 filas?
A) `df.first(5)`
B) `df.top(5)`
C) `df.head(5)`
D) `df.show(5)`
**Respuesta: C**

**28.** ¿Qué método me da información sobre los tipos de datos en un DataFrame?
A) `df.info()`
B) `df.types()`
C) `df.describe()`
D) `df.summary()`
**Respuesta: A**

### Operaciones Básicas

**29.** ¿Cómo selecciono la columna 'goles' de un DataFrame `df`?
A) `df.goles`
B) `df['goles']`
C) Ambas A y B son correctas
D) `df.select('goles')`
**Respuesta: C**

**30.** (Numérica) Si un DataFrame tiene 50 filas y 4 columnas, ¿qué devuelve `len(df)`?
**Respuesta: 50**

**31.** ¿Qué hace `df.describe()` en un DataFrame?
A) Muestra los tipos de datos
B) Muestra estadísticas descriptivas
C) Muestra las primeras filas
D) Cuenta valores únicos
**Respuesta: B**

**32.** ¿Cómo filtro un DataFrame para mostrar solo jugadores con más de 10 goles?
A) `df[df['goles'] > 10]`
B) `df.filter(goles > 10)`
C) `df.where(goles > 10)`
D) `df.select(goles > 10)`
**Respuesta: A**

---

## SEMANA 5: INTRODUCCIÓN A NUMPY Y VISUALIZACIÓN

### NumPy

**33.** ¿Cuál es el comando correcto para importar numpy?
A) `import numpy`
B) `import numpy as np`
C) `from numpy import np`
D) `import np`
**Respuesta: B**

**34.** ¿Qué función de numpy uso para crear un array con números del 0 al 9?
A) `np.array(10)`
B) `np.range(10)`
C) `np.arange(10)`
D) `np.create(10)`
**Respuesta: C**

**35.** (Numérica) ¿Cuál es el resultado de `np.mean([2, 4, 6, 8])`?
**Respuesta: 5**

**36.** ¿Qué hace `np.random.seed(42)` en numpy?
A) Genera números aleatorios
B) Fija la semilla para reproducibilidad
C) Cuenta elementos
D) Ordena arrays
**Respuesta: B**

### Matplotlib Básico

**37.** ¿Cuál es la forma común de importar matplotlib para gráficos?
A) `import matplotlib as plt`
B) `import matplotlib.pyplot as plt`
C) `import pyplot as plt`
D) `from matplotlib import plt`
**Respuesta: B**

**38.** ¿Qué función uso para mostrar un gráfico en matplotlib?
A) `plt.display()`
B) `plt.show()`
C) `plt.plot()`
D) `plt.draw()`
**Respuesta: B**

**39.** ¿Cómo agrego un título a un gráfico en matplotlib?
A) `plt.name('título')`
B) `plt.title('título')`
C) `plt.header('título')`
D) `plt.label('título')`
**Respuesta: B**

**40.** ¿Qué tipo de gráfico es mejor para mostrar la evolución de goles por mes?
A) Gráfico de barras
B) Gráfico de líneas
C) Gráfico circular
D) Histograma
**Respuesta: B**

---

## APLICACIONES EN FÚTBOL

### Análisis de Datos Futbolísticos

**41.** En el análisis de datos de fútbol, ¿qué tipo de variable es "posición del jugador"?
A) Numérica continua
B) Numérica discreta
C) Categórica
D) Booleana
**Respuesta: C**

**42.** (Numérica) Si un equipo anotó 45 goles en 30 partidos, ¿cuál es su promedio de goles por partido?
**Respuesta: 1.5**

**43.** ¿Cuál es la mejor manera de almacenar información de múltiples jugadores con sus estadísticas?
A) Variables individuales
B) Una lista simple
C) Un diccionario
D) Un DataFrame de pandas
**Respuesta: D**

**44.** En el contexto del fútbol, ¿qué significa "cleaning data" o limpiar datos?
A) Eliminar todos los datos
B) Corregir errores y valores faltantes
C) Ordenar alfabéticamente
D) Crear gráficos
**Respuesta: B**

### Estadísticas Deportivas

**45.** ¿Qué estadística es más útil para comparar goleadores de diferentes equipos?
A) Total de goles
B) Goles por partido
C) Goles en casa
D) Goles por temporada
**Respuesta: B**

**46.** (Numérica) Si un jugador tiene estas estadísticas por partido: [2, 0, 1, 3, 1], ¿cuál es su promedio de goles?
**Respuesta: 1.4**

**47.** ¿Qué tipo de gráfico es mejor para comparar el número de goles de diferentes equipos?
A) Gráfico de líneas
B) Gráfico de barras
C) Gráfico circular
D) Histograma
**Respuesta: B**

**48.** En análisis deportivo, ¿qué es más importante al presentar datos?
A) Usar muchos colores
B) Mostrar todos los datos posibles
C) Que sean fáciles de entender
D) Usar gráficos en 3D
**Respuesta: C**

---

## RESOLUCIÓN DE PROBLEMAS

### Debugging y Errores Comunes

**49.** ¿Qué error aparece si trato de acceder a `lista[5]` cuando la lista solo tiene 3 elementos?
A) ValueError
B) IndexError
C) KeyError
D) TypeError
**Respuesta: B**

**50.** Si tengo el error "NameError: name 'equipo' is not defined", ¿qué significa?
A) La variable equipo no existe
B) Hay un error de sintaxis
C) El archivo no existe
D) Falta instalar una librería
**Respuesta: A**

**51.** ¿Cuál es la mejor práctica para nombrar variables en Python?
A) usar_guiones_bajos
B) usarCamelCase
C) USAR_MAYUSCULAS
D) Cualquiera está bien
**Respuesta: A**

**52.** (Numérica) Si ejecuto este código, ¿cuántos elementos tendrá la lista final?
```python
goles = []
for i in range(4):
    goles.append(i)
```
**Respuesta: 4**

### Pensamiento Computacional

**53.** ¿Cuál es el primer paso para resolver un problema de programación?
A) Escribir código inmediatamente
B) Entender qué queremos lograr
C) Buscar en Google
D) Usar las librerías más avanzadas
**Respuesta: B**

**54.** ¿Qué significa "iterar" en programación?
A) Repetir un proceso
B) Crear variables
C) Importar librerías
D) Hacer gráficos
**Respuesta: A**

**55.** En el contexto de análisis de datos deportivos, ¿cuál es el orden lógico de trabajo?
A) Visualizar, limpiar, analizar
B) Analizar, limpiar, visualizar
C) Recopilar, limpiar, analizar, visualizar
D) Visualizar, analizar, limpiar
**Respuesta: C**

---

## CONCEPTOS AVANZADOS BÁSICOS

### Manipulación de Datos

**56.** ¿Qué hace el método `.groupby()` en pandas?
A) Ordena los datos
B) Agrupa datos por categorías
C) Elimina duplicados
D) Crea gráficos
**Respuesta: B**

**57.** (Numérica) Si tengo una Serie de pandas con valores [10, 20, 30], ¿cuál es el resultado de `.sum()`?
**Respuesta: 60**

**58.** ¿Qué función uso para unir dos DataFrames en pandas?
A) `pd.join()`
B) `pd.merge()`
C) `pd.combine()`
D) `pd.append()`
**Respuesta: B**

**59.** ¿Cómo manejo valores faltantes (NaN) en pandas?
A) Los ignoro
B) Uso `.dropna()` o `.fillna()`
C) Los convierto a 0
D) No se pueden manejar
**Respuesta: B**

### Visualización Avanzada

**60.** ¿Cuál es la diferencia entre matplotlib y seaborn?
A) Son iguales
B) Seaborn es más fácil para gráficos estadísticos
C) Matplotlib no puede hacer gráficos
D) Seaborn solo hace gráficos de líneas
**Respuesta: B**

**61.** ¿Qué tipo de gráfico uso para mostrar la distribución de edades de jugadores?
A) Gráfico de barras
B) Gráfico de líneas
C) Histograma
D) Gráfico circular
**Respuesta: C**

**62.** (Numérica) Si quiero crear un gráfico con subplots de 2 filas y 3 columnas, ¿cuántos gráficos individuales puedo hacer?
**Respuesta: 6**

---

## INTEGRACIÓN DE CONCEPTOS

### Proyectos Prácticos

**63.** Para analizar el rendimiento de un equipo durante una temporada, ¿qué estructura de datos es más apropiada?
A) Lista de listas
B) Diccionario simple
C) DataFrame con filas por partido
D) Variables individuales
**Respuesta: C**

**64.** ¿Cuál es la secuencia correcta para crear un análisis básico de datos deportivos?
A) Código → Datos → Análisis → Presentación
B) Datos → Limpieza → Análisis → Visualización
C) Visualización → Datos → Código → Resultados
D) Análisis → Datos → Código → Gráficos
**Respuesta: B**

**65.** (Numérica) Si quiero calcular la eficiencia de un delantero (goles/tiros), y anotó 12 goles con 40 tiros, ¿cuál es su eficiencia?
**Respuesta: 0.3**

**66.** Para presentar datos de múltiples equipos en una temporada, ¿cuál es la mejor práctica?
A) Un gráfico por equipo
B) Todos los equipos en un solo gráfico comparativo
C) Solo mostrar números
D) Usar colores aleatorios
**Respuesta: B**

### Casos de Uso Real

**67.** Un entrenador quiere identificar a los jugadores con mejor rendimiento. ¿Qué análisis es más útil?
A) Solo mirar goles totales
B) Combinar múltiples métricas (goles, asistencias, partidos jugados)
C) Solo ver la edad
D) Solo ver el equipo
**Respuesta: B**

**68.** (Numérica) Si un DataFrame de partidos tiene columnas ['equipo_local', 'equipo_visitante', 'goles_local', 'goles_visitante'], ¿cuántas columnas necesito para calcular el total de goles por partido?
**Respuesta: 2**

**69.** Para detectar patrones estacionales en el rendimiento de un equipo, ¿qué necesito incluir en mis datos?
A) Solo goles
B) Solo fechas
C) Fechas y métricas de rendimiento
D) Solo nombres de jugadores
**Respuesta: C**

**70.** ¿Cuál es la mejor práctica al compartir un análisis de datos deportivos?
A) Mostrar solo los códigos
B) Incluir contexto, métodos y conclusiones claras
C) Solo mostrar gráficos sin explicación
D) Usar términos técnicos complejos
**Respuesta: B**

---

## Instrucciones Técnicas para Canvas

### Configuración de Preguntas:
- **Opción múltiple**: Preguntas 1-70 (excepto numéricas)
- **Respuesta numérica**: Preguntas marcadas como (Numérica)
- **Selección aleatoria**: 20-25 preguntas por examen
- **Categorías para balance**:
  - Fundamentos Python (30%): Preguntas 1-15
  - Estructuras de datos (25%): Preguntas 16-32
  - Librerías básicas (25%): Preguntas 33-48
  - Aplicaciones prácticas (20%): Preguntas 49-70

### Ponderación Sugerida:
- Cada pregunta: 4-5 puntos
- Total por examen: 80-100 puntos
- Tiempo: 45-60 minutos
- Intentos permitidos: 1
- Mostrar respuestas correctas: Después del cierre