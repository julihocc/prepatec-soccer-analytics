# Banco de Preguntas Canvas - Bloque 2

## Explorando Datos Deportivos con Python

**Instrucciones para Canvas:**

- Preguntas de opción múltiple: 4 opciones (A, B, C, D)
- Preguntas numéricas: respuesta exacta con tolerancia del 5%
- Selección aleatoria de 20-25 preguntas por examen
- Tiempo sugerido: 45-60 minutos
- Etiquetas cognitivas: [R]=Recuerdo, [C]=Concepto, [A]=Aplicación *(Bloque 2: aún sin [S] Socrática, se añadirá en expansión)*

---

## Selección Núcleo (Core) y Plan de Expansión

El banco contiene 105 preguntas (75 Core + 30 Extended). Las preguntas 1–75 constituyen el Núcleo (cobertura mínima) y las 76–105 conforman la primera expansión Extended con introducción de etiqueta [S] (Socrática/Interpretativa).

### Núcleo (75 preguntas)

Preguntas 1–75 (sin cambios).

### Banco Extendido (30 preguntas)

Preguntas 76–105 (interpretación, refuerzo de recall y escenarios):

- Interpretación de salidas de pandas y visualizaciones (boxplots, dispersión, conteos)
- Razonamiento sobre calidad de datos y efecto de outliers
- Mini escenarios deportivos multi‑métrica y relevancia práctica de diferencias pequeñas

### Uso Sugerido

- Evaluaciones formales: muestrear mayormente Núcleo (≥85%).
- Práctica/Refuerzo: incorporar gradualmente Extended al publicarse.

### Distribución Cognitiva (aprox tras expansión)

- [R] Recuerdo: 37
- [C] Concepto: 37
- [A] Aplicación (incluye Numéricas): 23
- [S] Socrática/Interpretativa: 8

La expansión elevó [R] (déficit previo) e introdujo [S] dentro del rango objetivo (≈7.6%). Ajustes futuros menores podrán refinar equilibrio.

---

## SEMANA 6: INTRODUCCIÓN A LA EXPLORACIÓN DE DATOS

### Conceptos Fundamentales

**1. [C]** En el análisis de datos deportivos, ¿qué información básica contiene cada partido?
A) Solo el marcador final
B) Equipos, goles, fechas y competiciones
C) Solo los nombres de los jugadores
D) Solo la fecha del partido
**Respuesta: B**

**2. [R]** ¿Cuál es la configuración correcta para importar seaborn para gráficos bonitos?
A) `import seaborn`
B) `import seaborn as sns`
C) `from seaborn import sns`
D) `import sns`
**Respuesta: B**

**3. [R]** ¿Qué comando configura un tema bonito en seaborn?
A) `sns.config()`
B) `sns.style()`
C) `sns.set_theme()`
D) `sns.setup()`
**Respuesta: C**

**4. [A] (Numérica)** Si tengo datos de 30 partidos con un promedio de 2.4 goles por partido, ¿cuál es el total aproximado de goles?
**Respuesta: 72**

**5. [C]** Al trabajar con datos de fútbol, ¿qué representa mejor el rendimiento ofensivo de un equipo?
A) Solo goles totales
B) Goles por partido
C) Nombre del equipo
D) Color de la camiseta
**Respuesta: B**

### Visualización Básica

**6. [A]** ¿Qué tipo de gráfico es mejor para mostrar "¿Cuántos goles marcan los equipos locales?"
A) Gráfico de líneas
B) Gráfico circular
C) `sns.countplot()`
D) Histograma complejo
**Respuesta: C**

**7. [C]** Para analizar si "es mejor jugar en casa", ¿qué debo crear primero?
A) Una columna que identifique quién ganó cada partido
B) Un gráfico de líneas
C) Una lista de equipos
D) Estadísticas de jugadores
**Respuesta: A**

**8. [R]** ¿Qué función uso para agregar título a un gráfico en seaborn/matplotlib?
A) `plt.name()`
B) `plt.title()`
C) `sns.title()`
D) `graph.title()`
**Respuesta: B**

**9. [A] (Numérica)** Si de 30 partidos analizados, 15 los ganó el local, 8 el visitante y 7 fueron empates, ¿qué porcentaje representan las victorias locales?
**Respuesta: 50**

**10. [C]** ¿Cuál es la principal ventaja de usar seaborn sobre matplotlib básico?
A) Es más rápido
B) Crea gráficos bonitos automáticamente
C) Solo funciona con datos deportivos
D) No necesita matplotlib
**Respuesta: B**

---

## SEMANA 7: TIPOS DE DATOS EN FÚTBOL

### Clasificación de Datos

**11. [C]** En el análisis de fútbol, ¿qué son los "datos de resultados"?
A) Solo los goleadores
B) Información básica del partido: equipos, goles, fecha, competición
C) Estadísticas de cada jugador
D) Solo la posición en la tabla
**Respuesta: B**

**12. [C]** ¿Qué información contienen los "datos de eventos" en fútbol?
A) Solo el resultado final
B) Información detallada: goles, tarjetas, sustituciones con minuto exacto
C) Solo los nombres de equipos
D) Solo estadísticas de temporada
**Respuesta: B**

**13. [A] (Numérica)** Si creo un dataset con equipos de 3 ligas y 2 temporadas, con 4 equipos por liga, ¿cuántos registros tendré en total?
**Respuesta: 24**

**14. [C]** ¿Cuál es la estructura más común para organizar datos de fútbol?
A) Archivos de texto simple
B) Formato tabular (CSV, Excel, bases de datos)
C) Solo imágenes
D) Documentos PDF
**Respuesta: B**

**15. [C]** En el contexto de datos de fútbol, ¿qué son las "estadísticas de equipo"?
A) Solo el nombre del equipo
B) Rendimiento colectivo: posesión, precisión de pases, corners
C) Solo los jugadores titulares
D) Solo los resultados históricos
**Respuesta: B**

### Manipulación de Datos

**16. [A]** ¿Cómo creo una fecha aleatoria en Python para simular datos?
A) `fecha = random.date()`
B) `fecha = f"2023-{np.random.randint(1, 13):02d}-{np.random.randint(1, 29):02d}"`
C) `fecha = datetime.now()`
D) `fecha = "2023"`
**Respuesta: B**

**17. [C]** Para simular goles con distribución realista, ¿qué función de numpy es más apropiada?
A) `np.random.randint()`
B) `np.random.choice()`
C) `np.random.poisson()`
D) `np.random.normal()`
**Respuesta: C**

**18. [R] (Numérica)** Si uso `np.random.poisson(1.5)` para simular goles, ¿cuál es el promedio esperado de goles?
**Respuesta: 1.5**

**19. [A]** ¿Cómo simulo la selección de dos equipos diferentes para un partido?
A) Seleccionar equipos al azar sin restricción
B) Elegir un equipo, luego otro excluyendo el primero
C) Solo usar equipos de la misma liga
D) Siempre usar los mismos equipos
**Respuesta: B**

**20. [C]** ¿Qué ventaja tiene usar `np.random.seed(42)` al crear datos simulados?
A) Hace los datos más realistas
B) Garantiza reproducibilidad - todos obtienen los mismos datos
C) Acelera la generación
D) Crea más variedad
**Respuesta: B**

---

## SEMANA 8: ESTADÍSTICA DESCRIPTIVA BÁSICA

### Medidas de Tendencia Central

**21. [C]** ¿Qué mide el promedio (mean) en el contexto de datos de fútbol?
A) El valor más alto
B) El valor típico o central de una variable
C) El valor más bajo
D) La diferencia entre valores
**Respuesta: B**

**22. [A] (Numérica)** Si tres jugadores anotaron 10, 15 y 8 goles respectivamente, ¿cuál es el promedio?
**Respuesta: 11**

**23. [C]** ¿Cuál es la diferencia entre máximo y mínimo en estadística descriptiva?
A) Son lo mismo
B) Máximo es el valor más alto, mínimo el más bajo
C) Solo se usan con fechas
D) No tienen relevancia en fútbol
**Respuesta: B**

**24. [R]** En pandas, ¿qué método calcula automáticamente varias estadísticas descriptivas?
A) `.info()`
B) `.head()`
C) `.describe()`
D) `.count()`
**Respuesta: C**

**25. [C]** ¿Por qué es útil calcular el promedio de goles por posición de jugador?
A) Para ver qué posición anota más típicamente
B) Para contar jugadores
C) Para ordenar alfabéticamente
D) No tiene utilidad
**Respuesta: A**

### Visualización Estadística

**26. [A]** ¿Qué tipo de gráfico es mejor para comparar goles promedio entre posiciones?
A) Gráfico de líneas
B) `sns.boxplot()`
C) Gráfico circular
D) Scatter plot
**Respuesta: B**

**27. [C] (Numérica)** Si el promedio de goles por partido en mis datos es 2.1, ¿cómo interpretaría esto?
A) Son partidos muy emocionantes (si >2.5)
B) Son partidos con pocos goles (si <2.5)
C) Partidos normales con buenos goles
D) Según el contexto del promedio
**Respuesta: B**

**28. [C]** ¿Qué muestra un histograma de edades de jugadores?
A) Los nombres de los jugadores
B) La distribución/frecuencia de diferentes edades
C) Solo la edad máxima
D) El equipo de cada jugador
**Respuesta: B**

**29. [C]** En un boxplot, ¿qué información puedo obtener sobre los datos?
A) Solo el promedio
B) Mediana, cuartiles, valores atípicos
C) Solo los valores máximos
D) La cantidad total de datos
**Respuesta: B**

**30. [R]** ¿Cuál es la configuración recomendada para gráficos con seaborn?
A) `sns.set_theme(style="whitegrid", palette="Set2")`
B) No configurar nada
C) Solo cambiar colores
D) Usar matplotlib solamente
**Respuesta: A**

---

## SEMANA 9: VISUALIZACIÓN AVANZADA DE DATOS

### Tipos de Gráficos

**31. [C]** ¿Cuándo uso un gráfico de barras en análisis deportivo?
A) Para mostrar cambios en el tiempo
B) Para comparar categorías (equipos, posiciones, etc.)
C) Para mostrar relaciones entre variables
D) Solo para datos numéricos continuos
**Respuesta: B**

**32. [A]** ¿Qué tipo de gráfico es mejor para mostrar la evolución de goles a lo largo de un partido?
A) Gráfico de barras
B) Gráfico de líneas con tiempo en x
C) Gráfico circular
D) Histograma
**Respuesta: B**

**33. [R] (Numérica)** Si creo subplots con `plt.subplots(2, 2)`, ¿cuántos gráficos individuales puedo hacer?
**Respuesta: 4**

**34. [C]** ¿Para qué sirve `sns.scatterplot()` en análisis deportivo?
A) Contar elementos
B) Mostrar relación entre dos variables (ej: tiros vs goles)
C) Solo hacer puntos decorativos
D) Comparar categorías
**Respuesta: B**

**35. [C]** ¿Qué muestra un histograma de "total de goles por partido"?
A) Los nombres de los equipos
B) Cuántos partidos tuvieron 0, 1, 2, 3... goles
C) Solo el partido con más goles
D) Los mejores jugadores
**Respuesta: B**

### Personalización de Gráficos

**36. [R]** ¿Cómo agrego etiquetas a los ejes en un gráfico?
A) `plt.xlabel()` y `plt.ylabel()`
B) `sns.labels()`
C) `graph.label()`
D) No se pueden agregar
**Respuesta: A**

**37. [C]** ¿Qué hace `plt.xticks(rotation=45)` en un gráfico?
A) Rota todo el gráfico
B) Rota las etiquetas del eje x para mejor lectura
C) Cambia los colores
D) No hace nada
**Respuesta: B**

**38. [A] (Numérica)** Si quiero mostrar porcentajes en un gráfico circular y tengo 3 categorías con 10, 15 y 5 elementos respectivamente, ¿qué porcentaje representa la segunda categoría?
**Respuesta: 50**

**39. [C]** ¿Para qué uso `plt.tight_layout()` al crear múltiples gráficos?
A) Para hacer gráficos más grandes
B) Para evitar solapamiento entre subplots
C) Para cambiar colores
D) Para guardar el gráfico
**Respuesta: B**

**40. [C]** ¿Cuál es la mejor práctica para colores en gráficos de análisis deportivo?
A) Usar colores aleatorios
B) Usar paletas predefinidas como 'Set2' o 'viridis'
C) Solo usar negro
D) Cambiar colores constantemente
**Respuesta: B**

---

## SEMANA 10: ANÁLISIS E INTERPRETACIÓN

### Interpretación de Resultados

**41. [C]** Al analizar datos, ¿cuál es el primer paso como "detective de datos"?
A) Hacer gráficos inmediatamente
B) Contar y sumar - obtener estadísticas básicas
C) Crear presentaciones
D) Buscar datos en internet
**Respuesta: B**

**42. [C]** ¿Qué significa encontrar que el promedio de goles por partido es 2.1?
A) Todos los partidos tuvieron exactamente 2.1 goles
B) Es el valor típico, algunos tendrán más y otros menos
C) Es un error en los datos
D) Solo cuenta goles de un equipo
**Respuesta: B**

**43. [A] (Numérica)** Si en 30 partidos, 8 tuvieron 3 o más goles, ¿qué porcentaje representan los "partidos emocionantes"?
**Respuesta: 26.7**

**44. [A]** ¿Cuál es la secuencia correcta del análisis de datos?
A) Gráficos → Datos → Interpretación
B) Contar/Sumar → Comparar → Graficar → Interpretar
C) Interpretación → Datos → Gráficos
D) Solo hacer gráficos
**Respuesta: B**

**45. [C]** Cuando encuentro que un equipo tiene más empates que otros, ¿qué debo preguntarme?
A) No significa nada
B) ¿Es estadísticamente significativo? ¿Hay razones tácticas?
C) ¿Cuál es su color favorito?
D) Solo contar más partidos
**Respuesta: B**

### Búsqueda de Patrones

**46. [C]** ¿Qué son "patrones" en el análisis de datos deportivos?
A) Diseños gráficos
B) Tendencias o comportamientos regulares en los datos
C) Solo números altos
D) Colores en los gráficos
**Respuesta: B**

**47. [A] (Numérica)** Si defino "partidos emocionantes" como aquellos con 3+ goles, y de 50 partidos, 15 cumplen esta condición, ¿cuál es la tasa de partidos emocionantes?
**Respuesta: 30**

**48. [R]** ¿Cómo identifico el resultado más común en mis datos?
A) Solo mirar el primer dato
B) Usar `.mode()` o contar frecuencias con `.value_counts()`
C) Adivinar
D) No es posible saberlo
**Respuesta: B**

**49. [A]** En el análisis de "¿es mejor jugar en casa?", ¿qué debo comparar?
A) Solo goles de local
B) Victorias locales vs visitantes vs empates
C) Solo nombres de equipos
D) Solo fechas de partidos
**Respuesta: B**

**50. [A]** ¿Qué tipo de visualización ayuda a identificar patrones temporales?
A) Gráficos de barras estáticos
B) Gráficos de líneas con tiempo o scatter con colores
C) Solo tablas de números
D) Gráficos circulares
**Respuesta: B**

---

## ANÁLISIS INTEGRADO

### Combinación de Datos

**51. [A]** Para analizar el rendimiento de equipos, ¿qué datos debo combinar?
A) Solo resultados de partidos
B) Resultados + estadísticas de jugadores + datos de equipo
C) Solo nombres de equipos
D) Solo datos de una temporada
**Respuesta: B**

**52. [R]** ¿Qué función de pandas uso para agrupar datos por equipo?
A) `.sort()`
B) `.filter()`
C) `.groupby()`
D) `.merge()`
**Respuesta: C**

**53. [A] (Numérica)** Si un DataFrame tiene datos de jugadores agrupados por equipo y calculo `.agg({'goles': 'sum', 'partidos': 'mean'})`, ¿cuántas métricas obtengo por equipo?
**Respuesta: 2**

**54. [A]** ¿Cómo combino eficientemente datos de diferentes fuentes (jugadores + equipos)?
A) Copiar y pegar manualmente
B) Usar `pd.merge()` con columnas comunes
C) No se puede hacer
D) Solo usar un dataset
**Respuesta: B**

**55. [C]** En un análisis combinado, ¿qué muestra una matriz de correlación?
A) Los nombres de las variables
B) Cómo se relacionan numéricamente diferentes métricas
C) Solo valores máximos
D) Colores aleatorios
**Respuesta: B**

### Visualización Avanzada

**56. [C]** ¿Para qué sirve `sns.heatmap()` en análisis deportivo?
A) Solo para decorar
B) Para mostrar correlaciones entre métricas de rendimiento
C) Para contar jugadores
D) Para mostrar fechas
**Respuesta: B**

**57. [C]** ¿Qué información obtengo de un heatmap de correlaciones?
A) Nombres de jugadores
B) Qué métricas se relacionan positiva o negativamente
C) Solo colores bonitos
D) Fechas de partidos
**Respuesta: B**

**58. [C] (Numérica)** En un heatmap de correlaciones, si veo un valor de 0.85 entre "tiros" y "goles", ¿qué significa?
A) No hay relación
B) Relación positiva fuerte
C) Relación negativa
D) Error en los datos
**Respuesta: B**

**59. [C]** ¿Cuál es la ventaja de usar subplots para mostrar múltiples aspectos de los datos?
A) Ocupa más espacio
B) Permite comparar diferentes dimensiones del análisis simultáneamente
C) Es más difícil de entender
D) Solo funciona con datos numéricos
**Respuesta: B**

**60. [A]** ¿Qué configuración uso para un heatmap legible?
A) `sns.heatmap(data, annot=True, cmap='coolwarm')`
B) Solo `sns.heatmap(data)`
C) `plt.plot(data)`
D) No necesita configuración
**Respuesta: A**

---

## CONCEPTOS AVANZADOS

### Limpieza y Calidad de Datos

**61. [C]** ¿Qué significa "cleaning data" en el contexto deportivo?
A) Eliminar todos los datos
B) Corregir errores, manejar valores faltantes, validar consistencia
C) Solo ordenar alfabéticamente
D) Hacer gráficos más bonitos
**Respuesta: B**

**62. [A]** ¿Cómo valido la consistencia entre datasets de partidos y eventos?
A) No es necesario validar
B) Verificar que los IDs coincidan y las fechas sean coherentes
C) Solo mirar los primeros datos
D) Confiar que estén correctos
**Respuesta: B**

**63. [A] (Numérica)** Si un dataset de resultados tiene 400 partidos pero el dataset de eventos solo tiene datos para 100, ¿qué porcentaje de cobertura tengo?
**Respuesta: 25**

**64. [A]** ¿Qué debo verificar al cargar datos de fútbol desde archivos CSV?
A) Solo que se carguen
B) Tipos de datos, valores faltantes, rangos válidos
C) Solo el tamaño del archivo
D) Los colores del gráfico
**Respuesta: B**

**65. [A]** ¿Cómo manejo fechas inconsistentes en datos deportivos?
A) Las ignoro
B) Las elimino todas
C) Uso `pd.to_datetime()` y valido formatos
D) Las dejo como texto
**Respuesta: C**

### Interpretación Estadística

**66. [A]** ¿Qué debo considerar al interpretar que "los locales ganan más"?
A) Es una verdad absoluta
B) El tamaño de muestra, significancia estadística, contexto
C) Solo el porcentaje
D) No significa nada
**Respuesta: B**

**67. [C]** En el análisis de eficiencia de jugadores, ¿por qué es mejor usar goles/partido que goles totales?
A) Es más fácil de calcular
B) Normaliza por oportunidad - es más justo para comparar
C) Los totales no importan
D) Solo es tradición
**Respuesta: B**

**68. [A] (Numérica)** Si un jugador tiene 0.75 goles por partido y otro 0.65, ¿cuál es la diferencia en eficiencia?
**Respuesta: 0.1**

**69. [C]** ¿Qué precauciones debo tomar con datos simulados vs datos reales?
A) Ninguna, son iguales
B) Los simulados son para aprender métodos, los reales pueden tener sesgos
C) Solo usar datos simulados
D) Solo usar datos reales
**Respuesta: B**

**70. [C]** ¿Cuál es la importancia de la reproducibilidad en análisis deportivo?
A) No es importante
B) Permite validar resultados y metodología
C) Solo para parecer profesional
D) Es opcional
**Respuesta: B**

---

## CASOS PRÁCTICOS INTEGRADOS

### Análisis Completo

**71. [A]** Para un análisis completo de rendimiento de equipo, ¿cuál es la secuencia lógica?
A) Solo mirar goles
B) Datos → Limpieza → Exploración → Visualización → Interpretación
C) Hacer gráficos primero
D) Solo usar estadísticas básicas
**Respuesta: B**

**72. [C]** ¿Qué métricas son esenciales para evaluar un delantero?
A) Solo goles totales
B) Goles/partido, eficiencia (goles/tiros), asistencias
C) Solo la edad
D) Solo el equipo
**Respuesta: B**

**73. [A] (Numérica)** Para determinar si un equipo es "goleador", si el promedio general es 1.8 goles por partido, ¿a partir de qué promedio considerarías un equipo como "muy goleador"?
**Respuesta: 2.5**

**74. [C]** En un dashboard de análisis deportivo, ¿qué elementos son esenciales?
A) Solo números
B) Métricas clave, visualizaciones claras, contexto interpretativo
C) Solo gráficos bonitos
D) Muchas decoraciones
**Respuesta: B**

**75. [A]** ¿Cómo presento hallazgos de análisis deportivo a no-expertos?
A) Con mucha terminología técnica
B) Visualizaciones claras, lenguaje simple, conclusiones prácticas
C) Solo mostrar código
D) Solo números sin contexto
**Respuesta: B**

---

## Instrucciones Técnicas para Canvas

### Configuración de Preguntas

- **Opción múltiple**: Preguntas 1-105 (excepto numéricas)
- **Respuesta numérica**: Preguntas marcadas como (Numérica)
- **Selección aleatoria**: 20-25 preguntas por examen (evaluación formal: 22 fijas estratificadas)
- **Categorías para balance**:
  - Exploración básica (25%): 1-20
  - Tipos de datos (25%): 21-40
  - Visualización (20%): 41-55
  - Análisis avanzado (15%): 56-75
  - Interpretación / Escenarios (15% uso gradual): 76-105

### Ponderación Sugerida

- Cada pregunta: 4-5 puntos
- Total por examen: 80-100 puntos
- Tiempo: 45-60 minutos
- Intentos permitidos: 1
- Mostrar respuestas correctas: Después del cierre
- Recomendación: ≥85% de ítems de Núcleo en evaluaciones formales; Extended para refuerzo interpretativo.

### Enfoque Pedagógico

- Énfasis en aplicación práctica en contexto deportivo
- Combinación de conceptos técnicos con interpretación
- Preguntas que evalúan conocimiento, comprensión, aplicación y juicio interpretativo
- Integración de herramientas (pandas, seaborn, matplotlib)

---

## BANCO EXTENDIDO (Preguntas 76–105)

### Interpretación, Escenarios y Refuerzo de Fundamentos

**76. [R]** ¿Qué función de pandas muestra estadísticas básicas (media, std, min, max) de columnas numéricas?
A) `df.stats()`
B) `df.describe()`
C) `df.profile()`
D) `df.summary()`
**Respuesta: B**

**77. [R]** ¿Qué método cuenta frecuencias de valores en una serie (por ejemplo, posiciones de jugadores)?
A) `serie.count_values()`
B) `serie.value_counts()`
C) `serie.values_count()`
D) `serie.counts()`
**Respuesta: B**

**78. [R]** ¿Qué instrucción convierte una columna `edad` a entero?
A) `df['edad'] = df['edad'].astype(int)`
B) `df['edad'] = int(df['edad'])`
C) `df.astype('edad', int)`
D) `df.to_int('edad')`
**Respuesta: A**

**79. [R]** ¿Qué función genera un boxplot sencillo con seaborn para la columna `goles`?
A) `sns.lineplot(data=df, x='goles')`
B) `sns.boxplot(data=df, y='goles')`
C) `sns.scatterplot(data=df, y='goles')`
D) `sns.histplot(data=df, y='goles')`
**Respuesta: B**

**80. [R]** ¿Qué devuelve `df.shape`?
A) Número de columnas solamente
B) Una tupla (filas, columnas)
C) Solo número de filas
D) El tamaño en bytes
**Respuesta: B**

**81. [R]** ¿Qué hace `df.isna().sum()`?
A) Elimina valores faltantes
B) Cuenta valores faltantes por columna
C) Reemplaza valores faltantes con cero
D) Ignora valores faltantes
**Respuesta: B**

**82. [R]** ¿Qué método ordena un DataFrame por la columna `goles` descendente?
A) `df.order('goles')`
B) `df.sort_values('goles', ascending=False)`
C) `df.sort('goles', desc=True)`
D) `df.order_values('goles', reverse=True)`
**Respuesta: B**

**83. [R]** ¿Qué instrucción muestra las primeras 3 filas?
A) `df.head(3)`
B) `df.top(3)`
C) `df.first(3)`
D) `df.head3()`
**Respuesta: A**

**84. [R]** ¿Qué función restablece el índice tras un groupby?
A) `df.flatten_index()`
B) `df.reset_index()`
C) `df.new_index()`
D) `df.index_reset()`
**Respuesta: B**

**85. [R]** ¿Cuál es la regla simple usada en el curso para marcar un outlier alto?
A) media + 2*desviación estándar
B) mediana + 3
C) máximo + 1
D) media - 2*desviación estándar
**Respuesta: A**

**86. [R]** ¿Qué librería usamos para fijar un tema visual uniforme?
A) `matplotlib`
B) `pandas`
C) `seaborn`
D) `numpy`
**Respuesta: C**

**87. [R]** ¿Cuál es el rango realista típico de goles por partido en datos simulados básicos del curso?
A) 0-10
B) 0-7
C) 0-4
D) 0-1
**Respuesta: C**

**88. [R]** ¿Qué etiqueta describe mejor una variable como `posicion` (Portero, Defensa, Delantero)?
A) Numérica continua
B) Categórica
C) Binaria
D) Temporal
**Respuesta: B**

**89. [R]** ¿Qué diferencia principal hay entre `mean` y `median`?
A) Son siempre iguales
B) La media se afecta más por valores extremos
C) La mediana se afecta más por outliers
D) Ninguna, son idénticas siempre
**Respuesta: B**

**90. [R]** ¿Qué función aplica un cálculo por grupos (ej. promedio de goles por posición)?
A) `df.groupby('posicion').mean()`
B) `df.group('posicion').avg()`
C) `df.by('posicion').mean()`
D) `df.split('posicion').mean()`
**Respuesta: A**

**91. [R]** ¿Cuál es la convención de nombres de variables adoptada en el curso?
A) camelCase en todo
B) snake_case descriptivo
C) PascalCase para variables
D) Nombres de una letra siempre
**Respuesta: B**

**92. [R]** ¿Qué instrucción rota etiquetas del eje x 45 grados (matplotlib)?
A) `plt.rotate(45)`
B) `plt.xticks(rotation=45)`
C) `plt.xlabel(rotate=45)`
D) `plt.xlabels(45)`
**Respuesta: B**

**93. [R]** ¿Cuál es la diferencia básica entre `countplot` y `barplot` en seaborn (uso típico en este curso)?
A) `countplot` cuenta ocurrencias categóricas automáticamente
B) `barplot` siempre apila barras
C) `countplot` requiere datos agregados previos
D) No hay diferencia funcional
**Respuesta: A**

**94. [C]** ¿Por qué puede ser preferible la mediana a la media al comparar goles por partido en presencia de un jugador extremadamente prolífico?
A) Porque es más rápida de calcular
B) Porque ignora valores faltantes automáticamente
C) Porque reduce la influencia de un valor extremo y representa mejor el grupo
D) Porque siempre da un número mayor
**Respuesta: C**

**95. [A] (Numérica)** Si un jugador tiene 12 goles y 6 asistencias en 18 partidos, ¿cuál es su `contribucion_ofensiva` (goles + asistencias por partido)?
**Respuesta: 1.0**

**96. [A]** Un equipo tiene promedio de 1.8 goles, pero al remover un outlier (partido de 7 goles) baja a 1.6. ¿Qué conclusión es más adecuada?
A) El outlier inflaba la media, la producción típica es menor
B) El equipo dejó de ser bueno
C) No cambia nada interpretativamente
D) La mediana se vuelve un outlier
**Respuesta: A**

**97. [S]** Observas un boxplot de goles por delantero con un bigote superior muy largo. ¿Qué pregunta crítica debes plantearte antes de concluir que los delanteros son volátiles?
A) ¿Cuántos defensas hay?
B) ¿Cuántos puntos extremos reales hay y cuántas observaciones totales?
C) ¿Qué color tiene el gráfico?
D) ¿Cuál es el nombre del archivo?
**Respuesta: B**

**98. [S]** Falta la edad de 5 porteros (NA) en un dataset pequeño. ¿Qué acción es más razonable y por qué?
A) Eliminar toda la columna edad
B) Rellenar con la media general para no perder comparabilidad básica
C) Reemplazar con 0
D) Ignorar porque no afecta nada
**Respuesta: B**

**99. [S]** Dos posiciones tienen mismo promedio de goles pero una muestra mayor desviación estándar. ¿Qué interpretación es correcta?
A) La posición con mayor dispersión es menos consistente
B) Ambas son igualmente consistentes
C) La mayor dispersión significa mejores jugadores siempre
D) No se puede interpretar nada
**Respuesta: A**

**100. [S]** En un gráfico, un delantero con 15 goles sobre 10 partidos y los demás entre 0-5. ¿Qué deberías comunicar al entrenador?
A) Que todos son igual de efectivos
B) Que la media está sesgada por un jugador excepcional
C) Que la mediana también es muy alta
D) Que no se pueden usar métricas
**Respuesta: B**

**101. [S]** Observas que la media de goles por partido sube de 1.6 a 1.7 tras limpiar NA (remover filas vacías). ¿Qué interpretación es más prudente?
A) El equipo mejoró realmente
B) El cambio puede ser efecto de eliminar filas con menos goles
C) No tiene explicación
D) Significa que hubo manipulación
**Respuesta: B**

**102. [S]** Diferencia de eficiencia: 0.05 goles/partido entre dos delanteros (1.10 vs 1.05). ¿Cómo comunicarlo?
A) Como una diferencia enorme definitiva
B) Como una diferencia pequeña que puede no ser decisiva sin más contexto
C) Como que el segundo es inservible
D) Como que ambos son outliers
**Respuesta: B**

**103. [S]** Un scatter muestra relación ligera entre edad y asistencias (nube dispersa sin clara pendiente). ¿Qué dices?
A) Hay correlación fuerte
B) No se observa relación clara; otras variables podrían explicar asistencias
C) La edad causa asistencias directamente
D) Debemos usar modelos avanzados inmediatamente
**Respuesta: B**

**104. [S]** Tras agrupar por posición, ves que delanteros tienen media alta y mediana similar, mientras mediocampistas tienen media > mediana. ¿Qué implica para mediocampistas?
A) Distribución posiblemente sesgada por algunos valores altos
B) Total homogeneidad
C) No hay outliers
D) La mediana es inválida
**Respuesta: A**

**105. [S]** Si al añadir una métrica derivada (`contribucion_ofensiva`) las conclusiones sobre top 3 jugadores cambian respecto a sólo goles, ¿qué recomendación haces?
A) Ignorar la métrica nueva
B) Incorporar la métrica derivada porque ofrece visión más completa
C) Eliminar jugadores nuevos
D) Volver a datos en bruto únicamente
**Respuesta: B**

---

Fin de preguntas Extended.
