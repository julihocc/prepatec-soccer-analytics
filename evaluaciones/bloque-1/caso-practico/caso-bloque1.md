# Caso Práctico Colaborativo - Bloque 1
## Análisis del Rendimiento de un Club de Fútbol

**Modalidad:** Colaborativa (equipos de 3-4 estudiantes)  
**Ponderación:** 15% del 1er Parcial  
**Duración:** 2 semanas  
**Entrega:** Notebook de Jupyter + presentación de 10 minutos

---

## Contexto del Problema

Tu equipo ha sido contratado como analistas junior por un club de fútbol local. El director técnico necesita un informe sobre el rendimiento del equipo durante la última temporada para tomar decisiones sobre fichajes y estrategias.

**Situación:** El club tiene datos básicos de la temporada pasada pero necesita convertir esos números en información útil para la toma de decisiones.

---

## Objetivos de Aprendizaje

Al completar este caso práctico, los estudiantes serán capaces de:
- Aplicar fundamentos de Python para resolver problemas reales
- Trabajar colaborativamente en análisis de datos
- Crear funciones personalizadas para cálculos deportivos
- Manipular listas y diccionarios con datos futbolísticos
- Presentar resultados de forma clara y profesional

---

## Datos Proporcionados

### Dataset: `temporada_club.csv`
```csv
partido,fecha,rival,local_visitante,goles_favor,goles_contra,resultado
1,2023-08-15,Deportivo Atlas,Local,2,1,Victoria
2,2023-08-22,Club América,Visitante,0,3,Derrota
3,2023-08-29,Pumas UNAM,Local,1,1,Empate
...
```

### Dataset: `jugadores_rendimiento.csv`
```csv
jugador,posicion,edad,partidos_jugados,goles,asistencias,tarjetas_amarillas,tarjetas_rojas
Carlos Vela,Delantero,34,28,15,8,3,0
Andrés Guardado,Mediocampo,37,30,2,12,5,1
...
```

---

## Tareas Requeridas

### Parte 1: Análisis Básico con Python (40 puntos)

#### 1.1 Configuración del Entorno (5 puntos)
- Importar las librerías necesarias
- Configurar el entorno de trabajo
- Cargar los datos usando pandas

#### 1.2 Exploración de Datos (10 puntos)
- Crear variables para almacenar estadísticas básicas
- Usar estructuras de control para contar victorias, empates y derrotas
- Implementar bucles para calcular totales de goles

**Código requerido:**
```python
# Ejemplo de lo que deben implementar
victorias = 0
empates = 0
derrotas = 0

for resultado in lista_resultados:
    if resultado == "Victoria":
        victorias += 1
    elif resultado == "Empate":
        empates += 1
    else:
        derrotas += 1
```

#### 1.3 Creación de Funciones (15 puntos)
Crear las siguientes funciones obligatorias:

**a) Función para calcular puntos:**
```python
def calcular_puntos(victorias, empates, derrotas):
    """
    Calcula puntos según sistema FIFA: Victoria=3, Empate=1, Derrota=0
    """
    # Su implementación aquí
    return puntos_totales
```

**b) Función para evaluar rendimiento:**
```python
def evaluar_rendimiento(goles_favor, goles_contra):
    """
    Determina si el rendimiento es: Excelente, Bueno, Regular, Deficiente
    """
    # Su implementación aquí
    return categoria
```

**c) Función para análisis de jugador:**
```python
def analizar_jugador(goles, partidos, edad):
    """
    Calcula promedio de goles y determina si es prometedor
    """
    # Su implementación aquí
    return promedio, es_prometedor
```

#### 1.4 Manipulación de Estructuras de Datos (10 puntos)
- Crear listas con estadísticas de cada partido
- Usar diccionarios para organizar información de jugadores
- Implementar operaciones de slicing y indexing

**Ejemplo requerido:**
```python
# Organizar jugadores por posición
jugadores_por_posicion = {
    'Delanteros': [],
    'Mediocampos': [],
    'Defensas': [],
    'Porteros': []
}
```

### Parte 2: Análisis de Rendimiento (35 puntos)

#### 2.1 Estadísticas del Equipo (15 puntos)
- Calcular total de puntos obtenidos
- Determinar promedio de goles por partido
- Analizar rendimiento como local vs visitante
- Identificar la racha más larga (victorias/derrotas consecutivas)

#### 2.2 Análisis Individual de Jugadores (10 puntos)
- Identificar al goleador del equipo
- Encontrar al jugador con más asistencias
- Calcular la edad promedio del plantel
- Determinar qué posición anota más goles

#### 2.3 Insights y Recomendaciones (10 puntos)
- ¿En qué posición necesita refuerzos el equipo?
- ¿Cuál es el punto fuerte del equipo?
- ¿Qué jugador tiene mejor rendimiento por edad?

### Parte 3: Presentación y Documentación (25 puntos)

#### 3.1 Notebook Limpio (15 puntos)
- Código bien documentado con comentarios
- Uso correcto de markdown para explicaciones
- Estructura clara y lógica
- Sin errores de ejecución

#### 3.2 Presentación Grupal (10 puntos)
- 10 minutos máximo
- Cada integrante debe participar
- Mostrar hallazgos principales
- Responder preguntas del profesor y compañeros

---

## Entregables

### 1. Notebook de Jupyter (`caso_bloque1_equipo[X].ipynb`)
- Código completo y funcional
- Análisis paso a paso
- Comentarios explicativos
- Conclusiones claras

### 2. Archivo de Presentación (`presentacion_equipo[X].pdf`)
- 5-8 diapositivas máximo
- Hallazgos principales
- Recomendaciones concretas

### 3. Reporte Ejecutivo (`reporte_equipo[X].pdf`)
- 2 páginas máximo
- Resumen para el director técnico
- Lenguaje no técnico
- Recomendaciones accionables

---

## Criterios de Evaluación

### Rúbrica de Evaluación (100 puntos total)

| Criterio | Excelente (90-100) | Bueno (80-89) | Suficiente (70-79) | Insuficiente (<70) |
|----------|-------------------|---------------|-------------------|-------------------|
| **Código Python** | Funciona perfectamente, uso correcto de todos los conceptos | Funciona con errores menores | Funciona parcialmente | No funciona o tiene errores graves |
| **Funciones** | Todas las funciones implementadas correctamente | 2-3 funciones correctas | 1-2 funciones correctas | Funciones incorrectas o faltantes |
| **Análisis** | Insights profundos y útiles | Análisis correcto pero básico | Análisis superficial | Análisis incorrecto |
| **Colaboración** | Participación equitativa demostrable | Buena colaboración | Colaboración básica | Falta evidencia de trabajo colaborativo |
| **Presentación** | Excelente comunicación, dominio del tema | Buena presentación | Presentación básica | Presentación deficiente |

### Componentes de la Calificación:
- **Análisis Técnico (40%):** Correctitud del código y funciones
- **Aplicación de Conceptos (30%):** Uso apropiado de Python fundamentals
- **Trabajo Colaborativo (15%):** Evidencia de trabajo en equipo
- **Comunicación (15%):** Calidad de presentación y reportes

---

## Cronograma de Trabajo

### Semana 1:
- **Días 1-2:** Formación de equipos y exploración de datos
- **Días 3-4:** Implementación de funciones básicas
- **Días 5-7:** Análisis de estadísticas del equipo

### Semana 2:
- **Días 1-3:** Análisis de jugadores y insights
- **Días 4-5:** Preparación de presentación
- **Días 6-7:** Presentaciones grupales

---

## Recursos de Apoyo

### Tutoriales Recomendados:
- Repaso de funciones en Python
- Manipulación de listas y diccionarios
- Lectura de archivos CSV con pandas
- Mejores prácticas de documentación

### Ejemplos de Código:
```python
# Ejemplo de análisis básico
def analisis_basico(datos):
    """Función ejemplo para mostrar estructura"""
    resultados = {}
    
    for columna in datos.columns:
        if columna.startswith('goles'):
            resultados[columna] = datos[columna].sum()
    
    return resultados
```

### Preguntas Guía:
1. ¿Cómo puedo usar bucles para procesar cada partido?
2. ¿Qué estructura de datos es mejor para organizar información de jugadores?
3. ¿Cómo puedo hacer que mis funciones sean reutilizables?
4. ¿Qué insights son más valiosos para un director técnico?

---

## Notas Importantes

- **Plagio:** Cada equipo debe desarrollar su propio código
- **Consultas:** Se permite consultar documentación oficial y tutoriales
- **Herramientas:** Solo se permite usar conceptos vistos en Bloque 1
- **Formato:** Todos los archivos deben seguir la convención de nombres especificada
- **Fecha límite:** No se aceptan entregas tardías

---

*Este caso práctico está diseñado para aplicar todos los conceptos fundamentales de Python en un contexto deportivo real, preparando a los estudiantes para análisis más avanzados en bloques posteriores.*