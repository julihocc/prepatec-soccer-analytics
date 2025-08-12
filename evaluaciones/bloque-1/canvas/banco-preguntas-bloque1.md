# Banco de Preguntas Canvas - Bloque 1

## Python Fundamentals y Análisis de Datos Básico

**Instrucciones para Canvas:**

- Preguntas de opción múltiple: 4 opciones (A, B, C, D)
- Preguntas numéricas: respuesta exacta con tolerancia del 5%
- Selección aleatoria de 20-25 preguntas por examen
- Tiempo sugerido: 45-60 minutos

---

## Selección Núcleo (Core) vs Banco Extendido

Para quizzes introductorios (preparatoria) se recomienda usar SOLO el Núcleo de 75 preguntas. El resto (45) sirve como rotación/repaso adicional.

### Núcleo (75 preguntas)

Cobertura balanceada: fundamentos, estructuras, funciones, pandas básico, NumPy y visualización inicial, aplicación futbolística.
Preguntas núcleo:
1-60, 63, 64, 65, 66, 67, 69, 70, 73, 74, 76, 78, 80, 88, 97, 100

Total: 60 + 15 = 75.

### Banco Extendido (45 preguntas)

Preguntas para ampliar dificultad, variar intentos o tareas de práctica:
61-62, 68, 71-72, 75, 77, 79, 81-87, 89-96, 98-99, 101-120 (excluyendo las ya listadas en Núcleo).

### Uso sugerido en Moodle

- Crear dos categorías: "Bloque1 Núcleo" y "Bloque1 Extendido".
- Cargar primero solo Núcleo para evaluaciones formales iniciales.
- Añadir 5-7 ítems del Extendido de forma aleatoria como preguntas extra (créditos parciales / práctica) si se desea.
- Mantener proporción ~70% opción múltiple y ~30% numéricas dentro del Núcleo (actual: cercano; ajustar si se migra alguna pregunta).

### Próximo ajuste (opcional)

Si se requiere, se pueden mover gradualmente algunas preguntas del Extendido al Núcleo reemplazando duplicadas según desempeño de los estudiantes (análisis de ítems).

---

## SEMANA 1: FUNDAMENTOS DE PYTHON

### 1. Variables y Tipos de Datos

**1. [R]** ¿Cuál es el resultado de ejecutar `type(42)` en Python?
A) `<class 'float'>`
B) `<class 'int'>`
C) `<class 'str'>`
D) `<class 'number'>`
**Respuesta: B**

**2. [R]** Si ejecuto `nombre = "Barcelona"` y luego `print(len(nombre))`, ¿qué se imprime?
A) 8
B) 9
C) 10
D) Error
**Respuesta: B**

**3. [R] *Reescrita*** Necesitas crear una variable para guardar el equipo favorito de un jugador. ¿Cuál de estos nombres cumple las reglas de Python y es legible?
A) `2equipo`
B) `equipo-favorito`
C) `equipo_favorito`
D) `equipo.favorito`
**Respuesta: C**

**4. [A] (Numérica)** Si `goles = 25` y `partidos = 10`, ¿cuál es el resultado de `goles/partidos`?
**Respuesta: 2.5**

**5. [C]** ¿Qué tipo de dato es el resultado de `"Messi" + " " + "Barcelona"`?
A) int
B) float
C) str
D) list
**Respuesta: C**

### 2. Estructuras de Control

**6. [C]** En el código `if goles > 20: print("Goleador")`, ¿cuándo se ejecuta el print?
A) Siempre
B) Cuando goles es exactamente 20
C) Cuando goles es mayor que 20
D) Cuando goles es menor que 20
**Respuesta: C**

**7. [A]** ¿Cuál es la salida del siguiente código?

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

**8. [R] (Numérica)** ¿Cuántas veces se ejecuta `print("Gol")` en este código?

```python
for i in range(3):
    print("Gol")
```

**Respuesta: 3**

**9. [R]** En un bucle `for jugador in ['Messi', 'Ronaldo', 'Neymar']:`, ¿cuántas iteraciones habrá?
A) 2
B) 3
C) 4
D) Infinitas
**Respuesta: B**

**10. [R]** ¿Qué imprime este código?

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

**11. [R]** ¿Cómo se define una función en Python que calcula el promedio de goles?
A) `function promedio_goles():`
B) `def promedio_goles():`
C) `promedio_goles() def:`
D) `create promedio_goles():`
**Respuesta: B**

**12. [R]** En la función `def calcular_puntos(victorias, empates):`, ¿cuántos parámetros recibe?
A) 1
B) 2
C) 3
D) 0
**Respuesta: B**

**13. [C]** ¿Qué hace la palabra clave `return` en una función?
A) Imprime un valor
B) Devuelve un valor al código que llamó la función
C) Termina el programa
D) Define una variable
**Respuesta: B**

**14. [A] *Reescrita (Numérica)*** Un delantero acumuló 30 goles en 10 partidos. Con la función `def goles_promedio(total, partidos): return total/partidos`, ¿qué promedio de goles por partido reportas?
**Respuesta: 3**

**15. [C]** ¿Cuál es la diferencia entre parámetros y argumentos en funciones?
A) Son lo mismo
B) Parámetros son en la definición, argumentos al llamar la función
C) Argumentos son en la definición, parámetros al llamar la función
D) Los parámetros son opcionales
**Respuesta: B**

---

## SEMANA 3: LISTAS Y DICCIONARIOS

### Listas

**16. [R]** ¿Cómo accedo al primer elemento de la lista `jugadores = ['Messi', 'Ronaldo', 'Neymar']`?
A) `jugadores[1]`
B) `jugadores[0]`
C) `jugadores.first()`
D) `jugadores(0)`
**Respuesta: B**

**17. [R] (Numérica)** ¿Cuál es el resultado de `len(['Barcelona', 'Real Madrid', 'Atletico'])`?
**Respuesta: 3**

**18. [C]** ¿Qué hace el método `.append()` en una lista?
A) Elimina el último elemento
B) Ordena la lista
C) Agrega un elemento al final
D) Cuenta los elementos
**Respuesta: C**

**19. [R]** Si `goles = [1, 0, 2, 3]`, ¿qué devuelve `max(goles)`?
A) 1
B) 2
C) 3
D) 6
**Respuesta: C**

**20. [C]** ¿Cómo obtengo los primeros 2 elementos de `equipos = ['Barça', 'Madrid', 'City']`?
A) `equipos[0:2]`
B) `equipos[1:2]`
C) `equipos[0:1]`
D) `equipos[2]`
**Respuesta: A**

### Diccionarios

**21. [R]** En el diccionario `jugador = {'nombre': 'Messi', 'edad': 36}`, ¿cómo accedo a la edad?
A) `jugador['edad']`
B) `jugador.edad`
C) `jugador[1]`
D) `jugador(edad)`
**Respuesta: A**

**22. [R]** ¿Qué método uso para obtener todas las llaves de un diccionario?
A) `.values()`
B) `.keys()`
C) `.items()`
D) `.get()`
**Respuesta: B**

**23. [R] (Numérica)** Si `estadisticas = {'goles': 25, 'asistencias': 10}`, ¿cuál es `estadisticas['goles'] + estadisticas['asistencias']`?
**Respuesta: 35**

---

## SEMANA 4: INTRODUCCIÓN A PANDAS

### Conceptos Básicos

**24. [C] *Reescrita*** Estás por cargar un archivo CSV con estadísticas de partidos para analizarlo como tabla. ¿Qué instrucción necesitas primero para disponer de la estructura DataFrame?
A) `import pandas`
B) `import pandas as pd`
C) `from pandas import pd`
D) `import pd`
**Respuesta: B**

**25. [R]** ¿Cómo se llama la estructura principal de datos en pandas?
A) Array
B) List
C) DataFrame
D) Dict
**Respuesta: C**

**26. [C]** ¿Qué función uso para leer un archivo CSV en pandas?
A) `pd.open_csv()`
B) `pd.load_csv()`
C) `pd.read_csv()`
D) `pd.import_csv()`
**Respuesta: C**

**27. [C]** Si tengo un DataFrame `df`, ¿cómo veo las primeras 5 filas?
A) `df.first(5)`
B) `df.top(5)`
C) `df.head(5)`
D) `df.show(5)`
**Respuesta: C**

**28. [C] *Reescrita*** Tienes un DataFrame de jugadores y sospechas que la columna 'edad' quedó como texto. ¿Qué comando usas primero para revisar tipos y conteo de valores no nulos?
A) `df.info()`
B) `df.types()`
C) `df.describe()`
D) `df.summary()`
**Respuesta: A**

### Operaciones Básicas

**29. [A] *Reescrita*** Deseas calcular el promedio de goles rápidamente. ¿Qué forma(s) correcta(s) de acceder a la columna permiten luego hacer `mean()` sin pasos extra?
A) `df.goles`
B) `df['goles']`
C) Ambas A y B son correctas
D) `df.select('goles')`
**Respuesta: C**

**30. [R] (Numérica)** Si un DataFrame tiene 50 filas y 4 columnas, ¿qué devuelve `len(df)`?
**Respuesta: 50**

**31. [C] *Reescrita*** Tienes un DataFrame con columnas numéricas (goles, tiros, asistencias) y necesitas un resumen rápido (promedio, mínimo, máximo) para un informe preliminar. ¿Qué comando usas?
A) Muestra tipos de datos
B) Muestra estadísticas descriptivas
C) Muestra primeras filas
D) Cuenta valores únicos
**Respuesta: B**

**32. [A] *Reescrita*** Tienes un DataFrame `df` de jugadores con la columna `goles`. El entrenador pide una lista rápida de goleadores (más de 10 goles) para preparar una sesión especial. ¿Qué instrucción devuelve solo esas filas sin pasos extra?
A) `df[df['goles'] > 10]`
B) `df.filter(goles > 10)`
C) `df.where(goles > 10)`
D) `df.select(goles > 10)`
**Respuesta: A**

---

## SEMANA 5: INTRODUCCIÓN A NUMPY Y VISUALIZACIÓN

### NumPy

**33. [R]** ¿Cuál es el comando correcto para importar numpy?
A) `import numpy`
B) `import numpy as np`
C) `from numpy import np`
D) `import np`
**Respuesta: B**

**34. [R]** ¿Qué función de numpy uso para crear un array con números del 0 al 9?
A) `np.array(10)`
B) `np.range(10)`
C) `np.arange(10)`
D) `np.create(10)`
**Respuesta: C**

**35. [A] (Numérica) *Reescrita*** Una lista de goles por partido de un mediocampista creativo es `[2, 4, 6, 8]`. Usando `np.mean([...])`, ¿qué promedio obtienes para comentar su tendencia ofensiva?
**Respuesta: 5**

**36. [C]** ¿Qué hace `np.random.seed(42)` en numpy?
A) Genera números aleatorios
B) Fija la semilla para reproducibilidad
C) Cuenta elementos
D) Ordena arrays
**Respuesta: B**

### Matplotlib Básico

**37. [R]** ¿Cuál es la forma común de importar matplotlib para gráficos?
A) `import matplotlib as plt`
B) `import matplotlib.pyplot as plt`
C) `import pyplot as plt`
D) `from matplotlib import plt`
**Respuesta: B**

**38. [R]** ¿Qué función uso para mostrar un gráfico en matplotlib?
A) `plt.display()`
B) `plt.show()`
C) `plt.plot()`
D) `plt.draw()`
**Respuesta: B**

**39. [R]** ¿Cómo agrego un título a un gráfico en matplotlib?
A) `plt.name('título')`
B) `plt.title('título')`
C) `plt.header('título')`
D) `plt.label('título')`
**Respuesta: B**

**40. [C]** ¿Qué tipo de gráfico es mejor para mostrar la evolución de goles por mes?
A) Gráfico de barras
B) Gráfico de líneas
C) Gráfico circular
D) Histograma
**Respuesta: B**

---

## APLICACIONES EN FÚTBOL

### Análisis de Datos Futbolísticos

**41. [C]** En el análisis de datos de fútbol, ¿qué tipo de variable es "posición del jugador"?
A) Numérica continua
B) Numérica discreta
C) Categórica
D) Booleana
**Respuesta: C**

**42. [A] (Numérica)** Si un equipo anotó 45 goles en 30 partidos, ¿cuál es su promedio de goles por partido?
**Respuesta: 1.5**

**43. [A]** ¿Cuál es la mejor manera de almacenar información de múltiples jugadores con sus estadísticas?
A) Variables individuales
B) Una lista simple
C) Un diccionario
D) Un DataFrame de pandas
**Respuesta: D**

**44. [C]** En el contexto del fútbol, ¿qué significa "cleaning data" o limpiar datos?
A) Eliminar todos los datos
B) Corregir errores y valores faltantes
C) Ordenar alfabéticamente
D) Crear gráficos
**Respuesta: B**

### Estadísticas Deportivas

**45. [A]** ¿Qué estadística es más útil para comparar goleadores de diferentes equipos?
A) Total de goles
B) Goles por partido
C) Goles en casa
D) Goles por temporada
**Respuesta: B**

**46. [A] (Numérica) *Reescrita*** Registros de goles en 5 partidos: `[2,0,1,3,1]`. Calculas el promedio para decidir si mantiene consistencia mínima (≥1.0). ¿Qué valor obtienes?
**Respuesta: 1.4**

**47. [C] *Reescrita*** Quieres comparar goles totales de 5 equipos en una sola visual para detectar diferencias claras de altura entre valores. ¿Qué tipo de gráfico facilita esa comparación directa?
A) Gráfico de líneas
B) Gráfico de barras
C) Gráfico circular
D) Histograma
**Respuesta: B**

**48. [C]** En análisis deportivo, ¿qué es más importante al presentar datos?
A) Usar muchos colores
B) Mostrar todos los datos posibles
C) Que sean fáciles de entender
D) Usar gráficos en 3D
**Respuesta: C**

---

## RESOLUCIÓN DE PROBLEMAS

### Debugging y Errores Comunes

**49. [R]** ¿Qué error aparece si trato de acceder a `lista[5]` cuando la lista solo tiene 3 elementos?
A) ValueError
B) IndexError
C) KeyError
D) TypeError
**Respuesta: B**

**50. [C]** Si tengo el error "NameError: name 'equipo' is not defined", ¿qué significa?
A) La variable equipo no existe
B) Hay un error de sintaxis
C) El archivo no existe
D) Falta instalar una librería
**Respuesta: A**

**51. [C]** ¿Cuál es la mejor práctica para nombrar variables en Python?
A) usar_guiones_bajos
B) usarCamelCase
C) USAR_MAYUSCULAS
D) Cualquiera está bien
**Respuesta: A**

**52. [R] (Numérica)** Si ejecuto este código, ¿cuántos elementos tendrá la lista final?

```python
goles = []
for i in range(4):
    goles.append(i)
```

**Respuesta: 4**

### Pensamiento Computacional

**53. [C]** ¿Cuál es el primer paso para resolver un problema de programación?
A) Escribir código inmediatamente
B) Entender qué queremos lograr
C) Buscar en Google
D) Usar las librerías más avanzadas
**Respuesta: B**

**54. [C]** ¿Qué significa "iterar" en programación?
A) Repetir un proceso
B) Crear variables
C) Importar librerías
D) Hacer gráficos
**Respuesta: A**

**55. [A]** En el contexto de análisis de datos deportivos, ¿cuál es el orden lógico de trabajo?
A) Visualizar, limpiar, analizar
B) Analizar, limpiar, visualizar
C) Recopilar, limpiar, analizar, visualizar
D) Visualizar, analizar, limpiar
**Respuesta: C**

---

## CONCEPTOS AVANZADOS BÁSICOS

### Manipulación de Datos

**56. [C] *Reescrita*** Tienes un DataFrame de jugadores con columna `posicion` y quieres calcular el promedio de goles por posición para un informe táctico. ¿Qué hace `.groupby('posicion')` combinado con una agregación?
A) Ordena los datos automáticamente
B) Agrupa filas por cada valor de la columna y permite calcular estadísticas por grupo
C) Elimina duplicados antes de contar
D) Genera un gráfico por posición
**Respuesta: B**

**57. [R] (Numérica)** Si tengo una Serie de pandas con valores [10, 20, 30], ¿cuál es el resultado de `.sum()`?
**Respuesta: 60**

**58. [C]** ¿Qué función uso para unir dos DataFrames en pandas?
A) `pd.join()`
B) `pd.merge()`
C) `pd.combine()`
D) `pd.append()`
**Respuesta: B**

**59. [A]** ¿Cómo manejo valores faltantes (NaN) en pandas?
A) Los ignoro
B) Uso `.dropna()` o `.fillna()`
C) Los convierto a 0
D) No se pueden manejar
**Respuesta: B**

### Visualización Avanzada

**60. [C] *Reescrita*** Preparas visualizaciones: necesitas control detallado de cada elemento en un gráfico y, en otro caso, crear rápido un gráfico estadístico atractivo con menos código. ¿Qué comparación es correcta?
A) Son iguales
B) Seaborn facilita gráficos estadísticos de alto nivel sobre matplotlib
C) Matplotlib no puede hacer gráficos
D) Seaborn solo hace gráficos de líneas
**Respuesta: B**

**61. [C]** ¿Qué tipo de gráfico uso para mostrar la distribución de edades de jugadores?
A) Gráfico de barras
B) Gráfico de líneas
C) Histograma
D) Gráfico circular
**Respuesta: C**

**62. [R] (Numérica)** Si quiero crear un gráfico con subplots de 2 filas y 3 columnas, ¿cuántos gráficos individuales puedo hacer?
**Respuesta: 6**

---

## INTEGRACIÓN DE CONCEPTOS

### Proyectos Prácticos

**63. [A]** Para analizar el rendimiento de un equipo durante una temporada, ¿qué estructura de datos es más apropiada?
A) Lista de listas
B) Diccionario simple
C) DataFrame con filas por partido
D) Variables individuales
**Respuesta: C**

**64. [C]** ¿Cuál es la secuencia correcta para crear un análisis básico de datos deportivos?
A) Código → Datos → Análisis → Presentación
B) Datos → Limpieza → Análisis → Visualización
C) Visualización → Datos → Código → Resultados
D) Análisis → Datos → Código → Gráficos
**Respuesta: B**

**65. [A] (Numérica) *Reescrita*** Un reporte pide la eficiencia (goles/tiros) de un delantero: 12 goles, 40 tiros totales. ¿Qué valor entregas (formato decimal)?
**Respuesta: 0.3**

**66. [C]** Para presentar datos de múltiples equipos en una temporada, ¿cuál es la mejor práctica?
A) Un gráfico por equipo
B) Todos los equipos en un solo gráfico comparativo
C) Solo mostrar números
D) Usar colores aleatorios
**Respuesta: B**

### Casos de Uso Real

**67. [A]** Un entrenador quiere identificar a los jugadores con mejor rendimiento. ¿Qué análisis es más útil?
A) Solo mirar goles totales
B) Combinar múltiples métricas (goles, asistencias, partidos jugados)
C) Solo ver la edad
D) Solo ver el equipo
**Respuesta: B**

**68. [R] (Numérica)** Si un DataFrame de partidos tiene columnas ['equipo_local', 'equipo_visitante', 'goles_local', 'goles_visitante'], ¿cuántas columnas necesito para calcular el total de goles por partido?
**Respuesta: 2**

**69. [C]** Para detectar patrones estacionales en el rendimiento de un equipo, ¿qué necesito incluir en mis datos?
A) Solo goles
B) Solo fechas
C) Fechas y métricas de rendimiento
D) Solo nombres de jugadores
**Respuesta: C**

**70. [C]** ¿Cuál es la mejor práctica al compartir un análisis de datos deportivos?
A) Mostrar solo los códigos
B) Incluir contexto, métodos y conclusiones claras
C) Solo mostrar gráficos sin explicación
D) Usar términos técnicos complejos
**Respuesta: B**

**71. [C]** ¿Qué función en Python te permite obtener a la vez el índice y el valor al recorrer una lista de jugadores?
A) range()
B) enumerate()
C) index()
D) position()
**Respuesta: B**

**72. [R]** ¿Cuál es la forma correcta de crear un DataFrame a partir de un diccionario llamado `datos_jugadores`?
A) `pd.DataFrame = datos_jugadores`
B) `DataFrame(datos_jugadores)`
C) `pd.DataFrame(datos_jugadores)`
D) `pd.read_dict(datos_jugadores)`
**Respuesta: C**

**73. [A]** ¿Cómo agregas una nueva columna 'eficiencia' (goles/tiros) a un DataFrame `df` existente?
A) `add df['eficiencia'] = goles/tiros`
B) `df.eficiencia(goles/tiros)`
C) `df['eficiencia'] = df['goles'] / df['tiros']`
D) `df.column('eficiencia', goles/tiros)`
**Respuesta: C**

**74. [C]** ¿Qué produce `df.groupby('posicion').agg({'goles':'mean'})` sobre un DataFrame de jugadores?
A) Elimina la columna 'posicion'
B) Calcula el promedio de goles por cada posición
C) Devuelve solo las filas con mayor número de goles
D) Ordena el DataFrame por goles
**Respuesta: B**

**75. [C]** ¿Cuál es la diferencia principal entre una Serie (Series) y un DataFrame en pandas?
A) Una Serie puede tener múltiples columnas y un DataFrame no
B) No hay diferencia
C) Una Serie es una columna unidimensional; un DataFrame es una tabla bidimensional
D) Un DataFrame solo almacena números y una Serie solo texto
**Respuesta: C**

**76. [A]** ¿Qué instrucción devuelve solo las filas donde goles > 10 y asistencias > 5?
A) `df[df['goles'] > 10 and df['asistencias'] > 5]`
B) `df[(df['goles'] > 10) & (df['asistencias'] > 5)]`
C) `df.where(goles > 10 && asistencias > 5)`
D) `df.filter(goles > 10 & asistencias > 5)`
**Respuesta: B**

**77. [R]** ¿Qué método usas para mostrar una leyenda con las etiquetas de varias líneas en un gráfico de matplotlib?
A) `plt.labels()`
B) `plt.showlegend()`
C) `plt.legend()`
D) `plt.keys()`
**Respuesta: C**

**78. [C]** ¿Cuál es la diferencia entre `df.head()` y `df.info()`?
A) `head()` muestra tipos y `info()` primeras filas
B) `head()` muestra primeras filas; `info()` muestra tipos y resumen estructural
C) Ambas hacen lo mismo
D) `info()` calcula estadísticas numéricas descriptivas
**Respuesta: B**

**79. [R] (Numérica) *Reescrita*** Para generar identificadores de jornadas usas `np.arange(1, 11)`. ¿Cuántas jornadas produce ese array (usa `len(...)`)?
**Respuesta: 10**

**80. [A] (Numérica)** Dada una lista de diccionarios `jugadores = [{'goles':10}, {'goles':12}, {'goles':18}, {'goles':15}]`, ¿cuál es el promedio de goles? (Suma / número de jugadores)
**Respuesta: 13.75**

**81. [R]** ¿Qué tipo de dato devuelve la expresión `3 > 2`?
A) int
B) bool
C) float
D) str
**Respuesta: B**

**82. [R]** ¿Qué operador lógico devuelve True solo si ambas condiciones son True?
A) or
B) not
C) and
D) xor
**Respuesta: C**

**83. [C]** Si `goles = 8` y `asistencias = 5`, ¿qué evalúa `goles > 10 or asistencias >= 5`?
A) True
B) False
C) None
D) Error
**Respuesta: A**

**84. [R] (Numérica)** ¿Qué valor imprime este código?

```python
contador = 0
for i in range(1,6,2):
    contador += 1
print(contador)
```

**Respuesta: 3**

**85. [R]** ¿Qué hace `range(2, 10, 2)`?
A) Genera 2,4,6,8
B) Genera 2,4,6,8,10
C) Genera 2,3,4,5,6,7,8,9
D) Genera 2,10
**Respuesta: A**

**86. [R]** ¿Qué imprime este código?

```python
jugadores = ['Messi','Pedri','Gavi','Lewandowski']
print(jugadores[1:3])
```

A) ['Messi','Pedri','Gavi']
B) ['Pedri','Gavi']
C) ['Gavi','Lewandowski']
D) ['Pedri','Gavi','Lewandowski']
**Respuesta: B**

**87. [R] (Numérica)** Dado `valores = [5,2,9,1]`, ¿cuál es el resultado de `min(valores) + max(valores)`?
**Respuesta: 10**

**88. [C]** ¿Qué diferencia hay entre `lista2 = lista1` y `lista2 = lista1.copy()`?
A) Ninguna, ambas crean copia independiente
B) La primera referencia la misma lista; la segunda crea copia nueva
C) La segunda referencia la misma lista; la primera crea copia nueva
D) Ambas borran la lista original
**Respuesta: B**

**89. [C]** ¿Qué hace `if 'Messi' in jugadores:`?
A) Recorre toda la lista
B) Comprueba si 'Messi' está en la lista
C) Ordena la lista
D) Elimina 'Messi'
**Respuesta: B**

**90. [R] (Numérica)** ¿Cuál es la suma de la lista `[2,3,5]` usando `sum()`?
**Respuesta: 10**

**91. [C]** ¿Qué hace `diccionario['goles'] = 15` si la clave ya existía?
A) Lanza error
B) Agrega una clave duplicada
C) Actualiza el valor a 15
D) Elimina la clave
**Respuesta: C**

**92. [C]** ¿Para qué sirve `diccionario.get('edad', 0)`?
A) Siempre devuelve 0
B) Devuelve 'edad' o 0 si no existe
C) Elimina 'edad'
D) Cambia el valor a 0
**Respuesta: B**

**93. [A] (Numérica)** ¿Resultado de este bloque?

```python
valores = [1,2,3,4]
acum = 0
for v in valores:
    acum += v
print(acum)
```

**Respuesta: 10**

**94. [R]** ¿Qué error produce esta línea: `3 + '2'`?
A) ValueError
B) TypeError
C) NameError
D) IndexError
**Respuesta: B**

**95. [R]** ¿Qué hace `int('7')`?
A) Convierte texto '7' a entero 7
B) Convierte 7 a texto
C) Da error
D) Devuelve float 7.0
**Respuesta: A**

**96. [R]** ¿Qué devuelve `df.shape`?
A) Número de columnas
B) Número de filas
C) Tupla (filas, columnas)
D) Lista de nombres de columnas
**Respuesta: C**

**97. [A]** ¿Cómo ordenas un DataFrame `df` por la columna 'goles' de mayor a menor?
A) `df.sort('goles')`
B) `df.sort_values('goles', ascending=False)`
C) `df.order('goles', desc=True)`
D) `df.desc('goles')`
**Respuesta: B**

**98. [R] (Numérica)** Si `df['goles'] = [2,4,4,0]`, ¿cuál es `df['goles'].mean()`?
**Respuesta: 2.5**

**99. [A]** ¿Qué hace `df['ratio'] = df['goles'] / df['partidos']`?
A) Elimina columnas
B) Crea o reemplaza la columna 'ratio'
C) Renombra el DataFrame
D) Filtra filas
**Respuesta: B**

**100. [C]** ¿Cómo cuentas valores faltantes por columna?
A) `df.countna()`
B) `df.isnull().sum()`
C) `df.na().count()`
D) `df.sum().isnull()`
**Respuesta: B**

**101. [C]** ¿Cuál es la diferencia entre `loc` e `iloc` en pandas?
A) `loc` usa posiciones numéricas; `iloc` etiquetas
B) `loc` usa etiquetas; `iloc` índices numéricos
C) No hay diferencia
D) `iloc` solo funciona con columnas
**Respuesta: B**

**102. [A] (Numérica)** Dado `np.array([1,2,3]) + np.array([4,5,6])`, ¿qué elemento medio (índice 1) resulta?
**Respuesta: 7**

**103. [R]** ¿Qué hace `np.array([1,2,3]).dtype` normalmente?
A) Muestra el tipo de datos del array
B) Convierte a texto
C) Calcula la media
D) Crea un DataFrame
**Respuesta: A**

**104. [R]** ¿Cómo etiquetas el eje X en matplotlib?
A) `plt.axisx('Texto')`
B) `plt.xlabel('Texto')`
C) `plt.xtitle('Texto')`
D) `plt.titlex('Texto')`
**Respuesta: B**

**105. [A]** ¿Cómo cambias el tamaño de una figura antes de graficar?
A) `plt.size(10,5)`
B) `plt.figure(figsize=(10,5))`
C) `plt.dimensions(10,5)`
D) `plt.scale(10,5)`
**Respuesta: B**

**106. [R] (Numérica)** Si `edades = [18,19,20,21]`, ¿cuál es el promedio usando `sum(edades)/len(edades)`?
**Respuesta: 19.5**

**107. [C]** ¿Qué gráfico elegirías para mostrar la proporción de nacionalidades en un plantel pequeño?
A) Gráfico de líneas
B) Gráfico circular simple
C) Histograma
D) Gráfico de dispersión
**Respuesta: B**

**108. [R]** ¿Qué hace `sorted([3,1,2])`?
A) Modifica la lista original
B) Devuelve nueva lista [1,2,3]
C) Devuelve [3,1,2]
D) Elimina duplicados
**Respuesta: B**

**109. [C]** ¿Qué diferencia hay entre `.append()` y `.extend()` en listas?
A) Ninguna
B) append agrega un elemento; extend agrega todos los de otra colección
C) extend agrega un elemento; append agrega varios
D) append ordena; extend filtra
**Respuesta: B**

**110. [R] (Numérica)** Si `plantilla = ['A','B','C']` y ejecuto `plantilla.append('D')`, ¿cuántos elementos hay ahora?
**Respuesta: 4**

**111. [C]** ¿Qué hace este código?

```python
def promedio(a,b=2):
    return (a+b)/2
```

A) Error por parámetro por defecto
B) Crea una función con un parámetro opcional
C) Crea dos funciones
D) No devuelve nada
**Respuesta: B**

**112. [A]** ¿Qué imprime?

```python
x = 5
def f():
    y = 3
    return x + y
print(f())
```

A) 3
B) 5
C) 8
D) Error de variable
**Respuesta: C**

**113. [R]** ¿Qué error describe mejor un bloque mal indentado?
A) SyntaxError
B) IndentationError
C) TypeError
D) NameError
**Respuesta: B**

**114. [R] (Numérica)** Resultado de `float(7) + int(2.5)`
**Respuesta: 9.0**

**115. [C]** ¿Qué hace `value_counts()` sobre una columna categórica?
A) Calcula promedio
B) Cuenta ocurrencias de cada categoría
C) Ordena alfabéticamente
D) Elimina duplicados
**Respuesta: B**

**116. [A]** ¿Cómo renombrar columnas en pandas?
A) `df.rename(columns={'vieja':'nueva'})`
B) `df.columns.rename('vieja','nueva')`
C) `df.col_rename({'vieja':'nueva'})`
D) `df.rename_cols(vieja='nueva')`
**Respuesta: A**

**117. [R] (Numérica)** Si `goles = [0,1,1,2,2,2]`, ¿cuál es la moda (valor más frecuente)?
**Respuesta: 2**

**118. [C]** ¿Qué significa documentación clara en un análisis?
A) Explicar pasos, supuestos y conclusiones
B) Solo mostrar gráficos bonitos
C) Pegar código sin comentarios
D) Ocultar limitaciones
**Respuesta: A**

**119. [A]** ¿Qué instrucción filtra filas donde goles > 10 O asistencias > 7?
A) `df[(df['goles'] > 10) | (df['asistencias'] > 7)]`
B) `df[df['goles'] > 10 or df['asistencias'] > 7]`
C) `df.where(goles > 10 || asistencias > 7)`
D) `df.filter(goles > 10 | asistencias > 7)`
**Respuesta: A**

**120. [A] (Numérica)** Si un jugador hizo 9 goles en 30 partidos, ¿cuál es su promedio de goles por partido? (2 decimales)
**Respuesta: 0.30**

---

## Instrucciones Técnicas para Canvas

### Configuración de Preguntas

- **Opción múltiple**: Preguntas 1-120 (excepto numéricas)
- **Respuesta numérica**: Preguntas marcadas como (Numérica)
- **Selección aleatoria**: 25 preguntas por examen (sugerido) para mayor variedad
- **Categorías para balance (sugerido)**:
  - Fundamentos Python / Control (25%): 1-15, 49-55, 81-90, 94-95, 106, 108-110, 113-114
  - Estructuras de datos básicas (15%): 16-23, 86-93, 107-109, 117
  - Funciones y pensamiento modular (10%): 11-15, 111-112
  - Pandas / Manipulación (20%): 24-32, 56-59, 72-76, 96-105, 115-116, 119
  - NumPy y operaciones (10%): 33-36, 79, 98, 102-103
  - Visualización (10%): 37-40, 60-62, 77-78, 104-105
  - Integración / Aplicaciones deportivas (10%): 41-48, 63-71, 80, 97, 100, 118, 120

### Ponderación Sugerida

- Cada pregunta: 4 puntos (examen de 25 = 100 puntos)
- Tiempo: 45-60 minutos
- Intentos permitidos: 1
- Mostrar respuestas correctas: Después del cierre
