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

Actualmente el banco contiene 75 preguntas. Todas forman parte del Núcleo provisional (cobertura mínima). La fase de expansión añadirá 30–45 ítems adicionales (Extended) para llegar a 105–120, incorporando más preguntas de interpretación ([S]) y escenarios.

### Núcleo (75 preguntas)
Preguntas 1–75.

### Banco Extendido (Pendiente)
Se agregarán preguntas 76+ manteniendo numeración continua (sin renumerar Núcleo) con foco en:
- Interpretación de salidas de pandas y visualizaciones
- Razonamiento sobre calidad de datos
- Mini escenarios deportivos multi‑métrica

### Uso Sugerido
- Evaluaciones formales: muestrear mayormente Núcleo (≥85%).
- Práctica/Refuerzo: incorporar gradualmente Extended al publicarse.

### Distribución Cognitiva Actual (aprox)
- [R] Recuerdo: ~18
- [C] Concepto: ~36
- [A] Aplicación (incluye Numéricas): ~21

Meta tras expansión: equilibrar hacia 35–40% [R], 35–40% [C], 20–25% [A] y 5–10% [S].

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

### Configuración de Preguntas:
- **Opción múltiple**: Preguntas 1-75 (excepto numéricas)
- **Respuesta numérica**: Preguntas marcadas como (Numérica)
- **Selección aleatoria**: 20-25 preguntas por examen
- **Categorías para balance**:
  - Exploración básica (25%): Preguntas 1-20
  - Tipos de datos (25%): Preguntas 21-40
  - Visualización (25%): Preguntas 41-55
  - Análisis avanzado (25%): Preguntas 56-75

### Ponderación Sugerida:
- Cada pregunta: 4-5 puntos
- Total por examen: 80-100 puntos
- Tiempo: 45-60 minutos
- Intentos permitidos: 1
- Mostrar respuestas correctas: Después del cierre

### Enfoque Pedagógico:
- Énfasis en aplicación práctica en contexto deportivo
- Combinación de conceptos técnicos con interpretación
- Preguntas que evalúan tanto conocimiento como comprensión
- Integración de herramientas (pandas, seaborn, matplotlib)