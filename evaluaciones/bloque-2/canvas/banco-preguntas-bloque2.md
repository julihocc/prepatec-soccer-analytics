# Banco de Preguntas Canvas - Bloque 2

## Explorando Datos Deportivos con Python

**Instrucciones para Canvas:**

- Todas las preguntas son de opción múltiple: 4 opciones (A, B, C, D)
- 25 preguntas por examen (5 por cada semana del Bloque 2)
- Tiempo sugerido: 45-60 minutos
- Etiquetas cognitivas: [R]=Recuerdo, [C]=Concepto, [A]=Aplicación

---

## Distribución de Preguntas por Semana

**Semana 6: Introducción a la exploración de datos** (5 preguntas)
**Semana 7: Tipos de datos en fútbol** (5 preguntas)  
**Semana 8: Estadística descriptiva básica** (5 preguntas)
**Semana 9: Visualización avanzada de datos** (5 preguntas)
**Semana 10: Análisis e interpretación** (5 preguntas)

### Distribución Cognitiva

- [R] Recuerdo: 8 preguntas
- [C] Concepto: 11 preguntas  
- [A] Aplicación: 6 preguntas

**Nota:** Todas las preguntas son de opción múltiple para facilitar la evaluación automática en Canvas.

---

## SEMANA 6: INTRODUCCIÓN A LA EXPLORACIÓN DE DATOS

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

**3. [A]** ¿Qué tipo de gráfico es mejor para mostrar "¿Cuántos goles marcan los equipos locales?"
A) Gráfico de líneas
B) Gráfico circular
C) `sns.countplot()`
D) Histograma complejo
**Respuesta: C**

**4. [A]** Si de 30 partidos analizados, 15 los ganó el local, 8 el visitante y 7 fueron empates, ¿qué porcentaje representan las victorias locales?
A) 40%
B) 50%
C) 60%
D) 45%
**Respuesta: B**

**5. [C]** ¿Cuál es la principal ventaja de usar seaborn sobre matplotlib básico?
A) Es más rápido
B) Crea gráficos bonitos automáticamente
C) Solo funciona con datos deportivos
D) No necesita matplotlib
**Respuesta: B**

---

## SEMANA 7: TIPOS DE DATOS EN FÚTBOL

**6. [C]** En el análisis de fútbol, ¿qué son los "datos de resultados"?
A) Solo los goleadores
B) Información básica del partido: equipos, goles, fecha, competición
C) Estadísticas de cada jugador
D) Solo la posición en la tabla
**Respuesta: B**

**7. [C]** ¿Qué información contienen los "datos de eventos" en fútbol?
A) Solo el resultado final
B) Información detallada: goles, tarjetas, sustituciones con minuto exacto
C) Solo los nombres de equipos
D) Solo estadísticas de temporada
**Respuesta: B**

**8. [A]** ¿Cómo creo una fecha aleatoria en Python para simular datos?
A) `fecha = random.date()`
B) `fecha = f"2023-{np.random.randint(1, 13):02d}-{np.random.randint(1, 29):02d}"`
C) `fecha = datetime.now()`
D) `fecha = "2023"`
**Respuesta: B**

**9. [C]** Para simular goles con distribución realista, ¿qué función de numpy es más apropiada?
A) `np.random.randint()`
B) `np.random.choice()`
C) `np.random.poisson()`
D) `np.random.normal()`
**Respuesta: C**

**10. [C]** ¿Qué ventaja tiene usar `np.random.seed(42)` al crear datos simulados?
A) Hace los datos más realistas
B) Garantiza reproducibilidad - todos obtienen los mismos datos
C) Acelera la generación
D) Crea más variedad
**Respuesta: B**

---

## SEMANA 8: ESTADÍSTICA DESCRIPTIVA BÁSICA

**11. [C]** ¿Qué mide el promedio (mean) en el contexto de datos de fútbol?
A) El valor más alto
B) El valor típico o central de una variable
C) El valor más bajo
D) La diferencia entre valores
**Respuesta: B**

**12. [A]** Si tres jugadores anotaron 10, 15 y 8 goles respectivamente, ¿cuál es el promedio?
A) 10
B) 11
C) 12
D) 15
**Respuesta: B**

**13. [R]** En pandas, ¿qué método calcula automáticamente varias estadísticas descriptivas?
A) `.info()`
B) `.head()`
C) `.describe()`
D) `.count()`
**Respuesta: C**

**14. [A]** ¿Qué tipo de gráfico es mejor para comparar goles promedio entre posiciones?
A) Gráfico de líneas
B) `sns.boxplot()`
C) Gráfico circular
D) Scatter plot
**Respuesta: B**

**15. [C]** ¿Qué muestra un histograma de edades de jugadores?
A) Los nombres de los jugadores
B) La distribución/frecuencia de diferentes edades
C) Solo la edad máxima
D) El equipo de cada jugador
**Respuesta: B**

---

## SEMANA 9: VISUALIZACIÓN AVANZADA DE DATOS

**16. [C]** ¿Cuándo uso un gráfico de barras en análisis deportivo?
A) Para mostrar cambios en el tiempo
B) Para comparar categorías (equipos, posiciones, etc.)
C) Para mostrar relaciones entre variables
D) Solo para datos numéricos continuos
**Respuesta: B**

**17. [A]** ¿Qué tipo de gráfico es mejor para mostrar la evolución de goles a lo largo de un partido?
A) Gráfico de barras
B) Gráfico de líneas con tiempo en x
C) Gráfico circular
D) Histograma
**Respuesta: B**

**18. [C]** ¿Para qué sirve `sns.scatterplot()` en análisis deportivo?
A) Contar elementos
B) Mostrar relación entre dos variables (ej: tiros vs goles)
C) Solo hacer puntos decorativos
D) Comparar categorías
**Respuesta: B**

**19. [R]** ¿Cómo agrego etiquetas a los ejes en un gráfico?
A) `plt.xlabel()` y `plt.ylabel()`
B) `sns.labels()`
C) `graph.label()`
D) No se pueden agregar
**Respuesta: A**

**20. [A]** Si quiero mostrar porcentajes en un gráfico circular y tengo 3 categorías con 10, 15 y 5 elementos respectivamente, ¿qué porcentaje representa la segunda categoría?
A) 40%
B) 50%
C) 60%
D) 33%
**Respuesta: B**

---

## SEMANA 10: ANÁLISIS E INTERPRETACIÓN

**21. [C]** Al analizar datos, ¿cuál es el primer paso como "detective de datos"?
A) Hacer gráficos inmediatamente
B) Contar y sumar - obtener estadísticas básicas
C) Crear presentaciones
D) Buscar datos en internet
**Respuesta: B**

**22. [C]** ¿Qué significa encontrar que el promedio de goles por partido es 2.1?
A) Todos los partidos tuvieron exactamente 2.1 goles
B) Es el valor típico, algunos tendrán más y otros menos
C) Es un error en los datos
D) Solo cuenta goles de un equipo
**Respuesta: B**

**23. [A]** ¿Cuál es la secuencia correcta del análisis de datos?
A) Gráficos → Datos → Interpretación
B) Contar/Sumar → Comparar → Graficar → Interpretar
C) Interpretación → Datos → Gráficos
D) Solo hacer gráficos
**Respuesta: B**

**24. [R]** ¿Cómo identifico el resultado más común en mis datos?
A) Solo mirar el primer dato
B) Usar `.mode()` o contar frecuencias con `.value_counts()`
C) Adivinar
D) No es posible saberlo
**Respuesta: B**

**25. [A]** Si defino "partidos emocionantes" como aquellos con 3+ goles, y de 50 partidos, 15 cumplen esta condición, ¿cuál es la tasa de partidos emocionantes?
A) 25%
B) 30%
C) 35%
D) 40%
**Respuesta: B**

---
