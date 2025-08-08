# Rúbricas de Evaluación - Bloque 2
## Exploración de Datos Deportivos

**Ponderación del Bloque:** 35% de la calificación final  
**Componentes:** Examen Canvas (20%) + Caso Práctico Colaborativo (15%)

---

## Examen Canvas (20% de la calificación total)

### Configuración Automática
- **Preguntas totales:** 75 en el banco
- **Preguntas por examen:** 20-25 (selección aleatoria)
- **Tiempo límite:** 45-60 minutos
- **Intentos:** 1 único intento
- **Calificación:** Automática, 100 puntos

### Distribución por Temas:
| Tema | % del Examen | Preguntas |
|------|--------------|-----------|
| Exploración de datos | 25% | 5-6 |
| Tipos de datos deportivos | 25% | 5-6 |
| Estadística descriptiva | 25% | 5-6 |
| Visualización con seaborn | 25% | 5-6 |

---

## Caso Práctico Colaborativo (15% de la calificación total)

### "Análisis Básico de Jugadores de Fútbol"
**Modalidad:** Equipos de 2-3 estudiantes  
**Duración:** 1 semana

### Criterios de Evaluación Simplificada (100 puntos)

#### 1. Exploración Básica de Datos (40 puntos)
- **Carga de datos (10 pts):**
  - Importa pandas, seaborn, matplotlib correctamente: 5 pts
  - Carga el dataset sin errores: 5 pts
- **Exploración inicial (15 pts):**
  - Usa `.head()` para ver primeras filas: 3 pts
  - Usa `.info()` o `.describe()` para información básica: 4 pts
  - Cuenta jugadores por posición con `.value_counts()`: 4 pts
  - Calcula estadísticas básicas (promedio, máximo, mínimo): 4 pts
- **Identificación de patrones básicos (15 pts):**
  - Identifica quién marcó más goles: 5 pts
  - Encuentra diferencias entre posiciones: 5 pts
  - Responde preguntas básicas sobre los datos: 5 pts

#### 2. Análisis por Posición (30 puntos)
- **Uso de .groupby() (15 pts):**
  - Agrupa datos por posición correctamente: 8 pts
  - Calcula promedios de goles y asistencias: 7 pts
- **Identificación de mejores jugadores (15 pts):**
  - Encuentra el mejor jugador por posición: 10 pts
  - Interpreta correctamente los resultados: 5 pts

#### 3. Visualizaciones Básicas (20 puntos)
- **Gráficos obligatorios (15 pts):**
  - Gráfico de barras: jugadores por posición: 5 pts
  - Gráfico de cajas: goles por posición: 5 pts
  - Gráfico de dispersión: goles vs asistencias: 5 pts
- **Calidad de gráficos (5 pts):**
  - Títulos descriptivos en español: 2 pts
  - Etiquetas de ejes claras: 2 pts
  - Uso correcto de la paleta viridis: 1 pt

#### 4. Presentación Final (10 puntos)
- **Presentación simple (10 pts):**
  - 3-4 diapositivas con gráficos principales: 4 pts
  - Responde preguntas básicas del análisis: 3 pts
  - Cada integrante explica lo que aprendió: 3 pts

---

## Escala de Calificación del Bloque

### Conversión Final (35% del curso):
- **Examen Canvas:** 20% × (calificación/100)
- **Caso Práctico:** 15% × (calificación/100)
- **Total Bloque 2:** Suma de ambos componentes

### Niveles de Dominio Simplificados:
- **Excelente (90-100%):** Completa todas las tareas correctamente
- **Competente (80-89%):** Realiza la mayoría de las tareas con pequeños errores
- **Suficiente (70-79%):** Cumple con los requerimientos básicos
- **Insuficiente (<70%):** No logra completar las tareas principales

---

## Criterios Específicos de Evaluación

### ¿Qué Busco en el Código?
- **Funciona sin errores:** El código se ejecuta completamente
- **Usa las funciones correctas:** `.head()`, `.groupby()`, `.value_counts()` 
- **Variables en español:** `datos_jugadores`, `goleadores_top`
- **Comentarios explicativos:** Explican qué hace cada parte

### ¿Qué Busco en los Gráficos?
- **Gráficos obligatorios:** Los 3 tipos solicitados (barras, cajas, dispersión)
- **Títulos descriptivos:** "¿Qué posición marca más goles?" en lugar de "Graph"
- **Etiquetas claras:** Nombres de ejes en español
- **Paleta correcta:** Usa `palette="viridis"` como se enseñó

### ¿Qué Busco en el Trabajo en Equipo?
- **Participación equitativa:** Todos los integrantes contribuyen
- **División clara:** Cada persona tiene responsabilidades definidas
- **Coordinación:** El trabajo final está integrado

---

## Entregables Específicos

### Caso Práctico Bloque 2:
1. **analisis_jugadores_equipo[X].ipynb** - Notebook principal
2. **presentacion_equipo[X].pdf** - Presentación simple de 3-4 diapositivas

### Lo que Debe Funcionar:
- **Código ejecutable:** Todo el notebook se ejecuta sin errores
- **Análisis completo:** Incluye exploración, análisis por posición y gráficos
- **Presentación clara:** Comunica los hallazgos principales
- **Trabajo colaborativo:** Evidencia de que todos participaron

---

*Este bloque evalúa la capacidad de explorar datos básicos y crear visualizaciones simples usando pandas y seaborn en contextos deportivos.*